import bcrypt
from typing import Union
from app.models import User
from fastapi import FastAPI
from app.database import create_supabase_client

app = FastAPI()

supabase = create_supabase_client()

def user_exists(key:str = "email", value:str =None ):
    user= supabase.from_("users").select('*').eq(key,value ).execute()
    return len(user.data)> 0

#CREATE/POST
@app.post("/user")
def create_user(user: User):
        user_email = user.email.lower()
        #TODO implement hashing for password
        hashed_password = user.password
        # hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

        if user_exists(value=user_email):
            return {'message': 'User already exists'}
        
        user = supabase.from_("users")\
            .insert({"name": user.name, "email": user_email, "password": hashed_password}).execute()

        if user:    
            return {"message": "User created successfully"}
        else:
            raise Exception({"message": "User creation failed"})
        
 #GET
@app.get('/user')
def get_user(user_id: Union[str,None] = None):
    if user_id:
        user = supabase.from_("users")\
            .select("id","name","email")\
            .eq("id",user_id)\
            .execute()
        
    if user:
        return user
    
    else:
        users = supabase.from_("users").select('*').execute()

    if users:
        return users
    else:
        raise Exception({"message": "User not found"})
     
# UPDATE/PUT
@app.put("/user")
def update_user(user_id: str,email: str, name: str):
    user_email = email.lower()

    if user_exists(value=user_email):
        email_exists = supabase.from_("users").select("*").eq("email",user_email).execute()
        if len(email_exists.data) > 0:
            return {"message": "Email already exists"}
    user = supabase.from_("users").update("name": name, "email": email).eq("id", user_id).execute()
    if user:
        return {"message": "User updated successfully"}
    else:
        raise Exception({"message": "User update failed"})

@app.get("/")
def main_route():
    return {'message': 'Hello main route'}

@app.get("/health")
def health_check():
    return {'message': 'Healthy'}
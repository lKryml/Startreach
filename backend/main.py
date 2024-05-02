import bcrypt
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
 

@app.get("/")
def main_route():
    return {'message': 'Hello main route'}

@app.get("/health")
def health_check():
    return {'message': 'Healthy'}
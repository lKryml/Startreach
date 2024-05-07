from fastapi import FastAPI
import uvicorn

app = FastAPI()

# @app.get("/")
# def main_route():
#     return {'message': 'Hello main route'}

# @app.get("/health")
# def health_check():
#     return {'message': 'Healthy'}

# @app.get('/countries')
# def get_countries():
#     countries = supabase.from_("countries").select('*').execute()
#     return countries

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5555)
   

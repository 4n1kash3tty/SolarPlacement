from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return{"message":"The backend is running!"}
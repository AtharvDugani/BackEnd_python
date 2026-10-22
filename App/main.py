from fastapi import FastAPI
app = FastAPI(title = "Student API")
@app.get("/")
def home():
    return{
        "message":"Welcome to Student API"
    }
from fastapi import APIRouter


auth = APIRouter()

@auth.get("/")
def user_get():
    return "Hola desde el auth"
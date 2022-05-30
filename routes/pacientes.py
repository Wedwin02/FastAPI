from fastapi import APIRouter


paciente = APIRouter()

@paciente.get("/paciente")
def user_get():
    return "Hola desde el get"
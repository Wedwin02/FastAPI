from fastapi import FastAPI
from routes.pacientes import paciente
from routes.auth import auth
app = FastAPI()


app.include_router(auth)
app.include_router(paciente)
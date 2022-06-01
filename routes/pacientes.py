from fastapi import APIRouter
from sqlalchemy import values
from config.db import conn
from models.paciente import pacientes
from schemas.pacientes import S_Paciente

paciente = APIRouter()


@paciente.get("/paciente")
def get_paciente():    
    return conn.execute(pacientes.select()).fetchall()

@paciente.post("/paciente")
def pos_paciente(paciente:S_Paciente):
    new_paciente = {"DNI":paciente.DNI,"Nombre":paciente.Nombre,"Direccion":paciente.Direccion,"CodigoPostal":paciente.CodigoPostal,"Telefono":paciente.Telefono,"Genero":paciente.Genero,"FechaNacimiento":paciente.FechaNacimiento,"Correo":paciente.Correo}
    resultado = conn.execute(pacientes.insert().values(new_paciente)) 
    print(resultado)
    return  "Succesful"
#Seleccion por id
@paciente.get("/paciente/{id}")
def getById_paciente(id:int):
    conn.execute(pacientes.select().where(pacientes.c.PacienteId==id)).first()   
    return  "Succesful"
    
#metodo elimininar 
@paciente.delete("/paciente/{id}")
def delete_paciente(id:int):
    conn.execute(pacientes.delete().where(pacientes.c.PacienteId==id))
    return "Succesful"

@paciente.put("/paciente/{id}")
def put_paciente(id:int,paciente:S_Paciente):
    conn.execute(pacientes.update().values(DNI=paciente.DNI,Nombre=paciente.Nombre,Direccion=paciente.Direccion,CodigoPostal=paciente.CodigoPostal,
    Telefono=paciente.Telefono,Genero=paciente.Genero,FechaNacimiento=paciente.FechaNacimiento,Correo=paciente.Correo).where(pacientes.c.PacienteId==id))
    return "Update"
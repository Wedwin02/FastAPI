from typing import Optional
from pydantic import BaseModel

class S_Paciente(BaseModel):
        PacienteId:Optional[int]
        DNI:str
        Nombre:str
        Direccion:str
        CodigoPostal:str
        Telefono:str
        Genero:str
        FechaNacimiento:str
        Correo:str
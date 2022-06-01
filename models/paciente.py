from msilib import Table
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

#Se crea la tabla en la base de datos
pacientes = Table("pacientes",meta,Column(
    "PacienteId",Integer, primary_key =  True),
    Column("DNI",String(45)),
    Column("Nombre",String(150)),
    Column("Direccion",String(45)),
    Column("CodigoPostal",String(45)),
    Column("Telefono",String(45)),
    Column("Genero",String(45)),
    Column("FechaNacimiento",String(45)),
    Column("Correo",String(45))
)

# config.py
import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://admin:acer@cluster0.wdbuqoa.mongodb.net/personal_medico?retryWrites=true&w=majority")
    
#Si usas MongoDB Atlas, reemplaza "mongodb://localhost:27017/mi_base" por tu cadena de conexión de Atlas.
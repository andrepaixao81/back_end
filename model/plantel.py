from sqlalchemy import Column, String, Integer, DateTime, Date
from datetime import datetime, date
from typing import Union

from model.base import Base

class Plantel(Base):
    __tablename__ = 'plantel'

    id = Column(Integer, primary_key=True)
    anilha = Column(String(50), unique=True)
    especie = Column(String(100))
    mutacao = Column(String (250))
    sexo = Column(String(1))
    data_nascimento = Column(String(10))
    data_cadastro = Column(DateTime, default=datetime.now())        

    
def __init__(self, anilha:str, especie:str, mutacao:str, sexo:str, 
             data_nascimento:date, data_cadastro:Union[DateTime, None] = None):
    
    """
        Cadastra os dados básicos de uma ave do plantel.
        O cadastro é constituido pelos seguintes dados abaixo:

        Arguments:
            anilha: Número de identificação da ave. É um número único.
            especia: Espécie da ave (Nome comum).
            mutação: Mutação da ave (Cores e outros).            
            sexo: Sexo da ave.
            data_nascimento: Data de nascimento da ave.
            data_cadastro: Data de quando a ave foi inserida à base de dados.
        """
        
    self.anilha = anilha  
    self.especie = especie  
    self.mutacao = mutacao
    self.sexo = sexo
    self.data_nascimento = data_nascimento
    # se não for informada a data de cadastro dos dados,
    # será inserido a data exata da inserção no banco.
    if data_cadastro:
            self.data_cadastro = data_cadastro

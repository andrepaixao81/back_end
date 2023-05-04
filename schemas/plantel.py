from pydantic import BaseModel, Field
from typing import Optional, List
from model import Plantel


class PlantelSchema(BaseModel):
    """_summary_
    Define como o dado deverá ser inserido
    """
    anilha: str = "FOB001"
    especie: str = "Calopsita"
    mutacao: str = "Cinza Cara Branca Prata Recessivo"
    sexo: str = "M"
    data_nascimento: str = "01/01/2020"
        
class PlantelBuscaSchema(BaseModel):
    """
    Define como deverá ser realizada a busca
    """
    anilha: str = "FOB001"
    
class PlantelListSchema(BaseModel):
    """ Define como uma listagem de dados será retornado.
    """
    plantel:PlantelSchema

class PlantelViewSchema(BaseModel):
    """ Define como o cadastro de uma ave será retornada obj.
    """
    id: int = 1
    anilha: str = "FOB001"
    especie: str = "Calopsita"
    mutacao: str = "Arlequim Pastel Face Prata Recessivo"
    sexo: str = "M"
    data_nascimento: str = "15-01-2023"
    
        
class PlantelDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str

class PlantelUpdateSchema(BaseModel):
    """_summary_
    Define como o dado deverá ser inserido
    """
    anilha: str = "FOB001"
    especie: str = "Ring Neck"
    mutacao: str = "Azul"
    sexo: str = "F"
    data_nascimento: str = "23/05/2018"

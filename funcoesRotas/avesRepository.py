from connectionDB.connection import DBConnectionHandler
from model.plantel import Plantel
from sqlalchemy.orm.exc import NoResultFound
import json
from sqlalchemy_utils import JSONType
from pydantic import BaseModel
from typing import Optional, List
from connectionDB import Session
from sqlalchemy.exc import IntegrityError



import jsons
class ObjectJson:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

#Função para serializable o JSON
def encoder_ave(ave):
        if isinstance (ave, Plantel):
            return {"id":ave.id,"anilha":ave.anilha, "especie":ave.especie, "mutacao":ave.mutacao, "sexo":ave.sexo, "data_nascimento":ave.data_nascimento}
        raise TypeError(f"Object {ave} não é do tipo Plantel")
    

class plantelRepository:
    """
    Está classe contém todas as funções do CRUD
    
    """   
    #Função cadastra uma ave no banco de dados
    def cadastrar(self, ave):
        
        plantel = ave
        with DBConnectionHandler() as db:
            
            
            try:
                session = Session()
                session.add(plantel)
                session.commit()
                
                # return {"Ave cadastrada com sucesso. Anilha: {plantel.anilha}"}
                
                    
            except IntegrityError as e:
                        # como a duplicidade do nome é a provável razão do IntegrityError
                        error_msg = "Número de anilha já cadastrada na base de dados."
                        return {"mesage": error_msg}, 409

            except Exception as e:
                        # caso um erro fora do previsto
                        error_msg = "Não foi possível cadastrar está ave."
                        return {"mesage": error_msg}, 400   
        
            return (f"Ave cadastrada com sucesso. Anilha: {plantel.anilha}", 200)
                    
              

    #Função exibe todos os registro do banco de dados
    def select_all(self):
        
        with DBConnectionHandler() as db:
            data = db.session.query(Plantel).all()
                    
        result = []
        for ave in data:
            result.append({
                "id": ave.id,
                "anilha": ave.anilha,
                "especie": ave.especie,
                "mutacao": ave.mutacao,
                "sexo": ave.sexo,
                "data_nascimento": ave.data_nascimento
                })

        return {"aves": result}
             
    
    #Função para atualizar os dados de uma ave
    def update(self, anilha, especie, mutacao, sexo, data_nascimento):
        with DBConnectionHandler() as db:
            ave = db.session.query(Plantel).filter(Plantel.anilha == anilha).update({"especie": especie, "mutacao":mutacao, "sexo":sexo, "data_nascimento":data_nascimento})
            db.session.commit()

            if not ave:
                # se o Número de Anilha não for localizado
                error_msg = "Número de anilha não localizada no banco de dados."
                return {"mesage": error_msg}, 404
            else:
                
                return ({"Ave autalizada com sucesso. Anilha":anilha}), 200
        
        
        
    #Função busca uma ave pelo Número da Anilha
    def select_anilha(self, anilha: str):
        with DBConnectionHandler() as db:
            
            ave = db.session.query(Plantel).filter(Plantel.anilha == anilha).first()
            db.session.commit()
                                   
            if not ave:
                # se o Número de Anilha não for localizado
                error_msg = "Número de anilha não localizada no banco de dados."
                return {"mesage": error_msg}, 404
            else:
                # retorna a representação de produto
                resultado = json.dumps(ave, default=encoder_ave, indent=4)

                return resultado, 200

    #Função para deletar um ave da base de dados
    def deletar(self, anilha: str):
        with DBConnectionHandler() as db:
            
            ave = db.session.query(Plantel).filter(Plantel.anilha == anilha).delete()
            db.session.commit()
                                   
            if not ave:
                # se o Número de Anilha não for localizado
                error_msg = "Número de anilha não localizada no banco de dados."
                return {"mesage": error_msg}, 404
            else:
                # retorna a representação de produto

                return ({"Ave apagada com sucesso. Anilha":anilha}), 200



from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, json, jsonify
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model.plantel import Plantel
from connectionDB import Session
from logger import logger
from funcoesRotas.avesRepository import plantelRepository
from schemas import *
from flask_cors import CORS

from json import JSONDecoder



info = Info(title="API do Plantel", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

add = plantelRepository()


 
# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
plantel_tag = Tag(name="Plantel", description="Cadastro, visualização e remoção de aves à base de dados.")

#Rotas da API
# Rotas POST, GET e DELETE

#Rota da documentação
@app.get('/', tags=[home_tag] )
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')



#Cadastrar ave
@app.post('/plantel/cadastrar', tags=[plantel_tag],
          responses={"200": PlantelViewSchema, "409": ErrorSchema, "400": ErrorSchema, "201":PlantelSchema})
def cadastrar(form: PlantelSchema):
    """Realiza o cadastro de uma ave no banco de dados.

    Retorna uma mensagem com os dados da ave.
    """
    plantel = Plantel(anilha=form.anilha,
                      especie=form.especie,
                      mutacao=form.mutacao,
                      sexo=form.sexo,
                      data_nascimento=form.data_nascimento
                      )
    dados = add.cadastrar(plantel)
    
    return dados
    
    
#Obter o registro de todas as aves
@app.get('/plantel/listar', tags=[plantel_tag],
         responses={"200": PlantelListSchema, "404": ErrorSchema})
def get_aves():
    """Exibe todas as aves cadastradas no banco de dados.

    Retorna todas o registro de todas as aves.
    """
    dados = add.select_all()
            
    return dados

#Buscar ave por anilha
@app.get('/plantel/localizar', tags=[plantel_tag],
            responses={"200": PlantelViewSchema, "404": ErrorSchema})
def buscar(query: PlantelBuscaSchema):
    """Localiza uma ave a partir do número da anilha.

    Retorna uma mensagem com os dados da ave.
    """
    nr_anilha = unquote(unquote(query.anilha))
    dados = add.select_anilha(nr_anilha)
    
    return dados
    
#Apagar o registro de uma ave através da anilha
@app.delete('/plantel/deletar', tags=[plantel_tag],
            responses={"200": PlantelDelSchema, "404": ErrorSchema})
def apagar(query: PlantelBuscaSchema):
    """Apaga o registro de uma ave a partir do número da anilha.

    Retorna uma mensagem da ave que foi atualizada.
    """
    nr_anilha = unquote(unquote(query.anilha))
    dados = add.deletar(nr_anilha)
    
    return dados


#Atualiza o registro de uma ave através da anilha
@app.put('/plantel/atualizar', tags=[plantel_tag],
            responses={"200": PlantelDelSchema, "404": ErrorSchema})
def atualizar(query: PlantelUpdateSchema):
    """Atualiza os dados de uma ave a partir do número da anilha.

    Retorna uma mensagem da ave atualizada.
    """
    anilha = unquote(unquote(query.anilha))
    especie = unquote(unquote(query.especie))
    mutacao = unquote(unquote(query.mutacao))
    sexo = unquote(unquote(query.sexo))
    data_nascimento = unquote(unquote(query.data_nascimento))
            
    dados = add.update(anilha, especie, mutacao, sexo, data_nascimento)
    
    return dados



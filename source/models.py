from sqlalchemy import String, Integer, Float, Column
from sqlalchemy.orm import relationship
from .database import Base

class InfoEmpresa(Base):
    __tablename__:str = "info_empresa"

    cnpj = Column(String)
    cnpj_basico = Column(String)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    natureza_juridica = Column(String)
    capital_social = Column(Float)
    porte_empresa = Column(String)
    quantidade_socios = Column(Integer)
    cnae = Column(Integer)
    tipo_logradouro = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cep = Column(String)
    uf = Column(String)
    municipio = Column(String)
    ddd1 = Column(String)
    telefone1 = Column(String)
    ddd2 = Column(String)
    telefone2 = Column(String)
    emai = Column(String)
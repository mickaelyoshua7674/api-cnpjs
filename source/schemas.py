from pydantic import BaseModel

class InfoEmpresaBase(BaseModel):
    title:str
    description:str

class InfoEmpresa(InfoEmpresaBase):

    cnpj:str
    cnpj_basico:str
    razao_social:str
    nome_fantasia:str
    natureza_juridica:str
    capital_social:float
    porte_empresa:str
    quantidade_socios:int
    cnae:int
    tipo_logradouro:str
    logradouro:str
    numero:str
    complemento:str
    bairro:str
    cep:str
    uf:str
    municipio:str
    ddd1:str
    telefone1:str
    ddd2:str
    telefone2:str
    emai:str

    class Config:
        orm_mode:bool = True
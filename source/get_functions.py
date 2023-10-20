from sqlalchemy.orm import Session
from models import InfoEmpresa

def get_company_by_cnpj(db:Session, cnpj:str):
    return db.query(InfoEmpresa).filter(InfoEmpresa.cnpj == cnpj)

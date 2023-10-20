from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from get_functions import get_company_by_cnpj

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("")
@app.get("/")
async def home():
    return "Home"

@app.get("/{cnpj}")
async def home(cnpj:str, db:Session = Depends(get_db())):
    result = get_company_by_cnpj(db, cnpj)
    if result is None:
        raise HTTPException(status_code=404, detail="CNPJ não encontrado")
    print(result)
    return result

if __name__ == "__main__":
    from uvicorn import run
    run(app="main:app", reload=True)
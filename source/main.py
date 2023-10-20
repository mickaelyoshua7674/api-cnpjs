from fastapi import FastAPI

app = FastAPI()

@app.get("")
@app.get("/")
async def home():
    return "Home"

if __name__ == "__main__":
    from uvicorn import run
    run(app="main:app", reload=True)
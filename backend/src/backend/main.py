from fastapi import FastAPI

app = FastAPI(title="Real Estate Platform API")


@app.get("/")
def obtener_estado():
    return {
        "estado": "ok",
        "mensaje": "La API de la plataforma inmobiliaria está funcionando",
    }

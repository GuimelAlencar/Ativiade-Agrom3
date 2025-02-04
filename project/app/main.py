from fastapi import FastAPI
from app.database import engine
from app import models, endpoints

# Criar todas as tabelas do banco de dados
models.Base.metadata.create_all(bind=engine)

# Instanciar a aplicação FastAPI
app = FastAPI(
    title="Minha API",
    description="Uma API REST construída com FastAPI, SQLAlchemy e PostgreSQL",
)

# Incluir rotas da aplicação
app.include_router(endpoints.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
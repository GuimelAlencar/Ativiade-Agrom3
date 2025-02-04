from pydantic import BaseModel

# Esquema base para leitura e criação de itens
class ItemBase(BaseModel):
    name: str
    last_name: str
    college_course: str

# Esquema para criação de itens (não inclui ID, pois é gerado automaticamente)
class ItemCreate(ItemBase):
    pass

# Esquema para leitura de itens (inclui ID)
class ItemRead(ItemBase):
    id: int

    class Config:
        orm_mode = True

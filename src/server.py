from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infra.sqlachemy.config.database import create_db
from src.routers import router_products, router_users

create_db()

app = FastAPI(    
    title="OLX FastAPI",
    description="API de aprendizagem estilo OLX  🚀",
    version="0.0.1",
    contact={
        "name": "Matheus Rodrigues Santos",
        "url": "http://github.com/santos95mat",
        "email": "santos95mat@gmail.com",
    },
)

origins = ['http://localhost:8000']

app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router_products.router, tags=['products'])
app.include_router(router_users.router, tags=['Users'])
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from infrastructure.database.db import db
from infrastructure.views.main import user_route

app = FastAPI(
    title='OpenAPI web app for payment initiations from CRM'
)


@app.on_event('startup')
async def startup():
    print('hello')
    # await db.connect()


@app.on_event('shutdown')
async def shutdown():
    print('buy')
    # await db.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_route)

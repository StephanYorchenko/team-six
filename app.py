from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.database.db import db
from infrastructure.views.other import other_routes

tags_metadata = [
    {'name': 'OpenAPI', 'description': 'System <–> ППУ'},
    {'name': 'Main', 'description': 'СППУ <–> System'},
    {'name': 'Other', 'description': 'Something else'},
]

app = FastAPI(
    title='OpenAPI web app for payment initiations from CRM',
    openapi_tags=tags_metadata,
)


@app.on_event('startup')
async def startup():
    print('hello')
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    print('buy')
    await db.disconnect()


# middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# routes

api = APIRouter(prefix='/api')
api.include_router(other_routes)

app.include_router(api)

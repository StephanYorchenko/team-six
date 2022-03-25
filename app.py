from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.database.db import db
from infrastructure.views.authorization import authorization_routes
from infrastructure.views.payments import payment_routes

tags_metadata = [
    {'name': 'Authorization', 'description': 'System <–> OpenAPI <–> ППУ'},
    {'name': 'Payments', 'description': 'System <–> OpenAPI <–> ППУ'},
    {'name': 'Main', 'description': 'СППУ <–> System'},
]

app = FastAPI(
    title='Payment initiations',
    description='OpenAPI web app for payment initiations from CRM',
    docs_url='/swagger',
    openapi_tags=tags_metadata,
)


@app.get('/')
def index():
    return {'welcome_message': 'Hello from server!'}


# events

@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
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
api.include_router(payment_routes)
api.include_router(authorization_routes)

app.include_router(api)

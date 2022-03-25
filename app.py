from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.database.db import db
from infrastructure.views.partners import partner_routes
from infrastructure.views.openapi import openapi_routes
from infrastructure.views.payments import payment_routes

tags_metadata = [
    {'name': 'OpenAPI', 'description': 'System <–> OpenAPI <–> ППУ'},
    {'name': 'Payments', 'description': 'СППУ <–> System'},
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

app.include_router(payment_routes)
app.include_router(partner_routes)
app.include_router(openapi_routes)

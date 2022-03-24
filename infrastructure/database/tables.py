from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String, Boolean, DateTime, Table

from infrastructure.database.db import metadata

_crms_id = 'crms.id'

crms = Table(
    'crms',
    metadata,
    Column('id', String, primary_key=True),
)


access_tokens = Table(
    'access_tokens',
    metadata,
    Column('crms_id', ForeignKey(_crms_id, ondelete='CASCADE'), nullable=False),
    Column('access_token', String, nullable=True),
    Column('validate', Boolean, default=False),
)


hybrid_tokens = Table(
    'hybrid_tokens',
    metadata,
    Column('crms_id', ForeignKey(_crms_id, ondelete='CASCADE'), nullable=False),
    Column('access_token', String, nullable=True),
    Column('refresh_token', String, nullable=True),
)


payments = Table(
    'payments',
    metadata,
    Column('crms_id', ForeignKey(_crms_id, ondelete='CASCADE'), nullable=False),
    Column('title', String(length=256), nullable=False),
    Column('description', String(length=2048), nullable=True),
    Column('amount', Integer, nullable=False),
    Column('reciever', String(length=256), nullable=False),
    Column('created_at', DateTime(timezone=True), nullable=False)
)


trash = Table(
    'spatial_ref_sys',
    metadata,
    Column('srid', Integer, autoincrement=False, nullable=False),
    Column('auth_name', String(length=256), autoincrement=False, nullable=True),
    Column('auth_srid', Integer, autoincrement=False, nullable=True),
    Column('srtext', String(length=2048), autoincrement=False, nullable=True),
    Column('proj4text', String(length=2048), autoincrement=False, nullable=True),
    CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
)

# examples

# _room_id = "rooms.id"

# users_rooms = Table(
#     "users_rooms",
#     metadata,
#     Column("user_id", ForeignKey(_user_id, ondelete="CASCADE"), nullable=False),
#     Column("room_id", ForeignKey(_room_id, ondelete="CASCADE"), nullable=False),
# )

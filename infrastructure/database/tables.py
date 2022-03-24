from sqlalchemy import CheckConstraint, Column, PrimaryKeyConstraint, String, Boolean, Table, ForeignKey

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

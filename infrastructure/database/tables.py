from sqlalchemy import CheckConstraint, Column, Integer, PrimaryKeyConstraint, String, Table

from infrastructure.database.db import metadata

_user_id = 'users.id'

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('login', String, unique=True, nullable=False),
    Column('first_name', String, default=''),
    Column('second_name', String, default=''),
    Column('last_name', String, default=''),
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

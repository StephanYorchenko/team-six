from sqlalchemy import Column, Integer, String, Table

from infrastructure.database.db import metadata

_user_id = 'users.id'
# _room_id = "rooms.id"

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('login', String, unique=True, nullable=False),
    Column('first_name', String, default=''),
    Column('second_name', String, default=''),
    Column('last_name', String, default=''),
)

# users_rooms = Table(
#     "users_rooms",
#     metadata,
#     Column("user_id", ForeignKey(_user_id, ondelete="CASCADE"), nullable=False),
#     Column("room_id", ForeignKey(_room_id, ondelete="CASCADE"), nullable=False),
# )

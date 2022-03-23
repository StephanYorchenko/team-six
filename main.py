from typing import List

import uvicorn
from fastapi import Depends

from app import app
from auth import get_user_from_token
from dependencies import get_user_repository, get_rooms_repo
from schema import RoomDTO


@app.get("/api/rooms", response_model=List[RoomDTO])
async def get_rooms(
        user=Depends(get_user_from_token),
        rooms_repository=Depends(get_rooms_repo),
        repository=Depends(get_user_repository)
):
    user = repository.get_by_login(login=user)
    if not user:
        raise Exception()
    return await rooms_repository.get_all()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

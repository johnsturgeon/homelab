from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.services.auth import verify_token

from app.services.tidal import delete_songs_from_todo_playlist

router = APIRouter()
security = HTTPBearer()


@router.get("/delete_songs_from_todo")
async def delete_songs_from_todo(
    _: HTTPAuthorizationCredentials = Depends(verify_token),
):
    songs_deleted: int = await delete_songs_from_todo_playlist()
    return {"total_songs_deleted": songs_deleted}

"""Module for interacting with my TIDAL library"""

import asyncio
from typing import List

import tidalapi

from app.core.config import global_config


async def delete_songs_from_todo_playlist() -> int:
    todo_playlist = await get_todo_playlists()
    tracks_deleted: int = 0
    playlist_ids: List[int] = []
    for track in todo_playlist.tracks():
        playlist_ids.append(track.id)
    tracks_deleted += len(playlist_ids)
    for playlist_id in playlist_ids:
        todo_playlist.remove_by_id(str(playlist_id))
    return tracks_deleted


async def get_todo_playlists():
    await global_config.load_secrets()
    config = tidalapi.Config()
    session = tidalapi.Session(config)
    token_type = "Bearer"
    access_token = global_config.TIDAL_ACCESS_TOKEN
    refresh_token = global_config.TIDAL_REFRESH_TOKEN
    session.load_oauth_session(token_type, access_token, refresh_token)
    for playlist in session.user.playlists():
        if playlist.name == "TODO: Sync To Plex":
            return playlist
    return None


async def get_song_count_from_todo_playlist() -> int:
    todo_playlist = await get_todo_playlists()
    return len(todo_playlist.tracks())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_song_count_from_todo_playlist())

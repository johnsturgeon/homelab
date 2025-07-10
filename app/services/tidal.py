"""Module for interacting with my TIDAL library"""

import asyncio
from typing import List

import tidalapi

from app.core.config import global_config


async def delete_songs_from_todo_playlist() -> int:
    config = tidalapi.Config()
    session = tidalapi.Session(config)
    token_type = "Bearer"
    access_token = global_config.TIDAL_ACCESS_TOKEN
    refresh_token = global_config.TIDAL_REFRESH_TOKEN
    session.load_oauth_session(token_type, access_token, refresh_token)
    tracks_deleted: int = 0
    for playlist in session.user.playlists():
        if playlist.name == "TODO: Sync To Plex":
            playlist_ids: List[int] = []
            for track in playlist.tracks():
                playlist_ids.append(track.id)
            tracks_deleted += len(playlist_ids)
            for playlist_id in playlist_ids:
                playlist.remove_by_id(str(playlist_id))
    return tracks_deleted

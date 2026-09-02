"""
Módulo core do IPTV Player - Gerenciamento de playlists
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Channel:
    name: str
    url: str
    group: Optional[str] = None

    def __str__(self) -> str:
        if self.group:
            return f"{self.name} ({self.group})"
        return f"{self.name}"


class PlaylistManager:
    """Gerencia uma playlist M3U simples e uma lista de canais."""

    def __init__(self) -> None:
        # playlist raw content (str) or None
        self.playlist: Optional[str] = None
        # lista de canais (Channel)
        self.channels: List[Channel] = []
        # origem/URL da playlist
        self.url: Optional[str] = None

    def add_channel(self, channel: Channel) -> None:
        self.channels.append(channel)

    def clear(self) -> None:
        self.playlist = None
        self.channels = []
        self.url = None

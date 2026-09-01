"""Testes das playlists"""

import pytest
from src.core.playlist_manager import PlaylistManager, Channel


class TestPlaylistManager:
    """Testes do gerenciador de playlists"""
    
    def setup_method(self):
        """Setup de cada teste"""
        self.manager = PlaylistManager()
    
    def test_init(self):
        """Testa inicialização do gerenciador"""
        assert self.manager.playlist is None
        assert self.manager.channels == []
        assert self.manager.url is None
    
    def test_channel_creation(self):
        """Testa criação de um canal"""
        channel = Channel(
            name="Test Channel",
            url="http://example.com/stream"
        )
        assert channel.name == "Test Channel"
        assert channel.url == "http://example.com/stream"
    
    def test_channel_string(self):
        """Testa representação em string de um canal"""
        channel = Channel(
            name="Test",
            url="http://test.com",
            group="Movies"
        )
        assert "Test" in str(channel)
        assert "Movies" in str(channel)

"""
Gerenciador de configurações da aplicação IPTV Player
"""

import json
import os
from pathlib import Path
from typing import Optional, Dict, Any
from pydantic import BaseSettings, Field

from .constants import CONFIG_DIR, LOG_LEVEL, DEFAULT_QUALITY


class Settings(BaseSettings):
    """Configurações da aplicação"""
    
    # Aplicação
    app_name: str = "IPTV Player"
    app_version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    
    # Interface
    window_width: int = 1280
    window_height: int = 720
    window_x: int = 100
    window_y: int = 100
    theme: str = "dark"
    remember_position: bool = True
    fullscreen: bool = False
    
    # Streaming
    default_quality: str = DEFAULT_QUALITY
    buffer_size: int = 8192
    timeout: int = 30
    max_retries: int = 3
    retry_delay: int = 2
    
    # Playlist
    auto_refresh_playlist: bool = True
    playlist_refresh_interval: int = 3600
    last_playlist_url: Optional[str] = None
    
    # EPG
    enable_epg: bool = True
    epg_url: Optional[str] = None
    epg_refresh_interval: int = 86400
    
    # Cache
    enable_cache: bool = True
    cache_ttl: int = 3600
    max_cache_size: int = 500
    
    # Logging
    log_level: str = LOG_LEVEL
    log_file: Path = Path(CONFIG_DIR) / "iptv_player.log"
    
    # Rede
    proxy_enabled: bool = False
    proxy_url: Optional[str] = None
    user_agent: str = "IPTV Player/1.0.0"
    
    # Reprodução
    remember_last_channel: bool = True
    autoplay_on_start: bool = False
    loop_mode: str = "no-repeat"  # no-repeat, repeat-one, repeat-all
    
    class Config:
        env_file = CONFIG_DIR / ".env"
        env_file_encoding = "utf-8"
    
    @classmethod
    def from_file(cls, filepath: Path) -> "Settings":
        """Carrega configurações de um arquivo JSON"""
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return cls(**data)
        return cls()
    
    def save_to_file(self, filepath: Optional[Path] = None) -> None:
        """Salva configurações em um arquivo JSON"""
        if filepath is None:
            filepath = CONFIG_DIR / "settings.json"
        
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.dict(exclude_none=True), f, indent=4, default=str)
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte configurações para dicionário"""
        return self.dict(exclude_none=True)
    
    def update_from_dict(self, data: Dict[str, Any]) -> None:
        """Atualiza configurações a partir de um dicionário"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    @property
    def config_file_path(self) -> Path:
        """Retorna o caminho do arquivo de configuração"""
        return CONFIG_DIR / "settings.json"
    
    def __str__(self) -> str:
        return f"Settings({self.dict()})"


# Instância global de configurações
_settings = None


def get_settings() -> Settings:
    """Obtém a instância global de configurações"""
    global _settings
    if _settings is None:
        _settings = Settings.from_file(CONFIG_DIR / "settings.json")
    return _settings


def reload_settings() -> Settings:
    """Recarrega as configurações"""
    global _settings
    _settings = Settings.from_file(CONFIG_DIR / "settings.json")
    return _settings

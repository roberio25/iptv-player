"""Utilitários de validação (URLs e M3U)"""
from typing import Tuple
from urllib.parse import urlparse


def validate_url(url: str) -> Tuple[bool, str]:
    """Valida se a string passada é uma URL HTTP/HTTPS simples.

    Retorna uma tupla (is_valid: bool, message: str).
    """
    if not isinstance(url, str) or not url:
        return False, "URL vazia ou inválida"

    parsed = urlparse(url)
    if parsed.scheme in ("http", "https") and parsed.netloc:
        return True, ""

    return False, "URL inválida"


def validate_m3u(content: str) -> Tuple[bool, str]:
    """Valida se o conteúdo parece ser uma playlist M3U básica.

    Verifica se começa com #EXTM3U ou contém linhas #EXTINF.
    """
    if not isinstance(content, str) or not content.strip():
        return False, "Conteúdo vazio"

    s = content.strip()
    if s.startswith("#EXTM3U") or "#EXTINF" in s:
        return True, ""

    return False, "Conteúdo não parece ser M3U"

"""Utilitários de rede leves usados nos testes (validação de URL)."""
from urllib.parse import urlparse


def is_url_valid(url: str) -> bool:
    """Verifica de forma simples se a URL tem esquema http/https e netloc."""
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False

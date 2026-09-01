"""Testes dos utilitários"""

import pytest
from src.utils.validators import validate_url, validate_m3u
from src.utils.network import is_url_valid


class TestValidators:
    """Testes dos validadores"""
    
    def test_validate_url_valid(self):
        """Testa validação de URL válida"""
        is_valid, msg = validate_url("http://example.com")
        assert is_valid is True
    
    def test_validate_url_invalid(self):
        """Testa validação de URL inválida"""
        is_valid, msg = validate_url("not-a-url")
        assert is_valid is False
    
    def test_validate_m3u_valid(self):
        """Testa validação de M3U válido"""
        content = "#EXTM3U\n#EXTINF:-1,Canal 1\nhttp://example.com/stream"
        is_valid, msg = validate_m3u(content)
        assert is_valid is True
    
    def test_validate_m3u_invalid(self):
        """Testa validação de M3U inválido"""
        content = "Invalid content"
        is_valid, msg = validate_m3u(content)
        assert is_valid is False


class TestNetwork:
    """Testes de funcionalidades de rede"""
    
    def test_is_url_valid_http(self):
        """Testa validação de URL HTTP"""
        assert is_url_valid("http://example.com") is True
    
    def test_is_url_valid_https(self):
        """Testa validação de URL HTTPS"""
        assert is_url_valid("https://example.com") is True
    
    def test_is_url_valid_invalid(self):
        """Testa validação de URL inválida"""
        assert is_url_valid("not-a-url") is False

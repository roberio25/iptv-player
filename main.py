#!/usr/bin/env python3
"""
IPTV Player - Entry Point
Aplicação principal para o player IPTV
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.logger_setup import setup_logger
from src.config.settings import Settings

logger = setup_logger(__name__)


def main():
    """Função principal da aplicação"""
    try:
        logger.info("Iniciando IPTV Player...")
        
        # Carrega configurações
        settings = Settings()
        logger.debug(f"Configurações carregadas: {settings}")
        
        # Import da UI após configurações
        from PyQt6.QtWidgets import QApplication
        from src.ui.main_window import MainWindow
        
        # Cria aplicação PyQt6
        app = QApplication(sys.argv)
        
        # Cria janela principal
        logger.info("Criando interface gráfica...")
        window = MainWindow(settings)
        window.show()
        
        logger.info("IPTV Player iniciado com sucesso!")
        sys.exit(app.exec())
        
    except Exception as e:
        logger.error(f"Erro ao iniciar a aplicação: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

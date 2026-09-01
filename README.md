# IPTV Player 📺

Um player e gerenciador profissional de IPTV com suporte a listas M3U, streaming de canais de TV e EPG (Guia Eletrônico de Programação).

## 🌟 Funcionalidades

- ✅ Suporte para listas M3U
- ✅ Reprodução de streams IPTV
- ✅ Gerenciador de canais e playlists
- ✅ Interface gráfica intuitiva
- ✅ Suporte a EPG (Guia Eletrônico de Programação)
- ✅ Histórico de visualização
- ✅ Favoritos personalizados
- ✅ Configurações de qualidade de streaming
- ✅ Cache inteligente
- ✅ Multiplataforma (Windows, macOS, Linux)

## 📋 Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- ffmpeg (para processamento de streams)

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/roberio25/iptv-player.git
cd iptv-player
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o aplicativo

```bash
python main.py
```

## 📁 Estrutura do Projeto

```
iptv-player/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Arquivo principal
│   ├── core/
│   │   ├── __init__.py
│   │   ├── playlist_manager.py # Gerenciamento de playlists
│   │   ├── stream_player.py    # Player de streams
│   │   ├── epg_handler.py      # Gerenciador de EPG
│   │   └── cache_manager.py    # Gerenciamento de cache
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py      # Janela principal
│   │   ├── widgets.py          # Componentes UI
│   │   └── styles.py           # Estilos CSS
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── network.py          # Utilitários de rede
│   │   ├── parsers.py          # Parsers M3U/EPG
│   │   ├── validators.py       # Validações
│   │   └── logger.py           # Sistema de logs
│   └── config/
│       ├── __init__.py
│       ├── settings.py         # Configurações da aplicação
│       └── constants.py        # Constantes do projeto
├── tests/
│   ├── __init__.py
│   ├── test_playlist.py
│   ├── test_stream.py
│   └── test_utils.py
├── resources/
│   ├── icons/
│   ├── themes/
│   └── templates/
├── docs/
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   ├── API.md
│   └── ARCHITECTURE.md
├── requirements.txt
├── setup.py
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD Pipeline
├── Dockerfile
├── docker-compose.yml
├── LICENSE
└── main.py                     # Entry point
```

## 🛠️ Desenvolvimento

### Configurar ambiente de desenvolvimento

```bash
pip install -r requirements-dev.txt
```

### Executar testes

```bash
pytest tests/
```

### Gerar cobertura de testes

```bash
pytest --cov=src tests/
```

### Linting e Formatação

```bash
flake8 src/
black src/
isort src/
```

## 📖 Documentação

Veja a pasta `docs/` para documentação completa:

- [Guia de Instalação](docs/INSTALLATION.md)
- [Guia de Uso](docs/USAGE.md)
- [Documentação da API](docs/API.md)
- [Arquitetura do Projeto](docs/ARCHITECTURE.md)

## 🐳 Docker

Para executar com Docker:

```bash
docker-compose up
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

- **Roberto** - [@roberio25](https://github.com/roberio25)

## 📞 Suporte

Se você tiver dúvidas ou encontrar problemas, abra uma [issue](https://github.com/roberio25/iptv-player/issues) no GitHub.

## 🗺️ Roadmap

- [ ] Interface web (usando Flask/Django)
- [ ] Aplicativo mobile (iOS/Android)
- [ ] Suporte a DVR (gravação de programas)
- [ ] Integração com sistemas de recomendação
- [ ] Suporte a plugins
- [ ] API REST completa
- [ ] Sistema de autenticação avançado

---

**Desenvolvido com ❤️ por Roberto**

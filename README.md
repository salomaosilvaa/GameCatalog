# LastPlayed - Sistema de Gerenciamento de Catálogos Pessoais de Jogos Digitais
O LastPlayed é um sistema de linha de comando (CLI) desenvolvido em Python para gerenciamento de catálogos pessoais de jogos digitais.
O projeto tem como foco a aplicação prática de conceitos de Programação Orientada a Objetos (POO), como encapsulamento, herança, composição, validações de domínio e persistência de dados.
## Objetivo do Sistema
O LastPlayed permite que usuários: cadastrem jogos com informações detalhadas, acompanhem progresso (horas jogadas, status e avaliações), organizem jogos por filtros e ordenações, gerem relatórios consolidados (top 5, médias e percentuais), persistam dados localmente em arquivos JSON e utilizem o sistema de forma interativa via terminal.
## Conceitos Aplicados
- Programação Orientada a Objetos (POO)
- Encapsulamento e validação de regras de negócio
- Herança (jogos por plataforma)
- Serialização e persistência em JSON
- Separação de responsabilidades (domínio, dados e interface)
- Testes automatizados com pytest
- Estrutura modular e extensível
## Requisitos do Sistema
- Python 3.10 ou superior
- Windows, Linux ou MacOS
- Terminal
### Dependências
- pytest (as outras bibliotecas são nativas do Python)
## Estrutura do Projeto:
```text
LastPlayed/
│
├── README.md
├── requirements.txt
├── main.py
├── .gitignore
├── pytest.ini
│
├── source/
│   ├── __init.py__
│   ├── dominio/
│   │   ├── __init.py__
│   │   ├── jogo.py
│   │   ├── jogo_pc.py
│   │   ├── jogo_console.py
│   │   ├── jogo_mobile.py
│   │   ├── colecao.py
│   │   └── usuario.py
│   │
│   ├── dados/
│   │   ├── __init.py__
│   │   ├── jogos.json
│   │   ├── usuario.json
│   │   ├── repositorio_json.py
│   │   ├── relatorios.py
│   │   └── settings.py
│   │
│   └── utils/
│       └── cores.py
└── tests/
    ├── test_colecao.py
    ├── test_filtros.py
    ├── test_jogo.py
    ├── test_ordenacao.py
    ├── test_persist.py
    ├── test.relatorios.py
    └── __pycache__
```
## UML
<img width="1811" height="3138" alt="Untitled diagram-2025-11-18-052909" src="https://github.com/user-attachments/assets/7738928b-4260-4c70-b6bd-1625955d326f" />

# LastPlayed - Sistema de Gerenciamento de Catálogos Pessoais de Jogos Digitais
Trata-se de um projeto de CLI (Command-Line Interface) cujo intuito é gerenciar um catálogo pessoal de jogos digitais. O foco é utilizar recursos e conceitos da Programação Orientada a Objetos (POO), como herança e encapsulamento, a fim de  cumprir os requisitos do sistema.
## Objetivo do Sistema
O LastPlayed permite que seus usuários cadastrem jogos com informações detalhadas, controlem seu progresso in-game, filtrem e organizem jogos, criem coleções personalizadas e gerem relatórios contendo informações relevantes. 
## Estrutura do Projeto:
projeto_LastPlayed/

│

├── README.md

├── requirements.txt

├── main.py

│

├── src/

│   ├── dominio/

│   │   ├── jogo.py

│   │   ├── jogo_pc.py

│   │   ├── jogo_console.py

│   │   ├── jogo_mobile.py

│   │   ├── colecao.py

│   │   └── usuario.py   (opcional)

│   │

│   ├── dados/

│        ├── repositorio_json.py

│        ├── relatorios.py

│        └── settings.py

│ 
└── tests/

    └── test_exemplo.py

## UML
<img width="1811" height="3138" alt="Untitled diagram-2025-11-18-052909" src="https://github.com/user-attachments/assets/7738928b-4260-4c70-b6bd-1625955d326f" />

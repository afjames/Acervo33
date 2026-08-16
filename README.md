# Acervo33 - Sistema de Gestão de Acervo Musical

O **Acervo33** é uma aplicação web desenvolvida para catalogar e gerenciar acervos musicais (vinis, CDs e fitas K7), permitindo a organização estruturada de artistas, obras, faixas e mídias físicas.

## 🚀 Tecnologias Utilizadas
* **Backend:** Python 3, Flask, Flask-SQLAlchemy, PyMySQL, python-dotenv
* **Banco de Dados:** MySQL (Abordagem Database-First, Charset `utf8mb4`, Collation `utf8mb4_unicode_ci`)
* **Ambiente:** Ubuntu Linux, Virtual Environment (`venv`)

## 🏗️ Arquitetura e Modelagem de Dados
O projeto adota o padrão **MVC (Model-View-Controller)** com um banco de dados relacional projetado em **Terceira Forma Normal (3FN)**.

### Estrutura do Banco de Dados (`acervo33_db`)
1. **`artistas`**: Mapeia os criadores das obras.
   * `id` (PK, AUTO_INCREMENT), `nome` (VARCHAR 100, NOT NULL).
2. **`albuns`**: Registra as obras musicais.
   * `id` (PK), `titulo` (VARCHAR 100, NN), `ano_lancamento` (SMALLINT, NN), `genero` (VARCHAR 50, NN), `duracao_album` (TIME, NN), `nota` (TINYINT, CHECK 0-10), `capa_url` (VARCHAR 255), `produtor` (VARCHAR 100), `artista_id` (FK -> `artistas.id`).
3. **`musicas`**: Detalha as faixas pertencentes a cada álbum.
   * `id` (PK), `titulo` (VARCHAR 100, NN), `faixa_numero` (TINYINT, NN), `favorita` (BOOLEAN), `album_id` (FK -> `albuns.id`).
4. **`midia_fisica`**: Gerencia os itens físicos existentes no catálogo.
   * `id` (PK), `formato` (VARCHAR 20, NN, CHECK IN('Vinil', 'CD', 'FitaK7')), `estado_conservacao` (VARCHAR 50), `album_id` (FK -> `albuns.id`).

## 📁 Estrutura do Projeto
```text
acervo33/
├── app/
│   ├── models/
│   ├── routes/
│   └── templates/
├── .env
├── .gitignore
├── README.md
├── SECURITY.md
└── run.py
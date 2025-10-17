# Integração Trello → Asana

Este projeto realiza a sincronização automática entre **quadros do Trello** e **projetos do Asana**, transformando **listas em seções** e **cards em tarefas**, de forma automatizada.

---

## Funcionalidades

- Conexão com Trello e Asana via API
- Sincronização de listas e cards de forma automática
- Processamento de múltiplos itens usando **loops**
- Configuração simples através de variáveis de ambiente

---

## Como usar

### 1. Clonar o repositório

git clone https://github.com/wesley220v1-creator/project_api_integration.git
cd project_api_integration

### 2. Criar ambiente virtual (opcional)

python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` com as credenciais:

TRELLO_KEY=your_trello_key
TRELLO_TOKEN=your_trello_token
TRELLO_BOARD_ID=your_board_id
ASANA_TOKEN=your_asana_token
ASANA_PROJECT_ID=your_project_id

### 5. Executar a aplicação

python main.py

O script irá:

1. Listar todas as listas do quadro Trello
2. Criar seções correspondentes no projeto Asana
3. Percorrer cada card do Trello e criar tarefas equivalentes no Asana
4. Registrar logs de sucesso, erros e avisos no console ou arquivo

---

## Estrutura do projeto

projeto/
├─ main.py             # Script principal de sincronização
├─ trello_client.py    # Conexão e manipulação de Trello
├─ asana_client.py     # Conexão e manipulação de Asana
├─ utils.py            # Funções auxiliares e tratamento de dados
├─ requirements.txt    # Dependências
└─ .env.example        # Exemplo de variáveis de ambiente

---

## Observações

Espero que gostem (:

from dotenv import load_dotenv
import os

# Carrega as informações do arquivo .env
load_dotenv()

class Settings:
    BASE_TRELLO_KEY = os.getenv("BASE_TRELLO_KEY")
    BASE_TRELLO_TOKEN = os.getenv("BASE_TRELLO_TOKEN")
    BASE_TRELLO_BOARD_ID = os.getenv("BASE_TRELLO_BOARD_ID")

    BASE_ASANA_PAT = os.getenv("BASE_ASANA_PAT")
    BASE_ASANA_PROJECT_ID = os.getenv("BASE_ASANA_PROJECT_ID")

    POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", "60"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# Instância global
settings = Settings()

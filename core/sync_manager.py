import logging
from typing import Dict
from .trello_client import get_lists, get_cards
from .asana_client import find_project_sections, create_section, create_task

logger = logging.getLogger(__name__)

class SyncManager:
    def __init__(self, BASE_TRELLO_BOARD_ID: str, BASE_ASANA_PROJECT_ID: str):
        self.BASE_TRELLO_BOARD_ID = BASE_TRELLO_BOARD_ID
        self.BASE_ASANA_PROJECT_ID = BASE_ASANA_PROJECT_ID
        # Mapeamento trello_list_id -> asana_section_gid
        self.list_to_section: Dict[str, str] = {}


    def ensure_sections(self):
        """Garante que exista uma seção Asana por lista Trello e popula list_to_section."""
        trello_lists = get_lists(self.BASE_TRELLO_BOARD_ID)
        asana_sections = find_project_sections(self.BASE_ASANA_PROJECT_ID)
        # criar um mapeamento por nome (simplificação)
        name_to_section = {s.name: s for s in asana_sections}

        for tl in trello_lists:
            if tl.name in name_to_section:
                self.list_to_section[tl.id] = name_to_section[tl.name].id
            else:
                sec = create_section(self.BASE_ASANA_PROJECT_ID, tl.name)
                self.list_to_section[tl.id] = sec.id
                logger.info("Created section '%s' for Trello list %s", tl.name, tl.id)


    def sync_once(self):
        """Sincroniza cartões Trello para tarefas Asana (criação simples)."""
        self.ensure_sections()
        for trello_list_id, asana_section_gid in self.list_to_section.items():
            cards = get_cards(trello_list_id)
            for c in cards:
                # Cria tarefa para cada cartão com nome igual ao cartão
                # Verifica se já existe (por nome ou campo customizado)
                create_task(self.BASE_ASANA_PROJECT_ID, c.name, c.desc, section_gid=asana_section_gid)
                logger.info("Created task for card %s -> %s", c.id, c.name)
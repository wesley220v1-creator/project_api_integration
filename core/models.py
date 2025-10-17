from dataclasses import dataclass

# Classes de abstração para Trello e Asana, representando listas, cards, seções e tarefas

@dataclass
class TrelloList:
    id: str
    name: str


@dataclass
class TrelloCard:
    id: str
    name: str
    desc: str
    idList: str




@dataclass
class AsanaSection:
    id: str
    name: str


@dataclass
class AsanaTask:
    id: str
    name: str
    notes: str
    projects: list
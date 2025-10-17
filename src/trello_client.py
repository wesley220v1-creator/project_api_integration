import requests
from typing import List
from .config import settings
from .models import TrelloList, TrelloCard
from .exceptions import TrelloError
from tenacity import retry, stop_after_attempt, wait_exponential


BASE = "https://api.trello.com/1"


def _auth_params():
    return {"key": settings.BASE_TRELLO_KEY, "token": settings.BASE_TRELLO_TOKEN}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def get_lists(board_id: str) -> List[TrelloList]:
    url = f"{BASE}/boards/{board_id}/lists"
    resp = requests.get(url, params=_auth_params())
    if resp.status_code != 200:
        raise TrelloError(f"Error getting lists: {resp.status_code} {resp.text}")
    data = resp.json()
    return [TrelloList(id=item["id"], name=item["name"]) for item in data]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def get_cards(list_id: str) -> List[TrelloCard]:
    url = f"{BASE}/lists/{list_id}/cards"
    resp = requests.get(url, params=_auth_params())
    if resp.status_code != 200:
        raise TrelloError(f"Error getting cards: {resp.status_code} {resp.text}")
    data = resp.json()
    return [TrelloCard(id=item["id"], name=item.get("name",""), desc=item.get("desc",""), idList=item.get("idList")) for item in data]
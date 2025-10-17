import requests
from typing import Optional, List
from .config import settings
from .exceptions import AsanaError
from .models import AsanaSection, AsanaTask
from tenacity import retry, stop_after_attempt, wait_exponential


BASE = "https://app.asana.com/api/1.0"


def _headers():
    return {
    "Authorization": f"Bearer {settings.BASE_ASANA_PAT}",
    "Content-Type": "application/json",
    }


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def find_project_sections(project_id: str) -> List[AsanaSection]:
    url = f"{BASE}/projects/{project_id}/sections"
    resp = requests.get(url, headers=_headers())
    if resp.status_code != 200:
        raise AsanaError(f"Error fetching sections: {resp.status_code} {resp.text}")
    data = resp.json().get("data", [])
    return [AsanaSection(id=item["gid"], name=item["name"]) for item in data]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def create_section(project_id: str, name: str) -> AsanaSection:
    url = f"{BASE}/projects/{project_id}/sections"
    payload = {"data": {"name": name}}
    resp = requests.post(url, headers=_headers(), json=payload)
    if resp.status_code not in (200, 201):
        raise AsanaError(f"Error creating section: {resp.status_code} {resp.text}")
    d = resp.json()["data"]
    return AsanaSection(id=d["gid"], name=d["name"])


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def create_task(project_id: str, name: str, notes: Optional[str], section_gid: Optional[str]=None) -> AsanaTask:
    url = f"{BASE}/tasks"
    data = {"name": name, "notes": notes or "", "projects": [project_id]}
    resp = requests.post(url, headers=_headers(), json={"data": data})
    if resp.status_code not in (200, 201):
        raise AsanaError(f"Error creating task: {resp.status_code} {resp.text}")
    task = resp.json()["data"]
    
    if section_gid:
        _add_task_to_section(section_gid, task["gid"])
    return AsanaTask(id=task["gid"], name=task.get("name",""), notes=task.get("notes",""), projects=task.get("projects", []))


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def _add_task_to_section(section_gid: str, task_gid: str):
    url = f"{BASE}/sections/{section_gid}/addTask"
    resp = requests.post(url, headers=_headers(), json={"data": {"task": task_gid}})
    if resp.status_code not in (200, 201):
        raise AsanaError(f"Error adding task to section: {resp.status_code} {resp.text}")
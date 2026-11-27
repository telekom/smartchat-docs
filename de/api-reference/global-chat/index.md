# Global Chat

Source: https://docs.smartchat.ai.t-systems.net/de/api-reference/global-chat/

> Schritt-für-Schritt-Anleitung zum Erstellen einer Smartchat-Sitzung und Abfragen der gemeinsamen globalen Wissensbasis via RAG API.

# Global Chat

Diese Anleitung zeigt, wie Sie eine Chat-Sitzung mit der gemeinsamen globalen Wissensbasis erstellen — ohne Datei-Uploads.

## [Voraussetzungen](https://docs.smartchat.ai.t-systems.net/de/api-reference/global-chat/#voraussetzungen)

- **Zugangsdaten** fuer eine gehostete Smartchat RAG API mit der Rolle `CHAT_USER`
- Ein **vorkonfigurierter** Smartchat RAG API-Server

## [1. Authentifizieren](https://docs.smartchat.ai.t-systems.net/de/api-reference/global-chat/#1-authentifizieren)

```python
import requests
import json


base_url = "<BASE_URL>"


payload = json.dumps({"username": "<USERNAME>", "password": "<PASSWORD>"})
headers = {"Content-Type": "application/json"}


response = requests.post(f"{base_url}/api/v1/auth/user", headers=headers, data=payload)
headers["Authorization"] = f"Bearer {response.json()['access_token']}"
```

## [2. Standard-Chat-Konfiguration abrufen](https://docs.smartchat.ai.t-systems.net/de/api-reference/global-chat/#2-standard-chat-konfiguration-abrufen)

```python
response = requests.get(f"{base_url}/config-manager/api/v1/user/configs", headers=headers)


configs = response.json()
default_config = [c for c in configs if c["userGroupId"] == "default"][0]


default_local_config_id = default_config["localKbConfigs"][0]["id"]
allowed_llms = default_config["localKbConfigs"][0]["allowed_llms"]
```

## [3. Globale Chat-Sitzung erstellen](https://docs.smartchat.ai.t-systems.net/de/api-reference/global-chat/#3-globale-chat-sitzung-erstellen)

```python
body = {
    "title": "Testing the Smartchat RAG API",
    "config": {
        "localConfigId": default_local_config_id,
        "globalContext": True,
        "chatModel": allowed_llms[0]["name"],
    },
}
response = requests.post(f"{base_url}/chat-session-manager/api/v1/sessions/", headers=headers, json=body)
session_id = response.json()["sessionId"]
```

## [4. Chatten](https://docs.smartchat.ai.t-systems.net/de/api-reference/global-chat/#4-chatten)

```python
body = {
    "sessionId": session_id,
    "userPrompt": "Can you summarize the context to me?",
}
response = requests.post(f"{base_url}/query-pipelines/api/v1/chat", headers=headers, json=body)
print(response.json())
```

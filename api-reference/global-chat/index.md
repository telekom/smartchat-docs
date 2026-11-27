# Global KB Guide

Source: https://docs.smartchat.ai.t-systems.net/api-reference/global-chat/

> Step-by-step guide to creating a Smartchat session and querying the shared global knowledge base via the RAG API.

# Chat with the Global Knowledge Base

This guide shows how to create a chat session using the shared global knowledge base — no file uploads needed.

## [Prerequisites](https://docs.smartchat.ai.t-systems.net/api-reference/global-chat/#prerequisites)

- **Credentials** for a hosted Smartchat RAG API with a `CHAT_USER` role
- A **pre-configured** Smartchat RAG API server

## [1. Authenticate](https://docs.smartchat.ai.t-systems.net/api-reference/global-chat/#1-authenticate)

```python
import requests
import json


base_url = "<BASE_URL>"


payload = json.dumps({"username": "<USERNAME>", "password": "<PASSWORD>"})
headers = {"Content-Type": "application/json"}


response = requests.post(f"{base_url}/api/v1/auth/user", headers=headers, data=payload)
headers["Authorization"] = f"Bearer {response.json()['access_token']}"
```

## [2. Get Default Chat Configuration](https://docs.smartchat.ai.t-systems.net/api-reference/global-chat/#2-get-default-chat-configuration)

```python
response = requests.get(f"{base_url}/config-manager/api/v1/user/configs", headers=headers)


configs = response.json()
default_config = [c for c in configs if c["userGroupId"] == "default"][0]


default_local_config_id = default_config["localKbConfigs"][0]["id"]
allowed_llms = default_config["localKbConfigs"][0]["allowed_llms"]
```

## [3. Create a Global Chat Session](https://docs.smartchat.ai.t-systems.net/api-reference/global-chat/#3-create-a-global-chat-session)

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

## [4. Chat](https://docs.smartchat.ai.t-systems.net/api-reference/global-chat/#4-chat)

```python
body = {
    "sessionId": session_id,
    "userPrompt": "Can you summarize the context to me?",
}
response = requests.post(f"{base_url}/query-pipelines/api/v1/chat", headers=headers, json=body)
print(response.json())
```

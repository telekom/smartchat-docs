# RAG API Reference

Source: https://docs.smartchat.ai.t-systems.net/api-reference/rag-api/

> HTTP reference for the Smartchat RAG API gateway — covers authentication, service routing, and all available API operations.

Interact with the Smartchat RAG API via HTTP requests. The API is accessed through a gateway with multiple backend services.

## [Base URL & Routing](https://docs.smartchat.ai.t-systems.net/api-reference/rag-api/#base-url--routing)

Requests follow the format: `<base_url>/<service_path>/<route>`

**Example:** `https://api-gateway.ai.t-systems.net/config-manager/redoc`

| Part | Value |
| - | - |
| Base URL | `https://api-gateway.ai.t-systems.net` |
| Service path | `config-manager` |
| Route | `redoc` |

## [Authentication](https://docs.smartchat.ai.t-systems.net/api-reference/rag-api/#authentication)

Obtain a Bearer Token from the [authentication endpoint](https://api-gateway.ai.t-systems.net/redoc#tag/Auth/operation/get_user_token_api_v1_auth_user_post), then include the `access_token` in all subsequent requests.

**curl**

```bash
# Authenticate
curl --location '<BASE_URL>/api/v1/auth/user' \
  --header 'Content-Type: application/json' \
  --data '{
    "username": "<USERNAME>",
    "password": "<PASSWORD>"
  }'


# Use the token
curl --location '<BASE_URL>/chat-session-manager/api/v1/sessions/' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>'
```

**Python**

```python
import requests
import json


base_url = "<BASE_URL>"


# Authenticate
payload = json.dumps({"username": "<USERNAME>", "password": "<PASSWORD>"})
headers = {"Content-Type": "application/json"}
response = requests.post(f"{base_url}/api/v1/auth/user", headers=headers, data=payload)


# Add token to headers
headers["Authorization"] = f"Bearer {response.json()['access_token']}"


# Make authenticated requests
response = requests.get(f"{base_url}/chat-session-manager/api/v1/sessions/", headers=headers)
print(response.json())
```

## [Services](https://docs.smartchat.ai.t-systems.net/api-reference/rag-api/#services)

| Service | Path | Docs | Description |
| - | - | - | - |
| **API Gateway** | — | [link](https://api-gateway.ai.t-systems.net/redoc) | Authentication and entrypoint |
| **Config Manager** | `config-manager` | [link](https://api-gateway.ai.t-systems.net/config-manager/redoc) | Tenant and RAG configurations |
| **User Manager** | `user-manager` | [link](https://api-gateway.ai.t-systems.net/user-manager/redoc) | Users, roles, and groups |
| **File Manager** | `file-manager` | [link](https://api-gateway.ai.t-systems.net/file-manager/redoc) | Files, file groups, knowledge bases |
| **Ingest Master** | `ingest-master` | [link](https://api-gateway.ai.t-systems.net/ingest-master/redoc) | File ingestion orchestration |
| **Chat Session Manager** | `chat-session-manager` | [link](https://api-gateway.ai.t-systems.net/chat-session-manager/redoc) | Sessions, history, feedback |
| **Query Pipeline** | `query-pipeline` | [link](https://api-gateway.ai.t-systems.net/query-pipeline/redoc) | Chat response generation |

> **Changed in v3.19.0**
>
> `DELETE /user-manager/api/v1/users/{id}` and `DELETE /user-manager/api/v1/spaces/{id}/full` now also succeed for a user or Space that no longer exists: they answer `204` and `200` instead of `404`.

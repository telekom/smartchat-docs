# Smartchat Docs

Source: https://docs.smartchat.ai.t-systems.net/

> Documentation for T-Systems Smartchat.

The T-Systems Smartchat is an AI chatbot application. Smartchat enables secure interaction with your own data sources using natural language. You can search documents for information, summarize their content, and generate new content or specific output formats based on them.

The technical foundation is a **Retrieval Augmented Generation (RAG)** architecture. RAG retrieves information from files or databases and provides it to the language model (Large Language Model, LLM) as context. This means chat responses are grounded in the retrieved content. Smartchat displays the name of each source used.

> **Data privacy**
>
> The language models used in Smartchat are **not** trained on user inputs. Data processing takes place in a secure cloud environment within the EU, operated by Telekom and hosted in T-Cloud Public. A [selection of LLMs](https://docs.llmhub.t-systems.net/plans/) is available and continuously updated with the latest models.
>
> Data you mark as [confidential](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/) is processed only by Telekom-hosted models and is never sent to external providers.

[FAQ ](https://docs.smartchat.ai.t-systems.net/faq/)Answers to common questions about integrations, security, Spaces, large document collections and models.

[User Documentation ](https://docs.smartchat.ai.t-systems.net/user/)Getting started, knowledge collections, assistants, Deep Dive, agents and administration.

Multi-Tenancy

Fully isolated tenants (Spaces) with separate users, documents, and configurations — all on a single deployment.

Confidential Data

Mark a collection or a whole Space as confidential and Smartchat keeps it on Telekom-hosted models: no externally hosted models, no web search, no sharing.

Enterprise RBAC

Fine-grained role-based access control across spaces, admin panels, and API endpoints — synced with your SSO provider.

Async Ingestion Pipeline

Scalable, fully asynchronous document ingestion — handles large document volumes without blocking.

Security Hardening

Sandboxed code execution, input validation, and attack surface reduction beyond upstream defaults.

Compliance & Accessibility

Certified for enterprise compliance standards and accessibility requirements.

Confluence Integration

Connect Confluence Data Center spaces — pages are auto-synced and become searchable context in chats.

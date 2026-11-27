# Deep Dive

Source: https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/

> How to use the Deep Dive research feature in Smartchat.

**Deep Dive** is Smartchat’s in-depth research mode, equivalent to what other AI chatbots call “Deep Research”. Instead of a single LLM response, Deep Dive runs a multi-step research agent that reads through your Space’s documents, synthesises findings, and writes a structured report complete with sources.

## [Requirements](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#requirements)

Space Users need the **Deep Dive** [permission](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/), set on one of their groups under **Space Owner → Groups**. Space Owners have it in their Space without a group.

## [How Deep Dive works](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#how-deep-dive-works)

### [Spaces only](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#spaces-only)

Deep Dive works inside a **Space**. It searches all documents in the Space you currently have open. You cannot restrict which documents it uses; it always searches the full Space knowledge base. If you need answers from a different knowledge base, switch to that Space before starting a run.

### [Your settings are set aside](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#your-settings-are-set-aside)

Model selection, reasoning effort, and any system prompt configured for the Space do not affect a Deep Dive run. The agent uses its own dedicated research model to ensure consistent, reliable results. That research model is always a T-Cloud model hosted by T-Systems, so Deep Dive can be used with [confidential](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/) data: all processing takes place in Germany and no data is sent to an external party. Only your direct research question influences what it does. Nothing changes for your regular chat.

## [How often can I use it?](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#how-often-can-i-use-it)

Each user has:

- **10 runs per day**: the toggle shows how many you have used out of your daily total (e.g. `0/10`).
- **2 concurrent runs**: you can have up to two Deep Dive runs active at the same time across all your chats.

Daily runs reset at midnight.

Individual agreements can override these limits, so your own limit may be different. Application Owners are exempt from them entirely.

## [Starting a Deep Dive](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#starting-a-deep-dive)

*\[Image: Deep Dive toggle in the message input showing remaining daily runs]*

1. Open the Space whose documents you want the agent to research.
2. Toggle **Deep Dive** in the message input area before sending your message. The toggle shows how many runs you have used today.
3. Type your research question and send it.

## [Approving the research plan](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#approving-the-research-plan)

After receiving your question, Deep Dive proposes a refined research question for your review before doing any work. The status indicator shows **“Awaiting approval”**. You have three options:

*\[Image: Research question proposal with Approve, Give Feedback, and Reject buttons and "Awaiting approval" status]*

| Action | What happens |
| - | - |
| **Approve** | The agent starts working immediately. |
| **Give Feedback** | Opens a text field where you can describe what to change. The agent revises the research question and asks again. |
| **Reject** | Cancels the run. No quota is consumed. |

The agent will not start working until you approve. If you close the chat while it is awaiting approval, the run stays paused until you return and respond.

## [While the agent is running](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#while-the-agent-is-running)

Once approved, the agent runs in the background. You will see:

*\[Image: Agent streaming live updates into the chat with "Working" status]*

- A **spinner** in the bottom-right corner of the chat.
- The status indicator in the top-right corner of the agent message showing **“Working”**.
- Live updates streamed into the chat as the agent works, including documents it finds along the way.

You can close the chat or switch to a different chat and the agent will keep running. Come back to the same chat to see the final report when it is done.

## [The research report](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/#the-research-report)

When the run completes, the status changes to **“Completed”** and the agent delivers its findings as a formatted Markdown report with:

*\[Image: Completed Deep Dive with "Deep Dive Event History" and "Open Report" button]*

- **Inline citations**: every claim links back to the source document.
- **Downloadable report**: export the full report as a file.

The report is added to the chat history like a regular message. You can ask follow-up questions in the same chat afterwards. Follow-ups use regular chat mode and will not trigger another Deep Dive run unless you toggle Deep Dive again.

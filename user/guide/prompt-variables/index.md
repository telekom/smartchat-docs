# Prompt Variables

Source: https://docs.smartchat.ai.t-systems.net/user/guide/prompt-variables/

> Placeholders such as today's date or your name that fill themselves in when you use a prompt template or your personal system prompt.

**Prompt variables** are placeholders in double curly braces, such as `{{CURRENT_DATE}}`. Smartchat replaces them with a current value, so a [prompt template](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-prompt-templates) or your personal system prompt stays up to date without editing.

## [Available variables](https://docs.smartchat.ai.t-systems.net/user/guide/prompt-variables/#available-variables)

| Variable | Replaced with | Prompt templates | Personal system prompt |
| - | - | :-: | :-: |
| `{{CURRENT_DATE}}` | Today’s date, e.g. `2026-11-04` | ✓ | ✓ |
| `{{CURRENT_TIME}}` | The current time, e.g. `14:05:09` (system prompt: `2:05:09 PM`) | ✓ | ✓ |
| `{{CURRENT_DATETIME}}` | Date and time combined | ✓ | ✓ |
| `{{CURRENT_WEEKDAY}}` | The weekday in English, e.g. `Wednesday` | ✓ | ✓ |
| `{{CURRENT_TIMEZONE}}` | Your time zone, e.g. `Europe/Berlin` | ✓ | ✓ |
| `{{USER_NAME}}` | Your display name | ✓ | ✓ |
| `{{USER_LANGUAGE}}` | Your interface language, e.g. `de-DE` | ✓ | ✓ |
| `{{USER_LOCATION}}` | Your coordinates, if you allow location access in your browser | ✓ | – |
| `{{CLIPBOARD}}` | The text in your clipboard | ✓ | – |

Date, time and time zone are taken from your device. Variables must be written exactly as shown, in capital letters.

## [Variables in prompt templates](https://docs.smartchat.ai.t-systems.net/user/guide/prompt-variables/#variables-in-prompt-templates)

1. Open **Workspace → Prompts** and create a new prompt template or open an existing one.
2. Write the variables into the prompt content. Any other word in double curly braces, such as `{{recipient}}`, is a gap that you fill in yourself each time you use the template.
3. In the chat, type **/** followed by the template’s command and select the template.

The variables are filled in as soon as you select the template, and the text appears in the chat input. The first gap is selected, so you can type over it. Press **Tab** to jump to the next gap. Check the text, then send it.

Example template:

```text
Write a short status update for {{recipient}} as of {{CURRENT_DATE}}. Sign it with {{USER_NAME}}.
```

> **Note**
>
> - A gap you do not fill in is sent to the model as written, including the curly braces.
> - For `{{CLIPBOARD}}` and `{{USER_LOCATION}}`, your browser may ask for permission. If you copied an image, it is attached to the message as well.

## [Variables in your personal system prompt](https://docs.smartchat.ai.t-systems.net/user/guide/prompt-variables/#variables-in-your-personal-system-prompt)

Variables also work in your personal system prompt under **Settings → General → System Prompt (Advanced)**. They are filled in each time you send a message, so the model always sees the current values.

> **Caution**
>
> In the personal system prompt, each variable is only replaced the first time it appears. Use every variable at most once.

Gaps such as `{{recipient}}`, `{{CLIPBOARD}}` and `{{USER_LOCATION}}` are not filled in here.

## [Where variables are not replaced](https://docs.smartchat.ai.t-systems.net/user/guide/prompt-variables/#where-variables-are-not-replaced)

- **Assistant system prompts:** the system prompt of an [Assistant](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-assistants) is sent to the model exactly as written. Variables in it stay unchanged.
- **Prompt suggestions** on the start screen: only `{{CLIPBOARD}}` is filled in.

> **Tip**
>
> Smartchat tells the model today’s date in every chat. You do not need `{{CURRENT_DATE}}` just so the model knows the date.

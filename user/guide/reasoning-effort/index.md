# Reasoning Effort

Source: https://docs.smartchat.ai.t-systems.net/user/guide/reasoning-effort/

> Choose how much a reasoning model thinks before it answers.

Some models think a question through before they answer. **Reasoning effort** sets how much thinking they may do: more effort usually gives better answers to hard questions, such as analyses, calculations or code, but the answer takes longer and uses more tokens.

## [Choosing the effort](https://docs.smartchat.ai.t-systems.net/user/guide/reasoning-effort/#choosing-the-effort)

The selector shows the chosen effort, here Default.

1. Select a model that supports reasoning effort. A selector then appears in the message box that shows the current effort, for example **Default**. It only appears when every selected model supports reasoning effort, and disappears again when you add a model that does not.
2. Open it and pick **Low**, **Medium** or **High**.
3. Send your message. The effort applies to the messages you send until you change it.

Depending on the model, the list also offers a first option that leaves the effort to the model: **Default**, **Auto**, or **Disabled** for models that then answer without thinking first.

> **When to raise it**
>
> Start with the model’s default. Raise the effort when an answer to a demanding question misses steps or gets details wrong, and lower it for quick questions where speed matters more.

Reasoning effort does not apply to [Deep Dive](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/), which decides how long it researches by itself.

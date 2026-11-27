# Understanding & Using Outputs

Source: https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/

> Viewing sources and applying functions to responses.

## [Viewing sources](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#viewing-sources)

When a space’s knowledge is used to generate a response, the response includes up to five references at the bottom. Click a source to view more details. Where a document has an original address, for example a Confluence page, the source links to that original; otherwise it links to the copy stored in Smartchat.

*\[Image: Response with source reference]*

The percentage next to each source indicates how strongly the document correlates with the generated response (relevance score):

- **High percentage (90%–100%)** — Most of the content can be derived almost exclusively from this document.
- **Medium percentage (50%–80%)** — The document contributes significantly but is only part of a composite answer.
- **Low percentage (below 50%)** — The document is only peripherally involved (supporting evidence, background knowledge).

The values are produced automatically by Smartchat’s retrieval and ranking mechanism: the semantic similarity between document content and response sections is measured and converted into a percentage relevance score.

*\[Image: Source detail view with relevance score]*

## [Functions on responses](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#functions-on-responses)

You can further interact with Smartchat responses: edit, copy, read aloud, continue, stop, or regenerate.

*\[Image: Function icons below a response]*

### [Edit response](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#edit-response)

*\[Image: Edit button]*

Click the **pencil icon** to edit a response. Use “Save as Copy” to save the output as a separate copy, or the Save button to overwrite.

*\[Image: Edit view with save options]*

### [Copy response](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#copy-response)

*\[Image: Copy button]*

Click the **copy icon** to copy the response to your clipboard.

### [Read response aloud](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#read-response-aloud)

*\[Image: Read aloud button]*

Click the **speaker icon** to have the response read aloud.

### [Continue/stop response](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#continuestop-response)

*\[Image: Continue button]*

Click the **play icon** to generate additional text.

*\[Image: Stop button during generation]*

An ongoing response can be interrupted using the **“Stop” icon** next to the text input.

### [Regenerate response](https://docs.smartchat.ai.t-systems.net/user/guide/understanding-outputs/#regenerate-response)

*\[Image: Regenerate button]*

The **cycle icon** prompts the LLM to rephrase the response using different wording.

*\[Image: Regenerated response]*

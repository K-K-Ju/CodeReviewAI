# Part 2
Possible improvments for highloaded usage:
 - Using OpenAI (Batch API)[https://platform.openai.com/docs/guides/batch/overview] for cost saving (only if the result is not needed immediatly)
 - Using OpenAI Prompt caching (doc)[https://platform.openai.com/docs/guides/prompt-caching].
 - Implement query proccessing queue to decrease service load

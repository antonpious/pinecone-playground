from openaiclient import openaiClient

# create embeddings in one go for all documents
def embed(docs: list[str]) -> list[list[float]]:
    res = openaiClient.embeddings.create(
        input=docs,
        model="text-embedding-3-small"
    )
    doc_embeds = [r.embedding for r in res.data] 
    return doc_embeds 

'''
you might get this error
if you don't have credit in openai
raise self._make_status_error_from_response(err.response) from None
openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
'''
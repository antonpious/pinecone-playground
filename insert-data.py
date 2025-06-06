# insert data with embedding from OpenAI
# this uses the text-embedding-3-small
from pinecoregetindex import getIndex
from datarecords import data
from pinecoreindex import indexName, namespaceName
from openaiembed import embed

doc_embeds = embed([d["text"] for d in data])

vectors = []
for d, e in zip(data, doc_embeds):
    vectors.append({
        "id": d['id'],
        "values": e,
        "metadata": {'text': d['text']}
    })

index = getIndex(indexName)

index.upsert(
    vectors = vectors,
    namespace = namespaceName
)
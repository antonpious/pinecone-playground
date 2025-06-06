from pinecoregetindex import getIndex
from pinecoreindex import indexName, namespaceName
from openaiembed import embed

index = getIndex(indexName)

### Query
query = "Tell me about the tech company known as Apple"

x = embed([query])

print("The embed query", x[0])

print("Printing results")

results = index.query(
    namespace = namespaceName,
    vector = x[0],
    top_k = 3,
    include_values = False,
    include_metadata = True
)

print(results)

'''
This does print the Apple is a fruit with a score of 0.46
One should filter this score to match

{'matches': [{'id': 'vec2',
              'metadata': {'text': 'The tech company Apple is known for its '
                                   'innovative products like the iPhone.'},
              'score': 0.682733238,
              'values': []},
             {'id': 'vec4',
              'metadata': {'text': 'Apple Inc. has revolutionized the tech '
                                   'industry with its sleek designs and '
                                   'user-friendly interfaces.'},
              'score': 0.612685859,
              'values': []},
             {'id': 'vec1',
              'metadata': {'text': 'Apple is a popular fruit known for its '
                                   'sweetness and crisp texture.'},
              'score': 0.467486,
              'values': []}],
 'namespace': 'tenant1',
 'usage': {'read_units': 6}}

'''
from pinecoreclient import pinecoreClient, serverSpec
from pinecoreindex import indexName



# The 1536 dimension is dew to the model embedding size
# This should match the model used to embed each text
# no matter what the length of the text is each record is stored
# with 1536 vector dimensions.
#  A 1536 dimensional vector is ~6.15 kilobytes. 
# Scaling that up to 1M vectors, the raw data tops 6 gigabytes.
if not pinecoreClient.has_index(indexName):
    pinecoreClient.create_index(
        name=indexName,
        dimension=1536,
        metric="cosine",
        spec=serverSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
else:
    print("Index exists")


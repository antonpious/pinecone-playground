from pinecoreclient import pinecoreClient

# the create index needs to be done before get index
def getIndex(index_name):
    index = pinecoreClient.Index(index_name)
    return index


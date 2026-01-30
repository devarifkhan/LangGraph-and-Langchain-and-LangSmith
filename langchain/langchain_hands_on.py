from langchain_community.document_loaders import TextLoader, PyPDFLoader

loader = TextLoader('NeRF.txt')
text_documents = loader.load()
print(text_documents)

loader = PyPDFLoader('iso27001.pdf')
docs = loader.load()
print(docs)

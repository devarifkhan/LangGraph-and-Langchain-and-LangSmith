from langchain_community.document_loaders import TextLoader, PyPDFLoader

# load a text file
loader = TextLoader('NeRF.txt')
text_documents = loader.load()
print(text_documents)

# load a PDF file
loader = PyPDFLoader('iso27001.pdf')
docs = loader.load()
print(docs)
print("Page content: ",docs[0].page_content)
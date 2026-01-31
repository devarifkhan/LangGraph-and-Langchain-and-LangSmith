import bs4
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader

# load a PDF file
loader = PyPDFLoader('Python_Programming.pdf')
docs = loader.load()
print(docs)
print("Page content: ",docs[0].page_content)


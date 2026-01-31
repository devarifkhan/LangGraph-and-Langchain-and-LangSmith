import bs4
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader

# load a text file
loader = TextLoader('NeRF.txt')
text_documents = loader.load()
print(text_documents)

# load a PDF file
loader = PyPDFLoader('iso27001.pdf')
docs = loader.load()
print(docs)
print("Page content: ",docs[0].page_content)

# Web based loaders
loader = WebBaseLoader(web_paths=["https://en.wikipedia.org/wiki/Artificial_intelligence"])
loaded_web_docs= loader.load()
print(loaded_web_docs)
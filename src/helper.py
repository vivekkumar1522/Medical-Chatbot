from langchain.document_loaders import PyPDFLoader ,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings  
from typing import List
from langchain.schema import Document   






def load_pdf_files(data):
    loader = DirectoryLoader(
        data, #path of the file
        glob="*.pdf", #to load only pdf files from data
        loader_cls=PyPDFLoader #we need to load it from  pypdfloader 
    ) 

    documents = loader.load()
    return documents


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content = doc.page_content,
                metadata={'source': src}
            )
        )
    return minimal_docs    

#split the documents into smaller chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    chunk_texts = text_splitter.split_documents(minimal_docs)
    return chunk_texts


def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        )
    return embeddings




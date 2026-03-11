# 🏥 Medical Chatbot — RAG-Powered AI Health Assistant

An intelligent medical chatbot built using **Retrieval-Augmented Generation (RAG)** that answers health-related queries grounded in real medical documents — reducing hallucinations and improving reliability.

---

## 🚀 Features

- 📄 Ingests medical PDFs and indexes them into a vector database
- 🔍 Retrieves relevant context using semantic similarity search
- 🤖 Generates accurate, context-aware answers using GPT-4o
- 💬 Clean chat interface built with Flask
- ⚡ Fast retrieval powered by Pinecone vector store

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | OpenAI GPT-4o |
| Embeddings | HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Store | Pinecone |
| Orchestration | LangChain |
| Backend | Flask |
| Document Loader | PyPDF / LangChain DirectoryLoader |

---

## 📁 Project Structure

```
Medical-Chatbot/
│
├── src/
│   ├── __init__.py
│   ├── helper.py         # PDF loading, chunking, embedding utilities
│   └── prompt.py         # System prompt for the RAG chain
│
├── data/                 # Place your medical PDF files here
│
├── research/
│   └── trials.ipynb      # Experimentation notebook
│
├── app.py                # Flask web application
├── store_index.py        # Script to embed & store docs in Pinecone
├── requirements.txt
├── setup.py
├── template.sh           # Script to scaffold project structure
└── .env                  # API keys (not committed)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create and activate a conda environment

```bash
conda create -n medibot python=3.10
conda activate medibot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## 📥 Indexing Medical Documents

1. Place your medical PDF files inside the `data/` directory.
2. Run the indexing script to embed and store them in Pinecone:

```bash
python store_index.py
```

This will:
- Load and parse all PDFs from `data/`
- Split text into chunks
- Generate embeddings using HuggingFace Sentence Transformers
- Upsert embeddings into your Pinecone index (`medical-chatbot`)

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and navigate to:

```
http://localhost:8080
```

---

## 🧠 How It Works

```
User Query
    │
    ▼
HuggingFace Embeddings  ──►  Pinecone Vector Store
                                      │
                              Top-K Similar Chunks
                                      │
                                      ▼
                              GPT-4o (LLM) + System Prompt
                                      │
                                      ▼
                              Grounded Medical Answer
```

1. User submits a medical query via the chat interface.
2. The query is embedded and used to retrieve the top 3 most relevant document chunks from Pinecone.
3. The retrieved chunks + query are passed to GPT-4o via a RAG chain.
4. GPT-4o generates a response grounded in the retrieved medical context.

---

## 📦 Requirements

```
langchain==0.3.26
flask==3.1.1
sentence-transformers==4.1.0
pypdf==5.6.1
python-dotenv==1.1.0
langchain-pinecone==0.2.8
langchain-openai==0.3.24
langchain-community==0.3.26
```

---

## 🔑 API Keys Required

- **OpenAI API Key** — [https://platform.openai.com](https://platform.openai.com)
- **Pinecone API Key** — [https://www.pinecone.io](https://www.pinecone.io)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👤 Author

**Vivek Kumar**
- Email: unitevivek9999@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

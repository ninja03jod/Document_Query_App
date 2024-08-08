# Document Query Application

This application allows users to upload documents, query them, and download their chat history. It uses Streamlit for the user interface and LangChain with the Llama3 model for querying documents.

## Project Structure

- `app/main.py`: Main entry point for the Streamlit application.
- `app/document_upload.py`: Handles document upload and retrieval.
- `app/query_processing.py`: Manages document querying.
- `app/chat_history.py`: Handles chat history storage and retrieval.
- `app/utils.py`: Contains utility functions for text extraction from documents.
- `app/database.py`: Manages database operations and schema.
- `Dockerfile`: Defines the Docker image for the application.
- `requirements.txt`: Lists the Python dependencies required for the application.

## Database

- `database.db`: SQLite database used for storing documents and user history. It has two tables:
  - `documents`: Stores the uploaded documents with fields `id`, `file_name`, `file_type`, and `content`.
  - `user_history`: Stores the queries and responses with fields `id`, `user_id`, `query`, `response`, and `timestamp`.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ninja03jod/document_query_app.git
cd document_query_app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv my_env
source my_env/bin/activate  # On Windows, use `my_env\Scripts\activate`
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Set Up Database

The application uses SQLite for data storage. The database file database.db will be created automatically when you run the application.

## Running the Application

```bash
streamlit run app/main.py
```
## Usage

### 1. Upload Document:
Use the sidebar to upload documents (PDF, DOCX, or TXT). This will save the document content to the SQLite database.

### 2.Query Documents:
Enter your query in the main section and click "Submit Query" to get responses from the uploaded documents. The query and response will be saved in the user_history table of the database.

### 3.Download Chat History:
Click on "Download Chat History" in the sidebar to download your chat history in a text file.

## Code Overview
### `app/main.py`
- Functionality: Entry point for the Streamlit application. Handles document upload, query submission, and chat history download.
- Usage: Run this file with Streamlit to start the application.

### `app/document_upload.py`

#### Functions:
- `upload_document(uploaded_file)`: Uploads and saves the document to the database.
- `get_documents()`: Retrieves all documents from the database.
- `Usage`: Called by main.py for document upload and retrieval.

### app/query_processing.py
#### Function:
- `query_document(query_text, documents)`: Queries the documents using the Llama3 model.
- `Usage`: Called by main.py to process user queries.

### app/chat_history.py
#### Functions:
- `handle_history(download=False, user_id="default_user")`: Retrieves and optionally saves chat history to a file.
- `log_query(user_id, query, response)`: Logs user queries and responses to the database.
- `Usage`: Called by main.py to handle and save chat history.

### app/utils.py
#### Functions:
- `extract_text_from_pdf(file)`: Extracts text from PDF files.
- `extract_text_from_docx(file)`: Extracts text from DOCX files.
- `extract_text_from_txt(file)`: Extracts text from TXT files.
- `extract_text(file, file_type)`: Chooses the appropriate text extraction function based on the file type.
- `Usage`: Used by document_upload.py to extract text from uploaded documents.

### app/database.py
#### Functions:
- `get_db_connection()`: Establishes a connection to the SQLite database.
- `create_tables()`: Creates necessary tables in the SQLite database if they do not exist.
- `Usage`: Called by document_upload.py and chat_history.py to interact with the database.

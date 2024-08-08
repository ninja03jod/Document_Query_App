from utils import extract_text
from database import get_db_connection, create_tables

create_tables()

def upload_document(uploaded_file):
    file_name = uploaded_file.name
    file_type = file_name.split('.')[-1]
    content = extract_text(uploaded_file, file_type)
    
    conn = get_db_connection()
    with conn:
        conn.execute('''
            INSERT INTO documents (file_name, file_type, content)
            VALUES (?, ?, ?)
        ''', (file_name, file_type, content))

def get_documents():
    conn = get_db_connection()
    documents = conn.execute('SELECT file_name, content FROM documents').fetchall()
    return documents

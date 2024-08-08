import streamlit as st
from document_upload import upload_document, get_documents
from query_processing import query_document
from chat_history import handle_history
import pandas as pd
import io

# Function to generate a downloadable file
def download_file(file_data, file_name):
    buffer = io.BytesIO()
    buffer.write(file_data.encode('utf-8'))
    buffer.seek(0)
    st.download_button(
        label="Download Chat History",
        data=buffer,
        file_name=file_name,
        mime="text/plain"
    )

def main():
    st.title('Document Query Application')

    # Document upload
    st.sidebar.header('Upload Document')
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        upload_document(uploaded_file)
        st.sidebar.success("Document uploaded successfully!")

    # Query section
    st.header('Query Documents')
    query_text = st.text_input("Enter your query:")
    if st.button("Submit Query"):
        documents = get_documents()
        if not documents:
            st.error("No documents found. Please upload some documents first.")
        else:
            response = query_document(query_text, documents)
            st.write("Response:", response)
            save_to_history(query_text, response)
            st.success("Query processed successfully!")

    # View and download chat history
    st.sidebar.header('Chat History')
    if st.sidebar.button("Download Chat History"):
        history_lines = load_chat_history()
        if not history_lines:
            st.sidebar.warning("No chat history found.")
        else:
            formatted_history = format_chat_history(history_lines)
            download_file(formatted_history, "chat_history.txt")
            st.sidebar.success("Chat history downloaded!")

def save_to_history(query, response):
    """ Save the query and response to a chat history file. """
    with open("chat_history.txt", "a") as file:
        file.write(f"Query: {query}\nResponse: {response}\nTimestamp: {pd.Timestamp.now()}\n\n")

def load_chat_history():
    """ Load chat history from a file. """
    try:
        with open("chat_history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def format_chat_history(history_lines):
    """ Format chat history for readability. """
    formatted_history = "Query\tResponse\tTimestamp\n"
    query, response, timestamp = "", "", ""
    for line in history_lines:
        if "Query:" in line:
            query = line.split("Query:")[1].strip()
        elif "Response:" in line:
            response = line.split("Response:")[1].strip()
        elif "Timestamp:" in line:
            timestamp = line.split("Timestamp:")[1].strip()
            formatted_history += f"{query}\t{response}\t{timestamp}\n"
    return formatted_history

if __name__ == "__main__":
    main()
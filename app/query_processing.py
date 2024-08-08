from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import TransformChain

# Initialize the Llama3 model
llm = Ollama(model='llama3')

def query_document(query_text, documents):
    """
    Query the documents using the Llama3 model.
    
    Args:
    - query_text (str): The user's query.
    - documents (list): List of documents, each document should be a dictionary with 'content' key.

    Returns:
    - str: Response from the Llama3 model.
    """
    # Combine all document contents into a single string
    combined_document_text = "\n\n".join(doc['content'] for doc in documents)

    # Create a prompt template for the query
    prompt_template = PromptTemplate(
        input_variables=["query", "context"],
        template="You are a helpful assistant. Based on the following context, answer the query:\n\nContext:\n{context}\n\nQuery:\n{query}"
    )
    
    # Create the final prompt with the provided template
    final_prompt = prompt_template.format(query=query_text, context=combined_document_text)

    # Query the model with the formatted prompt
    response = llm.invoke(final_prompt)
    
    return response



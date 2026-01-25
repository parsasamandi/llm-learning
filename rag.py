import ollama
import chromadb
from sentence_transformers import SentenceTransformer

# What is our embedding model?
print("What is our embedding model?")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Create the vector database
chroma = chromadb.Client()
collection = chroma.create_collection(name="documents")

# Load the documents
print("Loading documents...")
with open("documents/company.txt", "r") as f:
    text = f.read()

# Split into chunks (each line is a chunk for simplicity)
chunks = [line.strip() for line in text.split("\n") if line.strip()]

# Step 4: Embed and store chunks
print("Embedding and storing chunks...") # We are converting text into embeddings and storing them in the vector database
for i, chunk in enumerate(chunks):  
    embedding = embedder.encode(chunk).tolist() # For each chunk of the iterator, we compute its embedding
    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[f"doc_{i}"]
    )
print(f"Stored {len(chunks)} chunks.\n")
# Step 5: Query loop
while True:
    question = input("Ask a question (or 'quit'): ")
    
    if question.lower() == "quit":
        break
    
    # Embed the question
    question_embedding = embedder.encode(question).tolist()
    
    # Search for relevant chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=6
    )
    
    relevant_chunks = results["documents"][0]
    
    print("\n--- Retrieved context ---")
    for chunk in relevant_chunks:
        print(f"  • {chunk}")
    print("-------------------------\n")
    
    # Build prompt with context
    context = "\n".join(relevant_chunks)
    
    prompt = f"""Use the following context to answer the question.
If the answer is not in the context, say "I don't have that information."

Context:
{context}

Question: {question}

Answer:"""

    # Get LLM response
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    
    print(f"Answer: {response['message']['content']}\n")
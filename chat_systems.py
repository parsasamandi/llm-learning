import ollama

system_prompt = """You are a senior Python developer doing code review.
- Point out bugs and issues
- Suggest improvements
- Be direct and concise
- If the code is good, say so"""

history = [
    {"role": "system", "content": system_prompt}
]

print("Code Reviewer ready. Paste code or ask questions. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    history.append({"role": "user", "content": user_input})
    
    response = ollama.chat(
        model="llama3.2",
        messages=history
    )
    
    assistant_message = response["message"]["content"]
    history.append({"role": "assistant", "content": assistant_message})
    
    print(f"\nReviewer: {assistant_message}\n")
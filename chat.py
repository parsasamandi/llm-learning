import ollama

# This list stores the whole conversation
history = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    # Add user message to history
    history.append({"role": "user", "content": user_input})
    
    # Send FULL history to the model
    response = ollama.chat(
        model="llama3.2",
        messages=history
    )
    
    # Get assistant's reply
    assistant_message = response["message"]["content"]
    
    # Add assistant's reply to history
    history.append({"role": "assistant", "content": assistant_message})
    
    print(f"Llama: {assistant_message}\n")
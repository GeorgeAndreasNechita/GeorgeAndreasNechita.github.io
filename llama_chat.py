import ollama

# Define the model you want to chat with
MODEL_NAME = "qwen2.5"

# Initialize conversation history with an optional system prompt
messages = [
    {
        "role": "system", 
        "content": "You are a helpful, friendly AI assistant. Converse naturally with the user."
    }
]

print(f"--- Interactive Chat with {MODEL_NAME} ---")
print("Type your message and press Enter. Type 'exit' or 'quit' to end the chat.\n")

while True:
    try:
        # Get user input from the terminal
        user_input = input("You: ").strip()
        
        # Check if the user wants to quit
        if user_input.lower() in ["exit", "quit"]:
            print("\nEnding chat session. Goodbye!")
            break
            
        if not user_input:
            continue

        # Append the user's message to the conversation history
        messages.append({"role": "user", "content": user_input})

        print(f"\n{MODEL_NAME}: ", end="", flush=True)

        # Call ollama.chat with streaming enabled for a real-time typing effect
        stream = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True,
        )

        assistant_response = ""
        
        # Stream the response chunks directly to the console
        for chunk in stream:
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
            assistant_response += content

        print("\n") # Add spacing after the response

        # Append the model's full response back into the history to maintain context
        messages.append({"role": "assistant", "content": assistant_response})

    except KeyboardInterrupt:
        print("\n\nChat interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
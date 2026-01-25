import ollama
import json

system_prompt = """Extract information and respond ONLY with valid JSON.
No explanation. No markdown. Just JSON.

Format:
{"name": string, "age": number, "city": string}

If any field is unknown, use null."""

user_input = "Sarah is 32 years old and lives in Toronto"

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
)

raw_response = response["message"]["content"]
print("Raw response:", raw_response)

# Try to parse as JSON
try:
    data = json.loads(raw_response)
    print("\nParsed data:")
    print(f"  Name: {data['name']}")
    print(f"  Age: {data['age']}")
    print(f"  City: {data['city']}")
except json.JSONDecodeError as e:
    print(f"\nFailed to parse JSON: {e}")
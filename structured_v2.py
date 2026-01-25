import ollama
import json
import re

def extract_json(text: str) -> dict | None:
    """Try to extract JSON from LLM response, even if there's extra text."""
    
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Try to find JSON in the text
    patterns = [
        r'\{[^{}]*\}',  # Simple object
        r'```json\s*(\{.*?\})\s*```',  # Markdown code block
        r'```\s*(\{.*?\})\s*```',  # Code block without language
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                json_str = match.group(1) if '```' in pattern else match.group(0)
                return json.loads(json_str)
            except (json.JSONDecodeError, IndexError):
                continue
    
    return None


def extract_person_info(text: str) -> dict | None:
    """Extract person information from natural language."""
    
    system_prompt = """Extract information and respond ONLY with valid JSON.
No explanation. No markdown. Just JSON.

Format: {"name": string, "age": number, "city": string}
Use null for unknown fields."""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    
    return extract_json(response["message"]["content"])


# Test it
test_sentences = [
    "John is 25 years old and lives in Vancouver",
    "My friend Maria, age 30, moved to Berlin last year",
    "The CEO is named Alex",
]

for sentence in test_sentences:
    print(f"Input: {sentence}")
    result = extract_person_info(sentence)
    if result:
        print(f"Output: {result}\n")
    else:
        print("Failed to extract\n")
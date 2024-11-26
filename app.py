from transformers import pipeline
import wikipedia


chat_generator = pipeline("text-generation", model="gpt2")


summarizer = pipeline("summarization")

def get_wikipedia_summary(query):
    """Fetch and summarize Wikipedia content."""
    try:
        content = wikipedia.summary(query, sentences=5)
        summarized_content = summarizer(content, max_length=60, min_length=20, do_sample=False)
        return summarized_content[0]['summary_text']
    except Exception as e:
        return "I couldn't retrieve information on that topic."

def generate_response(prompt):
    """Main function to determine user intent and generate a response."""
    if "brief" in prompt.lower() or "explain" in prompt.lower() or "summary" in prompt.lower():
        response = get_wikipedia_summary(prompt)
    else:
        response = chat_generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    
    return response

user_prompt = "Can you briefly explain neural networks?"
print(f"Jarvis: {generate_response(user_prompt)}")

user_prompt = "Tell me something funny, Jarvis!"
print(f"Jarvis: {generate_response(user_prompt)}")

import os
import json
from groq import Groq

def get_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_text_summary_data(text):
    client = get_client()

    chat_history = [
        {
            "role": "user",
            "content": "You are a helpful assistant that provides short summaries of the text provided along with a name that best describes the topic of the provided text."
            "In the response provided, the summary should always be called 'Summary' and the name should always be called 'Name'."
            "Additionally, the summary should be included first in the response, followed by the name."
            "For example, a sample response would be as follows:"
            "'**Summary:**\n\nReggae is a genre of music that originated in Jamaica in the late 1960s, characterized by its distinctive drum and bass rhythms,"
            "offbeat rhythms, and emphasis on call and response.\n\n**Name:** Reggae Music'."
        },
        {
            "role": "assistant",
            "content": "I'd be happy to help. Please go ahead and provide the text you'd like me to summarize, and I'll do my best to condense it into a shorter and more digestible form while still capturing the main points and essential information."
        },
    ]

    chat_history.append({
        "role": "user",
        "content": f"{text}",
    })

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=chat_history,
        max_tokens=1024,
        temperature=1,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    response_content = response.split("\n\n")
    if len(response_content) > 2:
        summary_text = response_content[1]
        summary_name = response_content[2]

    if summary_text.find("**Summary:** ") > -1:
        summary_text = summary_text.split("**Summary:** ")[1]

    if summary_name.find("**Name:** ") > -1:
        summary_name = summary_name.split("**Name:** ")[1]

    summary_data = {
        "name": summary_name,
        "original_text": text,
        "summary": summary_text,
    }

    return summary_data

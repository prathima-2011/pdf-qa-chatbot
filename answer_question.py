from openai import OpenAI

def answer_question(context, question):
    client = OpenAI()
    prompt = f"""
    Answer the question using only this context: {context}

    Question: {question}
    """

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


from config import get_groq_api_key
from groq import Groq
from .retriever import get_relevant_context

def generate_insights(abnormal_tests):
    api_key = get_groq_api_key()
    client = Groq(api_key=api_key)

    insights = []

    for test in abnormal_tests:
        query = f"{test['test_name']} {test['status']} lab value medical meaning"
        context = get_relevant_context(query)

        prompt = f"""
You are a medical information assistant.


You are a friendly and professional Medical Information Assistant. 

USER DATA:
The patient's lab results show the following:
{test['test_name']}: {test['value']} {test.get('unit')} (Status: {test['status']})

KNOWLEDGE SOURCE (RAG):
{context}

CONVERSATIONAL INSTRUCTIONS:
1. Start by acknowledging the user warmly (e.g., "I've reviewed your results...").
2. Clearly state which tests are high or low in a conversational way.
3. When explaining the reason, use phrases like "Based on medical references I found..." or "According to the knowledge base..."
4. Keep the tone supportive but strictly follow the safety rules below.

SAFETY RULES:
- Do NOT provide a diagnosis.
- Do NOT suggest specific medications.
- Suggest simple lifestyle adjustments.
- Always end by telling them which specific questions to ask their doctor.

Answer:
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        insights.append({
            "test": test["test_name"],
            "insight": response.choices[0].message.content
        })

    return insights

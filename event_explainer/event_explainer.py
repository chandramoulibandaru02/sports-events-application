from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import SecretStr
import os

load_dotenv()

api = SecretStr("api")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api,
    temperature=0.1
)


prompt = ChatPromptTemplate.from_template("""
Explain this sports event in simple language.

Title: {title}

Description: {description}

Venue: {venue}

Time: {time}
""")


def explain_event(data):

    chain = prompt | llm

    response = chain.invoke({
        "title": data["title"],
        "description": data["description"],
        "venue": data["venue"],
        "time": data["time"]
    })

    return response.content
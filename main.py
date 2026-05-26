from fastapi import FastAPI
from pydantic import BaseModel
from event_explainer.event_explainer import explain_event

app = FastAPI()

class EventRequest(BaseModel):
    title: str
    description: str
    venue: str
    time: str

@app.post("/explain-event")
def explain(data: EventRequest):

    result = explain_event(data.model_dump())

    return {
        "ai_explanation": result
    }
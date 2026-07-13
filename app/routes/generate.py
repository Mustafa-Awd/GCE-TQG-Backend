from fastapi import APIRouter, HTTPException
from app.services.ai_service import generate_exam_questions
import json

router = APIRouter()


@router.post("/generate")
def generate_questions(payload: dict):

    subject = payload.get("subject")
    topic = payload.get("topic")
    difficulty = payload.get("difficulty")
    count = payload.get("count")
    if not subject or not topic:
        raise HTTPException(
            status_code=400,
            detail="Both 'subject' and 'topic' are required.",
        )

    result = generate_exam_questions(subject, topic, difficulty, count)
    if not result or not isinstance(result, str):
        print(result)
        raise HTTPException(
            status_code=502,
            detail="AI service returned an empty response.",
        )

    # Remove markdown formatting if model adds it
    cleaned = (
        result.replace("```json", "")
        .replace("```", "")
        .strip()
    )
    if not cleaned:
        print(result)
        raise HTTPException(
            status_code=502,
            detail="AI service returned empty content after cleaning.",
        )

    # Extract likely JSON object if extra text is present
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    candidate = cleaned[start:end + 1] if start != -1 and end != -1 and end > start else cleaned

    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        print(result)
        raise HTTPException(
            status_code=502,
            detail="AI service returned invalid JSON.",
        )
    
    return parsed
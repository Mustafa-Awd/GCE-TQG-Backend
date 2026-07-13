import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR.parent / "data" / "ICT.json"

with open(FILE_PATH, "r" , encoding="utf-8") as file:
    syllabus = json.load(file)


def getTopic(topic):
    topicContent = syllabus[topic]["syllabus_content"]
    return topicContent

def generatePrompt(subject, topic, difficulty, count):
    topicContent = getTopic(topic)
    prompt = f"""
You are an API that outputs ONLY valid JSON.
Your task is to generate ORIGINAL exam-style questions inspired by Cambridge IGCSE ICT.

Requirements:
- Never copy or closely paraphrase real past paper questions.
- Match Cambridge wording style and structure.
- Use authentic command words such as "Describe", "Explain", "State", "Identify", "Discuss".
- Match realistic mark allocations and difficulty.
- Questions must be solvable using IGCSE ICT syllabus knowledge.
- Maintain examiner tone and formatting.
- Avoid modern topics outside syllabus scope unless explicitly requested.
- Do not include markdown.
- Do not include explanations outside JSON.

ABSOLUTE RULES:
- Do NOT include any explanation
- Do NOT include <think> or reasoning
- Do NOT include markdown
- Output ONLY raw JSON
- No extra keys outside schema

easy questions should prioritize recall and basic understanding and should ideally be worth 1-3 marks.
medium questions should involve application and analysis and should ideally be worth 3-6 marks.
hard questions should require synthesis and evaluation and should ideally be worth 6-10 marks.

mark scheme should be concise and directly related to the question, outlining the key points that would earn marks.

Return exactly this format:

{{
  "questions": [
    {{
      "question": "...",
      "marks": ...,
      "Mark scheme": ["mark 1 ...", "mark 2 ...", "mark 3 ..."],
      "command word": "..."
    }},
    {{
      "question": "...",
      "marks": ...,
      "Mark scheme": ["mark 1 ...", "mark 2 ...", "mark 3 ..."],
      "command word": "..."
    }},
    {{
      "question": "...",
      "marks": ...,
      "Mark scheme": ["mark 1 ...", "mark 2 ...", "mark 3 ..."],
      "command word": "..."
    }}
  ]
}}

Generate {count} questions.

Subject: {subject}
Topic: {topic}
Topic content (generate questions strictly from these topic contents) = {topicContent}
difficulty: {difficulty}
"""
    
    return prompt


# print(generatePrompt("ICT", "Hardware and Software", difficulty="easy", count=3))

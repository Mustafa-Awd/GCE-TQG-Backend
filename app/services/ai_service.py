import os
from dotenv import load_dotenv
from google import genai 
from .prompt_builder import generatePrompt
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
api_key = os.getenv("GEMINI_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_exam_questions(subject, topic, difficulty, count):

    prompt = generatePrompt(subject, topic, difficulty, count)
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    print(response.text)
    data = response.text
    return data













# f"""
# You are an API that outputs ONLY valid JSON.
# Your task is to generate ORIGINAL exam-style questions inspired by Cambridge IGCSE ICT.

# Requirements:
# - Never copy or closely paraphrase real past paper questions.
# - Match Cambridge wording style and structure.
# - Use authentic command words such as "Describe", "Explain", "State", "Identify", "Discuss".
# - Match realistic mark allocations and difficulty.
# - Questions must be solvable using IGCSE ICT syllabus knowledge.
# - Maintain examiner tone and formatting.
# - Avoid modern topics outside syllabus scope unless explicitly requested.
# - Do not include markdown.
# - Do not include explanations outside JSON.

# ABSOLUTE RULES:
# - Do NOT include any explanation
# - Do NOT include <think> or reasoning
# - Do NOT include markdown
# - Output ONLY raw JSON
# - No extra keys outside schema

# easy questions should prioritize recall and basic understanding and should ideally be worth 1-3 marks.
# medium questions should involve application and analysis and should ideally be worth 3-6 marks.
# hard questions should require synthesis and evaluation and should ideally be worth 6-10 marks.

# mark scheme should be concise and directly related to the question, outlining the key points that would earn marks.

# Return exactly this format:

# {{
#   "questions": [
#     {{
#       "question": "...",
#       "marks": ...,
#       "Mark scheme": "...",
#       "command word": "..."
#     }},
#     {{
#       "question": "...",
#       "marks": ...,
#       "Mark scheme": "...",
#       "command word": "..."
#     }},
#     {{
#       "question": "...",
#       "marks": ...,
#       "Mark scheme": "...",
#       "command word": "..."
#     }}
#   ]
# }}

# Generate {count} questions.

# Subject: {subject}
# Topic: {topic}
# difficulty: {difficulty}
# """

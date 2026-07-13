# ExamGen AI API - Backend

A FastAPI-based REST API that generates original Cambridge IGCSE exam-style questions using Google Gemini AI. The backend intelligently creates questions based on specific subjects, topics, and difficulty levels.

## Features

- 🤖 **AI-Powered Question Generation**: Uses Google Gemini to generate original, exam-style questions
- 📚 **Multiple Subjects**: Support for Cambridge IGCSE subjects (ICT, Computer Science, etc.)
- 📊 **Flexible Topic Support**: Generate questions for specific topics within each subject
- ⚙️ **Difficulty Levels**: Customize question difficulty
- 🔧 **RESTful API**: Clean and simple endpoint design
- 🌐 **CORS Enabled**: Pre-configured for frontend integration
- 📦 **MongoDB Integration**: Async database support with Motor

## Tech Stack

- **Framework**: FastAPI 0.136.1
- **Python**: 3.13+
- **AI Model**: Google Gemini 3 Flash
- **Database**: MongoDB (with Motor async driver)
- **Server**: Uvicorn
- **Dependencies**: Pydantic, python-dotenv, requests

## Prerequisites

- Python 3.13 or higher
- Google Gemini API key
- MongoDB instance (optional, for future database features)
- pip or poetry for package management

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or using pyproject.toml:

   ```bash
   pip install -e .
   ```

5. **Configure environment variables**

   Create a `.env` file in the root directory:

   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here (optional)
   ```

## Project Structure

```
backend/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── core/                   # Core configurations
│   ├── data/                   # Subject syllabus data
│   │   ├── CS.json            # Computer Science topics
│   │   └── ICT.json           # ICT topics
│   ├── models/                # Pydantic models (for request/response validation)
│   ├── routes/                # API endpoints
│   │   ├── generate.py        # Question generation endpoint
│   │   └── topics.py          # Topics retrieval endpoint
│   └── services/              # Business logic
│       ├── ai_service.py      # Google Gemini integration
│       ├── prompt_builder.py  # Prompt generation for AI
│       ├── getTopics.py       # Topic data loading
│       └── testing.py         # Testing utilities
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## API Endpoints

### 1. Health Check

**GET** `/`

Returns a simple message confirming the API is running.

**Response:**

```json
{
  "message": "ExamGen API is running"
}
```

### 2. Generate Questions

**POST** `/generate`

Generates exam-style questions for a specific topic.

**Request Body:**

```json
{
  "subject": "ICT",
  "topic": "Hardware and Software",
  "difficulty": "medium",
  "count": 5
}
```

**Parameters:**

- `subject` (required): Subject name (e.g., "ICT", "CS")
- `topic` (required): Specific topic within the subject
- `difficulty` (optional): Question difficulty level (e.g., "easy", "medium", "hard")
- `count` (optional): Number of questions to generate (default varies)

**Response:**

```json
{
  "questions": [
    {
      "question": "Explain the role of a device driver in a computer system.",
      "marks": 4,
      "Mark scheme": [
        "Acts as a translator between the operating system and the hardware device",
        "Allows the operating system to communicate with and control specific hardware components",
        "Converts general input/output commands from the OS into instructions the device understands",
        "Enables the hardware to function correctly without the OS needing to know the technical details of every device"
      ],
      "command word": "Explain"
    }, ...
}
```

**Error Responses:**

- `400 Bad Request`: Missing required fields (subject or topic)
- `502 Bad Gateway`: AI service returned invalid or empty response

### 3. Get Available Topics

**GET** `/topics:{filename}`

Retrieves all available topics for a given subject file.

**Parameters:**

- `filename` (required): Subject filename without extension (e.g., "ICT", "CS")

**Response:**

```json
{
  "topics": [
    "Hardware and Software",
    "Binary code",
    "Networks",
    ...
  ]
}
```

## Running the Server

1. **Development Mode**

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

2. **Production Mode**

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

3. **Access API Documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## CORS Configuration

The API is pre-configured to accept requests from:

- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (Common frontend port)

To modify CORS settings, edit the `app/main.py` file and update the `allow_origins` list.

## Environment Variables

| Variable             | Description                                    | Required |
| -------------------- | ---------------------------------------------- | -------- |
| `GEMINI_API_KEY`     | Google Gemini API key for question generation  | Yes      |
| `OPENROUTER_API_KEY` | OpenRouter API key (for alternative AI models) | No       |

## Development

### Adding New Subjects

1. Create a new JSON file in `app/data/` (e.g., `MATH.json`)
2. Structure it similar to existing subject files with topics and syllabus content
3. Use the new filename in API requests

### Modifying Prompts

Edit `app/services/prompt_builder.py` to customize how questions are generated. The prompt is designed to:

- Generate original questions (not copies of past papers)
- Match Cambridge exam style and wording
- Use authentic command words
- Follow realistic mark allocations

## Future Enhancements

- [ ] MongoDB integration for question caching and history
- [ ] User authentication and question storage
- [ ] Question difficulty calibration
- [ ] Multiple language support
- [ ] Additional subjects and exam boards
- [ ] Question validation and feedback

## License

This project is licensed under the MIT License - see the LICENSE file for details.

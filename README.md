# Interview Preparation Assistant

This has a menu with some multi-page content as a test of the format. The colors and CSS are not right yet.

## Local Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git
- Google (Gemini) API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Installation Steps

1. Clone the repository

```bash
git clone https://github.com/ashleysally00/interview-prep-app.git
cd interview-prep-app
```

2. Create and activate virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# MacOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages

First, install Streamlit and Google Generative AI dependencies directly

```bash
pip install streamlit
pip install google-generativeai
```

Next install all the other requirements from the txt file

```bash
pip install -r requirements.txt
```

4. Set up your API keys:

Create `.streamlit/secrets.toml`:

```toml
GOOGLE_API_KEY = "your-api-key-here"
```

Create `.env` in root directory:

```
GOOGLE_API_KEY=your-api-key-here
```

5. Run the application

```bash
streamlit run app.py
```

The application should open in your default web browser at `http://localhost:8501`

### Features

- **Confidence Assessment Quiz**: Evaluates your workplace confidence and provides personalized feedback
- **AI Interview Practice**: Interactive interview simulation powered by Google's Gemini AI
- **Split-Screen Interface**: Take the quiz and practice interviewing side by side
- **Instant Feedback**: Get real-time feedback on your interview responses
- **Personalized Recommendations**: Receive tailored advice based on your confidence assessment

### Project Structure

```
interview-prep-app/
├── .streamlit/
│   └── secrets.toml
├── src/
│   ├── confidence_quiz.py
│   ├── gemini_interviewer.py
│   └── utils.py
├── app.py
├── requirements.txt
└── .env
```

### Note

Make sure to never commit your API keys or secrets file to GitHub. The `.gitignore` file is configured to prevent this, but always double-check before committing changes.

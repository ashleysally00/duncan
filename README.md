# Interview Preparation Assistant

[Check out the video for our new interview prep app here!](https://www.youtube.com/watch?v=5ig7lilsb-I)

Test the app here: https://duncan-prep.streamlit.app/

Meet our new app, Empower Her - we designed Empower Her to help women in the fight for economic equality.
This app functions as both a confidence builder and a job coach. Women can use Empower Her to improve their interview skills with immediate AI-driven feedback They can take the confidence quiz and get conclusions and tips. Our aim is to help women become more confident during interviews so they can get better jobs that pay more.

Our app aligns with UN SDG 5 for gender equality. Learn more here: 
https://sdgs.un.org/goals/goal5

We created it to promote economic empowerment and leadership for women and girls. We made it by leveraging the power of Google's AI.
We built it during the Google Women Techmakers She Builds AI Hackathon. Learn more here: https://developers.google.com/womente...




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

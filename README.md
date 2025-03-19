**README.md**
```markdown
# Audio File Transcription using OpenAI Whisper

A Python script that batch processes audio files using OpenAI's Whisper API to generate text transcriptions.

## Features
- 🎧 Supports multiple audio formats (MP3, WAV, M4A, MP4, WEBM, MPEG)
- 📁 Batch processes all audio files in a directory
- 📝 Generates text files with matching filenames
- ⚙️ Secure API key management using environment variables
- 🚫 Skips already processed files

## Prerequisites
- Python 3.7+
- OpenAI API key
- Python packages: `requests`, `python-dotenv`

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/audio-transcription.git
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key:
     ```env
     API_KEY=your_openai_api_key_here
     ```

## Usage

1. **Prepare your audio files**
   - Place audio files in a folder (e.g., `audio_files`)

2. **Run the script**
   ```bash
   python transcribe.py
   ```

3. **Follow prompts**
   - Input folder path containing audio files
   - Output folder path (default: `transcriptions`)

4. **Output**
   - Text files with same base name as audio files
   - Saved in specified output folder

## Supported Audio Formats
- MP3, WAV, M4A, MP4, WEBM, MPEG
- Maximum file size: 25MB (OpenAI API limit)

## Important Notes
- 🔐 Keep your `.env` file private - never commit/share it
- 💸 API usage costs apply - check [OpenAI Pricing](https://openai.com/pricing)
- ⏳ Processing time depends on audio duration and API response

## File Structure
```
.
├── transcribe.py         # Main transcription script
├── config.py             # Configuration loader
├── .env.example          # Environment template
├── requirements.txt      # Dependencies
├── README.md             # This document
└── .gitignore            # Git exclusion rules
```

## Contributing
Contributions welcome! Please open an issue first to discuss proposed changes.
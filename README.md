# AI Thumbnail Agent 

An AI-powered YouTube thumbnail generator built with Python, Google Gemini, and Cloudflare Workers AI.

The project transforms a simple YouTube video title into three creative thumbnail concepts, generates a detailed image prompt, and produces a thumbnail using an AI image generation model.

##  Features

- **AI Concept Generation:** Generate 3 creative thumbnail concepts from a video title using Google Gemini.
- **Concept Selection:** Choose your favorite concept.
- **Prompt Engineering:** Generate a detailed image-generation prompt.
- **AI Image Generation:** Generate images using Cloudflare Workers AI and FLUX.1 Schnell.
- **Image Export:** Save the generated thumbnail as a PNG file.
- **Error Handling:** Handle invalid inputs and API errors.

##  Technologies Used

- Python
- Google Gemini API
- Cloudflare Workers AI
- FLUX.1 Schnell
- Requests
- JSON
- Base64

## 📁 Project Structure

```text
ai-thumbnail-agent/
│
├── thumbnail_agent.py
├── requirements.txt
├── .gitignore
└── README.md
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/amintaftafi395-maker/ai-thumbnail-agent.git
cd ai-thumbnail-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API credentials

You need:

- A Google Gemini API key.
- A Cloudflare account with Workers AI access.
- Your Cloudflare Account ID.
- A Cloudflare API token with the required Workers AI permissions.

Configure these environment variables:

```text
GEMINI_API_KEY
CLOUDFLARE_ACCOUNT_ID
CLOUDFLARE_API_TOKEN
```

Make sure the Gemini variable name matches the one used by your Python SDK configuration.

### 4. Run the application

```bash
python thumbnail_agent.py
```

Enter a video title, choose one of the three generated concepts, and confirm image generation.

The generated image is saved as:

```text
thumbnail.png
```

## 🔮 Future Improvements

- Build a modern web interface.
- Integrate a Python backend using Flask or FastAPI.
- Add thumbnail previews.
- Save generation history.
- Support multiple thumbnail styles.
- Improve image customization and export options.

##  Author

Created as a Python learning and AI development project.

**AI Thumbnail Agent** — Turning video ideas into visual concepts with AI.

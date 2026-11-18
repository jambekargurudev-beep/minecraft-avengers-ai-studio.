# Minecraft Avengers AI Studio V1.0

A beginner-friendly, cloud-first starter kit for planning and producing 3 Minecraft Avengers videos per week.

## What V1.0 does
- Generates episode outlines, scripts, scene lists, titles, descriptions and thumbnail concepts using a Gemini API key.
- Saves each episode as editable Markdown/JSON in `output/`.
- Includes a weekly production checklist and a YouTube upload checklist.
- Runs locally on Windows or in a cloud notebook. The app itself does not upload videos automatically.

## Free-first architecture
1. **GitHub** — store this project.
2. **Streamlit Community Cloud** — host the simple browser-based studio (free tier subject to platform limits).
3. **Google AI Studio / Gemini API** — optional script generation (free quota subject to model and region limits).
4. **Google Drive** — store generated assets and final MP4s.
5. **CapCut** — assemble scenes, voice, music and captions on iPhone/PC.
6. **YouTube Studio** — schedule three uploads weekly.

Important: free services have changing quotas and may require account verification. AI video generation, reliable unattended rendering and automatic YouTube uploads are not guaranteed free. V1.0 keeps a human review step before publishing.

## Run on Windows 11
1. Install Python 3.11+ from https://www.python.org/downloads/ and tick **Add Python to PATH**.
2. Extract this ZIP.
3. Open the project folder, click the address bar, type `cmd`, press Enter.
4. Run:
   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```
5. Open the local URL shown in the terminal.

## Run in the cloud
1. Create a GitHub repository and upload these files.
2. Open https://share.streamlit.io/ and connect GitHub.
3. Choose the repository, branch `main`, and file `app.py`.
4. Add `GEMINI_API_KEY` under **App settings → Secrets**:
   ```toml
   GEMINI_API_KEY = "paste-your-key-here"
   ```
5. Deploy. Open the app URL on iPhone or PC.

Get an API key from https://aistudio.google.com/app/apikey. Never paste your key into source code or share it in screenshots.

## First test
Run the app and press **Create sample episode**. It should create a script without an API key. Then optionally add your Gemini key in Streamlit Secrets and generate with AI.

## Weekly schedule (3 videos)
- Monday: create and approve Episode A; prepare scenes.
- Wednesday: create and approve Episode B; edit both A/B.
- Friday: create and approve Episode C; finish edits and schedule uploads.
- Publish: Tuesday, Thursday, Saturday (adjust to your audience analytics).

## Project structure
- `app.py` — Streamlit interface.
- `studio.py` — prompt and episode generation logic.
- `requirements.txt` — dependencies.
- `.streamlit/secrets.toml.example` — secret configuration example.
- `output/` — generated scripts and episode briefs.

## Safety / rights
Use original characters, dialogue, music and visuals, or assets you have permission to use. Avoid using copyrighted film/Marvel footage, logos, music or character likenesses without permission. “Minecraft” is a trademark; follow Mojang/Microsoft usage guidelines and YouTube policies. Review every AI output for accuracy, safety and quality before publishing.

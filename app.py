import json
from pathlib import Path
import streamlit as st
from studio import generate_episode

st.set_page_config(page_title="Minecraft Avengers AI Studio", page_icon="🎮", layout="wide")
st.title("🎮 Minecraft Avengers AI Studio")
st.caption("V1.0 • Cloud-first production planner • 3 videos per week")

with st.sidebar:
    st.header("Episode settings")
    season = st.number_input("Season", min_value=1, value=1, step=1)
    episode = st.number_input("Episode number", min_value=1, value=1, step=1)
    idea = st.text_input("Episode idea", placeholder="e.g. The Secret Portal")
    st.info("No API key? Use the built-in sample episode. Add GEMINI_API_KEY in Streamlit Cloud Secrets for AI generation.")

def create_episode():
    try:
        key = st.secrets.get("GEMINI_API_KEY", None)
    except Exception:
        key = None
    with st.spinner("Creating your episode..."):
        data = generate_episode(int(episode), idea, key)
    Path("output").mkdir(exist_ok=True)
    safe = "".join(c.lower() if c.isalnum() else "-" for c in data["title"]).strip("-")
    out = Path("output") / f"s{int(season)}-e{int(episode)}-{safe[:40]}.json"
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    st.session_state["episode_data"] = data
    st.session_state["episode_file"] = str(out)

if st.button("✨ Create episode", type="primary"):
    create_episode()

data = st.session_state.get("episode_data")
if data:
    st.success("Episode brief created.")
    st.subheader(data["title"])
    st.write(data["logline"])
    st.metric("Target duration", f'{data["duration_seconds"]} sec')
    st.markdown("**Opening hook**")
    st.write(data["hook"])
    st.markdown("**Narration**")
    st.write(data["narration"])
    st.markdown("**Scene plan**")
    for scene in data["scenes"]:
        with st.expander(f'Scene {scene["scene_number"]} • {scene["duration_seconds"]} sec'):
            st.write("**Visual prompt:**", scene["visual_prompt"])
            st.write("**Camera:**", scene["camera"])
            st.write("**Action:**", scene["action"])
            st.write("**Dialogue:**", scene["dialogue"])
            st.write("**Sound:**", scene["sound_design"])
    st.markdown("**Thumbnail prompt**")
    st.write(data["thumbnail_prompt"])
    st.markdown("**YouTube description**")
    st.write(data["description"])
    st.write(" ".join(data.get("hashtags", [])))
    st.markdown("**Continuity notes**")
    st.write(data["continuity_notes"])
    st.markdown("**Production checklist**")
    for item in data["production_checklist"]:
        st.checkbox(item, key=f"check-{item}")
    st.download_button("⬇️ Download episode JSON", json.dumps(data, indent=2, ensure_ascii=False), file_name="minecraft_avengers_episode.json", mime="application/json")
else:
    st.info("Start with Episode 1, then create Episodes 2 and 3 for your first weekly batch.")
    if st.button("Create sample episode"):
        create_episode()
        st.rerun()

st.divider()
st.subheader("Weekly publishing rhythm")
st.markdown("""
| Day | Task |
|---|---|
| Monday | Write and approve Episode 1 |
| Tuesday | Publish Video 1 |
| Wednesday | Produce Episode 2 |
| Thursday | Publish Video 2 |
| Friday | Produce Episode 3 and review all edits |
| Saturday | Publish Video 3 |
| Sunday | Review analytics and plan next week |
""")
st.caption("Human review is required. V1.0 prepares scripts and production briefs; it does not render or upload videos automatically.")

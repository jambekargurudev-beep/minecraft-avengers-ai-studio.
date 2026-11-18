import json
import os
import re
from datetime import date
from google import genai

CHARACTERS = """Steve: main hero, brown hair, blue eyes, blue shirt, purple pants.
Alex: smart friend, orange hair, green shirt, brown pants.
Creeper: green four-legged voxel monster; expressive but not frightening.
Herobrine: mysterious antagonist; pale glowing eyes, white eyes, restrained screen presence.
Keep character appearance consistent in every scene. Use original dialogue and story beats."""

SYSTEM_PROMPT = """You are the showrunner of Minecraft Avengers, an original family-friendly voxel animation series.
Create production-ready short episodes. Preserve continuity and character traits.
Do not copy scenes, dialogue, music, or distinctive designs from existing films or franchises.
Keep action non-graphic and suitable for a broad audience. Use clear, visual storytelling."""

def build_prompt(episode_number: int, title_seed: str = "") -> str:
    return f"""
{SYSTEM_PROMPT}

SERIES BIBLE:
{CHARACTERS}

Create Season 1 Episode {episode_number} of the series "The Secret of the Block World".
Working title / idea: {title_seed or "Continue the mystery and raise the stakes"}.
Target duration: 60-90 seconds. Target format: YouTube short-form vertical 9:16.
Return valid JSON only with these keys:
title, logline, duration_seconds, hook, narration, scenes (array of objects with
scene_number, duration_seconds, visual_prompt, camera, action, dialogue, sound_design),
thumbnail_prompt, description, hashtags, continuity_notes, production_checklist.
Make 5-7 scenes. Include a strong first 2-second hook, a clear mini-conflict,
a satisfying reveal or cliffhanger, and a simple call to action.
Avoid copyrighted music references. Suggest generic sound design only.
"""

def generate_episode(episode_number: int, title_seed: str = "", api_key: str | None = None):
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        return sample_episode(episode_number, title_seed)
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=build_prompt(episode_number, title_seed),
        config={"response_mime_type": "application/json", "temperature": 0.8},
    )
    return json.loads(response.text)

def sample_episode(episode_number: int, title_seed: str = ""):
    title = title_seed or "The Signal Beneath the Village"
    return {
        "title": f"S1E{episode_number}: {title}",
        "logline": "Steve and Alex discover a strange signal beneath the village.",
        "duration_seconds": 70,
        "hook": "The village bell rings underground—then the ground starts glowing.",
        "narration": "A signal is waking beneath the Block World. Steve and Alex must find its source before nightfall.",
        "scenes": [
            {"scene_number": 1, "duration_seconds": 8, "visual_prompt": "Voxel village at sunset; Steve and Alex look toward a glowing bell tower.", "camera": "Fast push-in", "action": "The bell rings although nobody is near it.", "dialogue": "Alex: That bell is underground!", "sound_design": "Low rumble, bright bell hit"},
            {"scene_number": 2, "duration_seconds": 10, "visual_prompt": "A glowing crack opens between block paths.", "camera": "Low tracking shot", "action": "Blue light pulses from below.", "dialogue": "Steve: Stay close. We are going down.", "sound_design": "Stone creak, rising pulse"},
            {"scene_number": 3, "duration_seconds": 12, "visual_prompt": "Steve and Alex enter a hidden redstone tunnel.", "camera": "Over-the-shoulder", "action": "A trail of redstone leads to a sealed door.", "dialogue": "Alex: Someone built this recently.", "sound_design": "Footsteps, redstone hum"},
            {"scene_number": 4, "duration_seconds": 12, "visual_prompt": "A shadow moves behind frosted glass in the door.", "camera": "Slow dolly", "action": "The door displays a symbol matching Steve's map.", "dialogue": "Steve: This was meant for us.", "sound_design": "Heartbeat-like bass pulse"},
            {"scene_number": 5, "duration_seconds": 12, "visual_prompt": "The door opens to reveal a floating cube of light.", "camera": "Wide reveal", "action": "The cube projects a map with one location blinking.", "dialogue": "Alex: The signal is coming from the old fortress!", "sound_design": "Airy shimmer"},
            {"scene_number": 6, "duration_seconds": 16, "visual_prompt": "A pair of pale eyes briefly appears in the darkness beyond the cube.", "camera": "Whip pan then close-up", "action": "The light goes out; a whisper echoes.", "dialogue": "Unknown voice: You should not have found it.", "sound_design": "Sudden silence, distant whisper, impact"},
        ],
        "thumbnail_prompt": "Steve and Alex in a glowing underground voxel tunnel, mysterious floating cube, dramatic blue lighting, clear expressive faces, no text, vertical composition.",
        "description": "Steve and Alex uncover a mysterious signal beneath the village. What is waiting at the old fortress?",
        "hashtags": ["#MinecraftAnimation", "#MinecraftStory", "#VoxelAnimation"],
        "continuity_notes": "Keep Steve's blue shirt and purple pants; Alex's green shirt and brown pants. The pale eyes appear only briefly.",
        "production_checklist": ["Approve script", "Create consistent character images", "Generate or animate scenes", "Record voice", "Add licensed/original sound", "Edit vertical video", "Review captions", "Schedule upload"]
    }

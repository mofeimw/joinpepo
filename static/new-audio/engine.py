import os
import sys
import requests

# 1. Config: API key & voice
API_KEY = "sk_23345e46f958e4108c9185e69b040cf38b789a98d4c69c5c"
VOICE_ID = "jBpfuIE2acCO8z3wKNLl"

def synthesize_and_save(text: str, out_path: str):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.75, "similarity_boost": 0.75}
    }
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    with open(out_path, "wb") as f:
        f.write(resp.content)
    print(f"✅ Wrote {out_path}")

def load_segments_by_line(filename: str):
    segments = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                segments.append(line)
    return segments

if __name__ == "__main__":
    # 2. Default to input.txt if no arg provided
    if len(sys.argv) > 2:
        print("Usage: python engine.py [input_file]")
        sys.exit(1)
    input_file = sys.argv[1] if len(sys.argv) == 2 else "input.txt"

    # 3. Read each non-blank line as its own segment
    segments = load_segments_by_line(input_file)

    # 4. Send to TTS and save 1.mp3, 2.mp3, …
    for idx, segment in enumerate(segments, start=191):
        out_file = f"{idx}.mp3"
        synthesize_and_save(segment, out_file)

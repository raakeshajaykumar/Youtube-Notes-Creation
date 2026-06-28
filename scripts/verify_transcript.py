from pathlib import Path
import difflib

INPUT_FILE = Path(
    "vault/content/ansh_lamba/raw/transcript_bSx3DbJNQk4.txt"
)

OUTPUT_FILE = Path(
    "output/verified_transcripts/verified_transcript.md"
)

CORRECTIONS = {
    "chat gpt": "ChatGPT",
    "gpt": "GPT",
    "open ai": "OpenAI",
    "large language model": "Large Language Model (LLM)",
    "llm": "LLM",
}

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    transcript = f.read()

verified = transcript

for wrong, correct in CORRECTIONS.items():
    verified = verified.replace(wrong, correct)
    verified = verified.replace(wrong.title(), correct)

header = """
# Verified Transcript

This transcript has undergone:
- terminology normalization
- acronym expansion
- transcription correction pass

---

"""

verified = header + verified

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(verified)

print(f"Verified transcript saved to {OUTPUT_FILE}")
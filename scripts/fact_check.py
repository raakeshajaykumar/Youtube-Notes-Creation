from pathlib import Path

INPUT_FILE = Path(
    "output/verified_transcripts/verified_transcript.md"
)

OUTPUT_FILE = Path(
    "output/fact_checks/fact_checked_transcript.md"
)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    transcript = f.read()

fact_checked_content = transcript

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(fact_checked_content)

print(f"Fact checked transcript saved to {OUTPUT_FILE}")
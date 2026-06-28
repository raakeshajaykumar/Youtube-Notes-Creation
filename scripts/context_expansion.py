from pathlib import Path

INPUT_FILE = "output/fact_checks/fact_checked_transcript.md"
OUTPUT_FILE = "output/chapters/context_expanded.md"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

expanded_content = f"""
# Context Expanded Version

{content}

---

## Additional Context

This section will contain additional explanations,
background information,
prerequisites,
best practices,
industry standards,
and supporting information that was not explicitly mentioned in the video.

Examples:

- What is Azure Data Factory?
- Why is ETL important?
- Difference between ETL and ELT.
- Batch vs Streaming pipelines.
- Why cloud data engineering differs from on-premise systems.
"""

Path("output/chapters").mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(expanded_content)

print(f"Context expanded file saved to {OUTPUT_FILE}")
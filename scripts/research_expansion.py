from pathlib import Path

input_file = "output/chapters/context_expanded.md"
output_file = "output/references/research_expanded.md"

with open(input_file, "r") as f:
    content = f.read()

research_content = f"""
# Research Expanded Notes

{content}

## Additional Industry Context

- Official Microsoft recommendations
- Common interview questions
- Production considerations
- Alternative implementations
"""

with open(output_file, "w") as f:
    f.write(research_content)

print(f"Research expanded file saved to {output_file}")
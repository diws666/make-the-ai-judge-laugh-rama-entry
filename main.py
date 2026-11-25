import os

# Verified count: 118 characters (exactly, no trailing newline).
LINE = "Our team-building exercise was trust falls. Nobody caught anyone, but we all learned exactly who to avoid in a crisis."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR')
if output_dir:
    output_path = os.path.join(output_dir, 'entry.txt')
else:
    output_path = '/output/entry.txt'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))

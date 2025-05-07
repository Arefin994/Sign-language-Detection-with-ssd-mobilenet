import os

labels = [
    {'name': 'Hello', 'id': 1},
    {'name': 'Yes', 'id': 2},
    {'name': 'No', 'id': 3},
    {'name': 'Thank you', 'id': 4},
    {'name': 'I love you', 'id': 5}
]

ANNOTATIONS_PATH = 'workspace/annotations/'

# Ensure the directory exists
os.makedirs(ANNOTATIONS_PATH, exist_ok=True)

with open(os.path.join(ANNOTATIONS_PATH, 'label_map.pbtxt'), 'w') as f:
    for label in labels:
        f.write('item {\n')
        f.write(f'  id: {label["id"]}\n')
        f.write(f'  name: "{label["name"]}"\n')
        f.write('}\n')
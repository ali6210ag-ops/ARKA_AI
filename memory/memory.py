import json
import os
from datetime import datetime


class ARKAMemory:
    def __init__(self):
        self.file = "data/arka_memory.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def save(self, category, content):
        memory = {
            "category": category,
            "content": content,
            "created_at": str(datetime.now())
        }

        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)

        data.append(memory)

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read(self):
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    brain_memory = ARKAMemory()

    brain_memory.save(
        "system",
        "ARKA Digital Brain memory initialized"
    )

    print(brain_memory.read())
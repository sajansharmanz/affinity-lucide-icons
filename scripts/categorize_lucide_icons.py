import os
import json
import shutil

# Paths
ICON_DIR = "./icons"
CATEGORY_OUTPUT_DIR = "./categorized-icons"

# Ensure output directory exists
os.makedirs(CATEGORY_OUTPUT_DIR, exist_ok=True)

# Loop through all icon JSON files
for file in os.listdir(ICON_DIR):
    if file.endswith(".json"):
        icon_name = file.replace(".json", "")
        json_path = os.path.join(ICON_DIR, file)
        svg_path = os.path.join(ICON_DIR, icon_name + ".svg")

        # Skip if corresponding SVG doesn't exist
        if not os.path.exists(svg_path):
            continue

        # Parse the icon JSON
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        categories = data.get("categories", [])

        # Copy the SVG to each category folder
        for category in categories:
            category_dir = os.path.join(CATEGORY_OUTPUT_DIR, category)
            os.makedirs(category_dir, exist_ok=True)

            dst_svg_path = os.path.join(category_dir, icon_name + ".svg")
            shutil.copyfile(svg_path, dst_svg_path)

print("✅ Icons have been organized into category folders.")

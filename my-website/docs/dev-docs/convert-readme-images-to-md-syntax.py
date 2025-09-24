import os
import re
import json

# Regex patterns
IMAGE_BLOCK_PATTERN = re.compile(r"\[block:image\]\s*({.*?})\s*\[/block\]", re.DOTALL)
EMBED_BLOCK_PATTERN = re.compile(r"\[block:embed\]\s*(\{.*\})\s*\[/block\]", re.DOTALL)
PARAMETERS_BLOCK_PATTERN = re.compile(r"\[block:parameters\]\s*(\{.*?\})\s*\[/block\]", re.DOTALL)
AUTOLINK_PATTERN = re.compile(r"<(https?://[^ >]+)>")

def convert_image_block(block: str) -> str:
    """Convert a [block:image] JSON block to Markdown image syntax."""
    try:
        data = json.loads(block)
        if "images" not in data:
            return ""
        md_images = []
        for img in data["images"]:
            url = img.get("image", [None])[0]
            if url:
                md_images.append(f"![]({url})")
        return "\n\n".join(md_images)
    except Exception as e:
        print(f"⚠️ Could not parse image block: {e}")
        return block  # fallback

def convert_embed_block(block: str) -> str:
    """Convert a [block:embed] JSON block into its raw iframe HTML."""
    try:
        data = json.loads(block)
        html = data.get("html", "")
        if html:
            return html.strip()
        url = data.get("url", "")
        title = data.get("title", "")
        return f"[Embed: {title or url}]"
    except Exception as e:
        print(f"⚠️ Could not parse embed block: {e}")
        return block  # fallback

def convert_parameters_block(block: str) -> str:
    """Convert a [block:parameters] JSON block into a Markdown table."""
    try:
        data = json.loads(block)
        table_data = data.get("data", {})
        cols = data.get("cols", 0)
        rows = data.get("rows", 0)

        # Headers
        headers = [table_data.get(f"h-{i}", "") for i in range(cols)]
        header_row = "| " + " | ".join(headers) + " |"
        separator_row = "| " + " | ".join([":---" for _ in headers]) + " |"

        # Rows
        body_rows = []
        for r in range(rows):
            row = [table_data.get(f"{r}-{c}", "") for c in range(cols)]
            body_rows.append("| " + " | ".join(row) + " |")

        return "\n".join([header_row, separator_row] + body_rows)

    except Exception as e:
        print(f"⚠️ Could not parse parameters block: {e}")
        return block  # fallback

def process_file(filepath: str, stats: dict):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    image_matches = IMAGE_BLOCK_PATTERN.findall(content)
    embed_matches = EMBED_BLOCK_PATTERN.findall(content)
    parameters_matches = PARAMETERS_BLOCK_PATTERN.findall(content)
    autolinks = AUTOLINK_PATTERN.findall(content)

    new_content = IMAGE_BLOCK_PATTERN.sub(lambda m: convert_image_block(m.group(1)), content)
    new_content = EMBED_BLOCK_PATTERN.sub(lambda m: convert_embed_block(m.group(1)), new_content)
    new_content = PARAMETERS_BLOCK_PATTERN.sub(lambda m: convert_parameters_block(m.group(1)), new_content)
    new_content = AUTOLINK_PATTERN.sub(lambda m: f"[{m.group(1)}]({m.group(1)})", new_content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ Updated: {filepath}")
        if image_matches:
            print(f"   • Converted {len(image_matches)} image block(s)")
            stats["images"] += len(image_matches)
        if embed_matches:
            print(f"   • Converted {len(embed_matches)} embed block(s)")
            stats["embeds"] += len(embed_matches)
        if parameters_matches:
            print(f"   • Converted {len(parameters_matches)} parameters block(s)")
            stats["parameters"] += len(parameters_matches)
        if autolinks:
            print(f"   • Fixed {len(autolinks)} autolink(s)")
            stats["autolinks"] += len(autolinks)
        stats["files_changed"] += 1
    else:
        print(f"⏭️ Skipped: {filepath} (no changes)")

    stats["files_total"] += 1

def process_folder(folder: str):
    stats = {
        "files_total": 0,
        "files_changed": 0,
        "images": 0,
        "embeds": 0,
        "parameters": 0,
        "autolinks": 0,
    }
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file), stats)

    print("\n📊 Conversion Summary:")
    print(f"   • Files processed:     {stats['files_total']}")
    print(f"   • Files updated:       {stats['files_changed']}")
    print(f"   • Image blocks:        {stats['images']} converted")
    print(f"   • Embed blocks:        {stats['embeds']} converted")
    print(f"   • Parameters blocks:   {stats['parameters']} converted")
    print(f"   • Autolinks fixed:     {stats['autolinks']} converted")

if __name__ == "__main__":
    # Run in the folder where the script is placed
    folder_path = os.path.dirname(os.path.abspath(__file__))
    process_folder(folder_path)
    print("🎉 Conversion complete.")

import os
import re

FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n.*?\n---\s*\n?", re.DOTALL)

def find_empty_docs(folder):
    empty_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                # Remove front matter if present
                content_no_front = FRONT_MATTER_PATTERN.sub("", content, count=1).strip()
                if not content_no_front:  # empty body
                    empty_files.append(path)
    return empty_files

def delete_files(files):
    for f in files:
        try:
            os.remove(f)
            print(f"🗑️ Deleted: {f}")
        except Exception as e:
            print(f"⚠️ Could not delete {f}: {e}")

def remove_empty_dirs(folder):
    removed = 0
    for root, dirs, files in os.walk(folder, topdown=False):
        for d in dirs:
            full_path = os.path.join(root, d)
            # List only non-hidden files
            visible = [f for f in os.listdir(full_path) if not f.startswith(".")]
            if not visible:  # only hidden files (or nothing)
                # Remove hidden files too, e.g., .DS_Store
                for hidden in os.listdir(full_path):
                    hidden_path = os.path.join(full_path, hidden)
                    if os.path.isfile(hidden_path):
                        os.remove(hidden_path)
                os.rmdir(full_path)
                print(f"📂 Removed empty folder: {full_path}")
                removed += 1
    return removed

if __name__ == "__main__":
    # Work in the folder where this script is located
    folder_path = os.path.dirname(os.path.abspath(__file__))

    empty_docs = find_empty_docs(folder_path)

    if empty_docs:
        print("⚠️ Found Markdown files with only front matter and no body:\n")
        for f in empty_docs:
            print(f" - {f}")

        answer = input("\nDo you want to DELETE these files permanently? (y/N): ").strip().lower()
        if answer == "y":
            delete_files(empty_docs)
        else:
            print("❌ Skipped deletion.")
    else:
        print("✅ No empty Markdown files found.")

    # Always check for empty folders
    removed_count = remove_empty_dirs(folder_path)
    if removed_count == 0:
        print("✅ No empty folders found.")

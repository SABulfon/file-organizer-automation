#!/usr/bin/env python3
import os
import shutil
import logging
from pathlib import Path

# Mapping file extensions to destination folder names
EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.txt', '.csv'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Executables': ['.exe', '.msi', '.dmg', '.deb'],
    'Code': ['.py', '.js', '.html', '.css', '.json', '.sql', '.cpp', '.java']
}

# Temporary extensions to skip (e.g. active downloads)
IGNORED_EXTENSIONS = ['.crdownload', '.tmp', '.part', '.download']

def get_target_category(file_extension):
    """
    Determines the category folder name based on the file extension.
    Returns 'Others' if the extension is not in the mapping.
    """
    ext = file_extension.lower()
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    return 'Others'


def resolve_name_collision(destination_path):
    """
    Checks if a file already exists at destination_path.
    If it exists, appends an incremental index (_1, _2, etc.) until finding a free name.
    
    :param destination_path: Path or str target destination for the file.
    :return: Path object with a safe, non-colliding destination path.
    """
    path = Path(destination_path)

    if not path.exists():
        return path

    parent = path.parent
    stem = path.stem
    suffix = path.suffix

    counter = 1

    new_path = parent/f"{stem}_{counter}{suffix}"
    while new_path.exists():
        counter +=1
        new_path = parent/f"{stem}_{counter}{suffix}"

    return new_path

def organize_directory(directory):
    target_dir = Path(directory)
    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)

    for item in target_dir.iterdir():
        if item.is_file():
            if item.suffix.lower() in IGNORED_EXTENSIONS:
                logging.info(f"Skipping temporary file: {item.name}")
                continue

            category = get_target_category(item.suffix)
            destination_dir = target_dir / category

            destination_dir.mkdir(parents=True, exist_ok=True)

            destination_path = destination_dir / item.name
            destination_path = resolve_name_collision(destination_path)

            try:
                shutil.move(item, destination_path)
                logging.info(f"Moved '{item.name}' to '{destination_path}'")
            except Exception as e:
                logging.error(f"Failed to move '{item.name}' to '{destination_path}': {e}")

def main():
    # Configuración de los logs
    log_dir = Path("reports")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        filename=log_dir / "organizer.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    print("[+] Starting directory organization...")
    organize_directory("test_downloads")
    print("[✔] Organization complete. Check 'reports/organizer.log' for details.")

if __name__ == '__main__':
    main()
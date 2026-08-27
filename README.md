# File Organizer Automation

A Python command-line automation tool designed to structure messy directories by dynamically categorizing files based on their extensions. The script handles filename collisions through auto-versioning, skips incomplete/temporary download files, and logs all operations for auditing purposes.

---

## Features

- **Dynamic File Categorization:** Groups files into predefined categories (`Images`, `Documents`, `Audio`, `Video`, `Archives`, `Executables`, `Code`, `Others`).
- **Collision Resolution:** Automatically appends incremental version tags (`file_1.ext`, `file_2.ext`) if a file with the same name already exists in the destination folder.
- **Safety Safeguards:** Skips active download files and temporary extensions (`.crdownload`, `.tmp`, `.part`, `.download`).
- **Command-Line Interface (CLI):** Powered by `argparse`, allowing users to specify custom paths or fall back to a default directory.
- **Audit Logging:** Keeps a detailed timestamped log of all file movements and skipped files in `reports/organizer.log`.

---

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SABulfon/file-organizer-automation.git](https://github.com/SABulfon/file-organizer-automation.git)
   cd file-organizer-automation

1. Run with the default directory (test_downloads):
    ```bash
    python organize.py

2. Run with a custom directory path:
    ```bash
    # Windows
    python organize.py "C:\Users\YourUsername\Downloads"

    # Linux / macOS
    python organize.py "/Users/YourUsername/Downloads"

### Display CLI Help

Run `--help` to inspect arguments and description directly in your terminal:

```bash
python organize.py --help
import datetime
from pathlib import Path

def main():
    """Append update timestamp to log file"""
    log_path = Path("update_log.txt")
    now = datetime.datetime.utcnow().isoformat()
    with log_path.open("a") as f:
        f.write(f"{now} - Updated offers\n")

if __name__ == "__main__":
    main()

import csv
from pathlib import Path
from datetime import datetime


class FeedbackReader:
    def __init__(self):
        self.data_dir = Path("data")

    def parse_timestamp(self, raw):
        formats = [
            "%Y-%m-%d %H:%M:%S",
            "%d/%m/%Y %H:%M",
            "%Y-%m-%dT%H:%M:%S",
            "%d-%m-%Y %H:%M:%S",
        ]
        value = raw.strip()
        for fmt in formats:
            try:
                return datetime.strptime(value, fmt).isoformat()
            except ValueError:
                continue
        return value

    def read_txt(self, name):
        path = self.data_dir / name
        records = []
        if not path.exists():
            return records
        with path.open("r", encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("|", 2)
                if len(parts) != 3:
                    continue
                records.append(
                    {
                        "timestamp": self.parse_timestamp(parts[0]),
                        "customer_id": parts[1].strip(),
                        "message": parts[2].strip(),
                    }
                )
        return records

    def read_csv(self, name):
        path = self.data_dir / name
        records = []
        if not path.exists():
            return records
        with path.open("r", encoding="utf-8", errors="ignore") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                records.append(
                    {
                        "timestamp": self.parse_timestamp(row["timestamp"]),
                        "customer_id": row["customer_id"].strip(),
                        "message": row["message"].strip(),
                    }
                )
        return records

    def read_all_sources(self):
        sources = ["feedback_today.txt", "chat_logs.txt", "email_feedback.csv"]
        all_records = []
        for name in sources:
            if name.endswith(".csv"):
                all_records.extend(self.read_csv(name))
            else:
                all_records.extend(self.read_txt(name))
        return all_records

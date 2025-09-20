import csv
from typing import List, Dict

class FileHandler:
    @staticmethod
    def read_csv(file_path: str) -> List[Dict]:
        try:
            with open(file_path, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [row for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def write_csv(file_path: str, data: List[Dict], fieldnames: List[str] = None):
        if fieldnames is None and data:
            fieldnames = list(data[0].keys())
        if fieldnames is None:
            fieldnames = []
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

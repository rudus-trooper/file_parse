from src.exceptions import EmptyContentError
from src.processors.base_processor import BaseProcessor


class CsvProcessor(BaseProcessor):
    """Processes CSV content - counts data rows (excludes header)."""

    def process(self, content: str) -> dict:
        # Reject empty content before doing any work
        if not content.strip():
            raise EmptyContentError()

        # Split into lines and isolate the data rows (skip header)
        lines = content.strip().splitlines()
        data_rows = [line for line in lines[1:] if line.strip()]

        return {"record_count": len(data_rows)}

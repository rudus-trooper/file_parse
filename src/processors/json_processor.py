import json

from src.exceptions import EmptyContentError, MalformedContentError
from src.processors.base_processor import BaseProcessor


class JsonProcessor(BaseProcessor):
    """Processes JSON content - expects a top-level array, returns element count."""

    def process(self, content: str) -> dict:
        # Reject empty content before attempting to parse
        if not content.strip():
            raise EmptyContentError()

        # Attempt to parse - wrap json errors into our domain exception
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            raise MalformedContentError(file_type="json")

        return {"record_count": len(data)}

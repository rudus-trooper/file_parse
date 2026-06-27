import xml.etree.ElementTree as ET

from src.exceptions import EmptyContentError, MalformedContentError
from src.processors.base_processor import BaseProcessor


class XmlProcessor(BaseProcessor):
    """Processes XML content - counts top-level child elements."""

    def process(self, content: str) -> dict:
        # Reject empty content before attempting to parse
        if not content.strip():
            raise EmptyContentError()

        # Attempt to parse - wrap XML errors into our domain exception
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            raise MalformedContentError(file_type="xml")

        return {"record_count": len(list(root))}

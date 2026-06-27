from src.exceptions import UnsupportedFileTypeError
from src.processors import CsvProcessor, JsonProcessor, XmlProcessor


class ProcessorFactory:
    """Maps file type strings to their matching processor instances."""

    # Registry - adding a new format means adding an entry here
    _processors = {
        "csv": CsvProcessor,
        "json": JsonProcessor,
        "xml": XmlProcessor,
    }

    def get_processor(self, file_type: str):
        # Look up the processor class or fail with a clear error
        processor_cls = self._processors.get(file_type.lower())
        if processor_cls is None:
            raise UnsupportedFileTypeError(file_type)
        return processor_cls()

import pytest

from src.exceptions import UnsupportedFileTypeError
from src.factory import ProcessorFactory
from src.main import process_file
from src.processors import CsvProcessor, JsonProcessor, XmlProcessor


class TestProcessorFactory:
    def test_returns_csv_processor(self):
        p = ProcessorFactory().get_processor("csv")
        assert isinstance(p, CsvProcessor)

    def test_returns_json_processor(self):
        p = ProcessorFactory().get_processor("json")
        assert isinstance(p, JsonProcessor)

    def test_returns_xml_processor(self):
        p = ProcessorFactory().get_processor("xml")
        assert isinstance(p, XmlProcessor)

    def test_case_insensitive(self):
        p = ProcessorFactory().get_processor("CSV")
        assert isinstance(p, CsvProcessor)

    def test_unsupported_type_raises(self):
        with pytest.raises(UnsupportedFileTypeError):
            ProcessorFactory().get_processor("yaml")


class TestProcessFileIntegration:
    def test_csv_integration(self):
        result = process_file("csv", "a,b\n1,2\n3,4")
        assert result == {"record_count": 2}

    def test_json_integration(self):
        result = process_file("json", '[1, 2, 3]')
        assert result == {"record_count": 3}

    def test_xml_integration(self):
        result = process_file("xml", "<r><i/><i/><i/><i/></r>")
        assert result == {"record_count": 4}

    def test_unsupported_integration(self):
        with pytest.raises(UnsupportedFileTypeError):
            process_file("yaml", "key: val")

    def test_empty_integration(self):
        with pytest.raises(Exception):
            process_file("csv", "")

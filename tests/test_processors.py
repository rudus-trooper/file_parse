import pytest

from src.exceptions import EmptyContentError, MalformedContentError
from src.processors import CsvProcessor, JsonProcessor, XmlProcessor


class TestCsvProcessor:
    # Returns record count excluding the header
    def test_valid_csv(self):
        result = CsvProcessor().process("id,name\n1,John\n2,Mary")
        assert result == {"record_count": 2}

    # Only a header means zero data rows
    def test_header_only(self):
        result = CsvProcessor().process("id,name")
        assert result == {"record_count": 0}

    def test_empty_raises(self):
        with pytest.raises(EmptyContentError):
            CsvProcessor().process("")


class TestJsonProcessor:
    def test_valid_json_array(self):
        result = JsonProcessor().process('[{"id":1},{"id":2}]')
        assert result == {"record_count": 2}

    def test_empty_array(self):
        result = JsonProcessor().process("[]")
        assert result == {"record_count": 0}

    def test_empty_raises(self):
        with pytest.raises(EmptyContentError):
            JsonProcessor().process("")

    def test_malformed_raises(self):
        with pytest.raises(MalformedContentError):
            JsonProcessor().process("{bad json}")


class TestXmlProcessor:
    def test_valid_xml(self):
        result = XmlProcessor().process("<root><item/><item/></root>")
        assert result == {"record_count": 2}

    def test_empty_root(self):
        result = XmlProcessor().process("<root></root>")
        assert result == {"record_count": 0}

    def test_empty_raises(self):
        with pytest.raises(EmptyContentError):
            XmlProcessor().process("")

    def test_malformed_raises(self):
        with pytest.raises(MalformedContentError):
            XmlProcessor().process("<root><unclosed>")

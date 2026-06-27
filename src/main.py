import json
import sys

from src.factory import ProcessorFactory


def process_file(file_type: str, file_content: str) -> dict:
    """Main entry point - pick a processor, run it, return the result."""
    factory = ProcessorFactory()
    processor = factory.get_processor(file_type)
    return processor.process(file_content)


if __name__ == "__main__":
    # CLI usage: python -m src.main csv ./data.csv
    if len(sys.argv) < 3:
        print("Usage: python -m src.main <file_type> <file_path>", file=sys.stderr)
        sys.exit(1)

    file_type = sys.argv[1]
    file_path = sys.argv[2]

    with open(file_path) as f:
        file_content = f.read()

    result = process_file(file_type, file_content)
    print(json.dumps(result))

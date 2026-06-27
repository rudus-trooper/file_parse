from src.exceptions import EmptyContentError


class BaseProcessor:
    """Base class that all file processors inherit from."""

    def process(self, content: str) -> dict:
        # Subclasses override this - raise if someone calls the base directly
        raise NotImplementedError("Subclass must implement process()")

"""Contains a Chart class containing metadata for an aeronautical chart."""

class Chart:
    """
    Represents an aeronautical chart metadata, including name, current edition,
    and next edition for this chart.
    """
    def __init__(self, name, current_edition, next_edition):
        self.name = name
        self.current_edition = current_edition
        self.next_edition = next_edition

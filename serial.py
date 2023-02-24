"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    Attributes:
    - start (int): The starting value of the serial number generator.
    - next (int): The next serial number to be generated.

    Methods:
    - __init__(self, start=0): Initializes a new SerialGenerator object with the given starting value.
    - __repr__(self): Returns a string representation of the SerialGenerator object.
    - generate(self): Generates a new serial number and returns it.
    - reset(self): Resets the serial number generator to its starting value.
    """
    def __init__(self, start=0):
         """Initializes a new SerialGenerator object with the given starting value."""
        self.start = start
        self.next = start

    def __repr__(self):
        """Returns a string representation of the SerialGenerator object."""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """Generates a new serial number and returns it."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the serial number generator to its starting value."""
        self.next = self.start
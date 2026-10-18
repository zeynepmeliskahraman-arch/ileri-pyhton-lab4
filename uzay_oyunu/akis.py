from itertools import islice, takewhile
from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayıları üreten bir üreteç."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
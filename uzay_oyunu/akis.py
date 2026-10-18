from itertools import islice, takewhile
from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayıları üreten bir üreteç."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her next() çağrısında yakıtı tüketim kadar azaltıp kalan yakıtı üreten üreteç."""
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit
        if yakit == 0:
            break

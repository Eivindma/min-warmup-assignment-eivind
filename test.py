from pathlib import Path
import sys
from typing import TextIO, Dict
from io import StringIO



def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    with open(file_name,'r') as f:
        lines = f.read().splitlines()
        # lines = f.readlines()
    return lines  # TODO: Du må erstatte denne linjen



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    with open('small.txt') as small_file:
        print(read_file(small_file))
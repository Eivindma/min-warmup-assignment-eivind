def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    with open(file_name, "r") as f:
        lines = f.readlines().splitlines()
    return lines


lines = ["dette er en test", "Denne teste er,", "god tur"]

linesto = lines.splitlines()
print(linesto)
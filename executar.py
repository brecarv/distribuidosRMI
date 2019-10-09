# This is the code that visits the warehouse.
import sys
import Pyro4
from usuario import Usuario

if sys.version_info < (3, 0):
    input = raw_input

uri = input("URI: ").strip()
acervo = Pyro4.Proxy(uri)
emerson = Usuario("Emerson")
raissa = Usuario("Raissa")
emerson.visitar(acervo)
raissa.visitar(acervo)

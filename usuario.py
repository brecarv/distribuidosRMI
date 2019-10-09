from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input


class Usuario(object):
    def __init__(self, nome):
        self.nome = nome

    def visitar(self, acervodoele):
        print("Usuario: {0}.".format(self.nome))
        self.doar(acervodoele)
        self.receberDoacao(acervodoele)
        print("Obrigado!")

    def doar(self, acervodoele):
        print("O acervo do Doele tem os seguintes livros:",
              acervodoele.list_contents())
        item = input("Digite o nome do livro que deseja doar: ").strip()
        if item:
            acervodoele.store(self.nome, item)

    def receberDoacao(self, acervodoele):
        print("O acervo do Doele tem os seguintes livros:",
              acervodoele.list_contents())
        item = input(
            "Digite o nome do livro que voce deseja receber: ").strip()
        if item:
            acervodoele.take(self.nome, item)

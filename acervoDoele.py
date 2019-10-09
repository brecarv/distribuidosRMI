from __future__ import print_function
import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class AcervoDoele(object):
    def __init__(self):
        self.contents = ["A mao esquerda de Deus", "Sherlock Holmes",
                         "Revolucao dos Bichos ", "O homem de Giz", "1984"]

    def list_contents(self):
        return self.contents

    def take(self, name, item):
        self.contents.remove(item)
        print("{0} pegou um livro: {1}.".format(name, item))

    def store(self, name, item):
        self.contents.append(item)
        print("{0} guardou um livro: {1}.".format(name, item))


def main():
    Pyro4.Daemon.serveSimple(
        {
            AcervoDoele: "exemplo.acervodoele"
        },
        ns=False)


if __name__ == "__main__":
    main()

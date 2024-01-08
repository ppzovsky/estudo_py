def saudacao(nome='', idade=20):
    print(f'bom dia {nome}, voce tem {idade} anos?')


print(__name__)


def soma(a, b, x):
    return a+b*x


if __name__ == '__main__':
    saudacao('felipe', 45)

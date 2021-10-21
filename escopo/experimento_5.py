
def main():
    x = 10

    def minha_funcao():
        y = 7
        print('ola mundo!')
        print('Estou acessando a variável x da função main, de dentro da minha_funcao, e seu valor é %d' % x)
        print('a variável y da função minha_funcao tem valor %d' % y)

    minha_funcao()
    print('Estou acessando a variável x da função main, e seu valor é %d' % x)
    print('a variável y da função minha_funcao tem valor %d' % y)


if __name__ == '__main__':
    main()

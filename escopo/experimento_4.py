
def main():
    x = 10

    def minha_funcao():
        print('ola mundo!')
        print('Estou acessando a variável x da função main, de dentro da minha_funcao, e seu valor é %d' % x)

    minha_funcao()
    print('Estou acessando a variável x da função main, e seu valor é %d' % x)


if __name__ == '__main__':
    main()

import random


def main():
    num = random.randint(0, 10)
    if num < 5:
        texto = 'menor que 5'

    print('num é', texto)


if __name__ == '__main__':
    main()

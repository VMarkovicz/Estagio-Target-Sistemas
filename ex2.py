#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
#seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def main():
    string = input('Digite uma palavra: ')
    find_letter(string)

def find_letter(string):
    string = string.lower()
    count = 0
    for caracter in string:
        if caracter == 'a':
            count += 1

    print(f'A palavra possui a letra A {count} vezes')

if __name__ == '__main__':
    main()
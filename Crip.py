tamanho_max = 26

def recebeModo():
    while True:
        modo = input('Você deseja criptografar ou decriptografar? \n').lower()
        if modo in 'criptografar c decriptografar d'.split() :
            return modo
        else:
            print('Entre "criptotografar" ou "c" ou "decriptografar" ou "d" .')

def recebeChave():
    global tamanho_max 
    chave = 0
    while True:
        chave = int(input(f'Entre com o número da chave (1-{tamanho_max}): '))
        if 1 <= chave <= tamanho_max:
            return chave

def geraMsgTraduzida(modo, mensagem, chave):
    if modo[0] == 'd':
        chave *= -1
    traduzido = ''
    for simbolo in mensagem :
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z') :
                    num -= 26
                elif num < ord('a') :
                    num += 26
            traduzido += chr(num)
        else :
            traduzido += simbolo
    return traduzido

def main():
    modo = recebeModo()
    mensagem = input('Entre com sua mensagem \n')
    chave = recebeChave()
    print('Seu texto traduzido é: ')
    print(geraMsgTraduzida(modo, mensagem, chave))

main()

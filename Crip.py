def recebeModo():
    while True:
        modo = input('Você deseja criptografa ou decriptografa? \n').lower()
        if modo in 'criptografar c decriptografar d'.split() :
            return modo
        else:
            print('Entre "criptotografar" ou "c" ou "decriptografar" ou "d" .')

def recebeChave():
    global tamanho_max 
    chave = 0
    while True:
        chave = int(input(f'Entre com o número da chave {tamanho_max}'))
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
                
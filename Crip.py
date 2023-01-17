def recebeModo():
    while True:
        modo = input('Você deseja criptografa ou decriptografa? \n').lower()
        if modo in 'criptografar c decriptografar d'.split() :
            return modo
        else:
            print('Entre "criptotografar" ou "c" ou "decriptografar" ou "d" .')
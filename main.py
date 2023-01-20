tamanho_max = 26

def recebeModo():
    while True :
        print('Seja bem-vindo')
        modo = input('Deseja [c]riptografar ou [d]escriptografar ? : ').lower()
        if modo in 'criptografar c descriptografar d'.split():
            return modo
        else :
            print('Digite apenas "criptografar" ou "c" ou "descriptografar" ou "d" .')
        continue
def recebeChave():
    """
    Função que pede o valor da chave para o usuário
    e devolve a chave caso o valor desta esteja adequado
    """
    global tamanho_max
    chave = 0
    while True :
        try:
            chave = int(input(f'Digite o número da chave (1-{tamanho_max}): '))
            if 1 <= chave <= tamanho_max :
                return chave
        except:
            print('Por favor escolha uma chave de 1 a 26. ')
            continue

def msgTraduzida(modo, mensagem, chave) :
    if modo[0] == 'd' :
        chave *= -1
    traduzido = ''
    
    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave
            if simbolo.isupper():
                if num > ord('Z') :
                    num -= 26
                elif num < ord('A'):
                    num += 26
            if simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduzido += chr(num)
        else :
            traduzido += simbolo
    return traduzido
 
def main():
    modo = recebeModo()
    mensagem= input('Digite sua mensagem \n')
    chave = recebeChave()
    print(msgTraduzida(modo, mensagem, chave))

main()

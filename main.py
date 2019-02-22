import sys
import time
import twitterCredentials as tt


consumer_key = ''
consumer_secret = ''
acess_token = ''
acess_token_secret = ''

twitter = tt.Twitter(consumer_key, consumer_secret, acess_token, acess_token_secret)

def write(msg):
    for letter in msg:
        time.sleep(0.05)
        sys.stdout.write(letter)
        sys.stdout.flush()


def main():
    isRunning = True
    write('Bem vindo!!!\nPara encerrar a execução escreva: "sair".\n')
    while isRunning:
        print('''
                MENU --\n
                DIGITE 1 - TWEETAR\n
                DIGITE 2 - PESQUISAR
              ''')
        user_input = input('> ')
        if user_input == 'sair':
            isRunning = False
        elif user_input == '1':
            write('Por favor, digite sua atualização de status: \n')
            user_input = input('> ')
            twitter.request_POST(str(user_input))
        elif user_input == '2':
            write('Streaming? [Y/N]\n')
            choice = input('> ')
            write('Por favor, digite uma palavra chave: \n')
            user_input = input('> ')
            twitter.search_TWEET(str(user_input), str(choice))

if __name__ == '__main__': main()

    
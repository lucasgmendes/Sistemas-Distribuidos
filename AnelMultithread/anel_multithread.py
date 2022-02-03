import threading
import time
import string
import random

class myThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.next = None
        self.message = str()
        self.finished = False
        self.token = False

    def setNext(self, next):
        self.next = next

    def run(self):
        print(f'Starting Thread {self.id}...')

        while True:
            if self.finished == True:
                print(f'Killing Thread {self.id}')
                break

            if self.token == True:
                found = False
                for i in range(0, len(self.message)):
                    if self.message[i].islower():
                        found = True
                        
                        self.message = self.message[:i] + self.message[i].upper() + self.message[i+1:]
                        self.next.message = self.message
                        
                        self.token = False
                        print(f'Thread {self.id}: {self.message}')
                        
                        time.sleep(1)
                        self.next.token = True
                        break

                #Todos os caracteres ja sao maiusculos
                if found == False:
                    self.token = False
                    self.next.message = self.message
                    self.next.finished = True
                    print(f'Final Message: {self.message}')
        
        #Finalizando o processamento
        self.next.finished = True


class startRing:
    def __init__(self, N):
        self.threads = list()

        # Criacao da lista de Threads
        for i in range(0,N):
            self.threads.append(myThread(i))

        # Interligacao para formar o anel
        for i in range(0, N-1):
            self.threads[i].setNext(self.threads[i+1])
        self.threads[N-1].setNext(self.threads[0])
    
    # Inicialiacao das Threads
    def start_threads(self, message):
        for thread in self.threads:
            thread.start()

        self.threads[0].message = message
        self.threads[0].token = True


if __name__ == "__main__":

    threadRing = startRing(10)

    while(True):
        op = int(input('Escolha a opcao desejada:\n1 - Gerar Mensagem Aleatória\n2 - Inserir Mensagem\n'))
        if op == 1:
            n = int(input('Tamanho da mensagem: '))
            length_of_string = n
            
            message = (''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(length_of_string)))
            break
        
        elif op == 2:
            message = input('Mensagem:\n')
            break
        else:
            print('Opcao invalida!\n')
    
    threadRing.start_threads(message)
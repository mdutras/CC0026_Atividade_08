from threading import Semaphore, Thread
from time import sleep
from random import randint

semaforo = Semaphore(3)

def atender(i):
    semaforo.acquire()
    print(f"Atendendo cliente com senha {i}")
    sleep(randint(3,10))
    semaforo.release()

def main():
    for i in range(30):
        t = Thread(target=atender, args=(i,))
        t.start()

if __name__ == "__main__":
    main()

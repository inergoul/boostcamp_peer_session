import math
import time
from threading import Thread
from multiprocessing import Process, Manager
import sys

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def makePrimeList(start, end, res):
    for j in range(start, end):
        if isPrime(j):
            res.append(j)
    return


if __name__ == "__main__":
    
    t1 = time.time()
    START, END = 2, 2000000
    prime_list = Manager().list()

    process1 = Process(target=makePrimeList, args=(START, END//4, prime_list))
    process2 = Process(target=makePrimeList, args=(END//4, END//4 * 2, prime_list))
    process3 = Process(target=makePrimeList, args=(END//4 * 2, END//4 * 3, prime_list))
    process4 = Process(target=makePrimeList, args=(END//4 * 3, END, prime_list))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    
    sys.stdout = open('prime number_multi_process.txt', 'w')
    print(prime_list)
    print(len(prime_list))

    t2 = time.time()

    print(f'elapsed time : {t2-t1:.4f}(sec)')

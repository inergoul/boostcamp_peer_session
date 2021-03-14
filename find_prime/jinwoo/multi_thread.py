import math
import time
from threading import Thread
import sys

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def makePrimeList(id, start, end, res):
    for j in range(start, end):
        if isPrime(j):
            res.append(j)
    return


if __name__ == "__main__":
    
    START, END = 2, 2000000
    prime_list = list()

    t1 = time.time()
    th1 = Thread(target=makePrimeList, args=(1, START, END//4, prime_list))
    th2 = Thread(target=makePrimeList, args=(2, END//4, END//4 * 2, prime_list))
    th3 = Thread(target=makePrimeList, args=(3, END//4 * 2, END//4 * 3, prime_list))
    th4 = Thread(target=makePrimeList, args=(4, END//4 * 3, END, prime_list))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()

    sys.stdout = open('prime number_multi_thread.txt', 'w')
    print(prime_list)
    print(len(prime_list))

    t2 = time.time()
    print(f'elapsed time : {t2-t1:.4f}(sec)')

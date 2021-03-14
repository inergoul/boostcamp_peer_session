import math
import time
import sys
from threading import Thread

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def makePrimeList(id, start, end, res):
    # cnt = 0
    for j in range(start, end+1):
        if isPrime(j):
            res.append(j)
            # cnt += 1
    return


if __name__ == "__main__":
    
    START, END = 2, 2000000
    prime_list = []
    t1 = time.time()

    th1 = Thread(target=makePrimeList, args=(1, START, END, prime_list))
    th1.start()
    th1.join()
    
    sys.stdout = open('prime number_single_thread.txt', 'w')
    print(prime_list)
    print(len(prime_list))

    t2 = time.time()
    print(f'elapsed time : {t2-t1:.4f}(sec)')

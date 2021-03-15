### 소수 리스트 구하기로 구현해본 multi-process, multi-thread



##### 파일 요약

총 네 개의 파이썬 파일로 실험하였으며 각각의 해당하는 결과는 .txt file로 정리

1. prime_list.py : thread / process 개념을 사용하지 않고 구현 ==> prime_num.txt

2. single_thread.py : single_thread로 구현 ==> prime_num_single_thread.txt

3. multi_thread.py : multi_thread 로 구현 ==> prime_num_multi_thread.txt

4. multi_process.py : multi_process 로 구현 ==> prime_num_multi_process.txt



##### 실험 조건

> computing power

![](https://user-images.githubusercontent.com/43771580/111176198-76646880-85ec-11eb-8463-107f3ce1d2f6.png)

thread와 process의 개수는 core 개수인 4개로 정하였으며

1부터 n까지의 소수 구하기에서 n이 100,000 이하인 경우 걸리는 시간이 1초 근방으로

시간의 차이를 확인하기에 부족함이 있어 n을 2,000,000으로 설정



##### Code

> 공통 코드

```python
# 소수 판별 함수
def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
```

```python
# 소수이면 list에 추가
def makePrimeList(id, start, end, res):
    for j in range(start, end+1):
        if isPrime(j):
            res.append(j)
    return
```

```python
# 메인 및 출력
if __name__ == "__main__":
    
    START, END = 2, 2000000
    prime_list = []
    t1 = time.time()
	
    ''' 1번
    makePrimeList(1, START, END, prime_list)
    '''
    
    sys.stdout = open('prime number.txt', 'w')
    print(prime_list)
    print(len(prime_list))

    t2 = time.time()
    print(f'elapsed time : {t2-t1:.4f}(sec)')
```



> thread 및 process 구현 코드

```python
# 2번 single thread
from threading import Thread
	th1 = Thread(target=makePrimeList, args=(1, START, END, prime_list))
    th1.start()
    th1.join()
```

```python
# 3번 multi thread  
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
```

```python
from multiprocessing import Process, Manager
# 4번 multi process
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
```



##### 결과

- 1번 : 35.0103(sec)
- 2번 : 39.7584(sec)
- 3번 : 76.4899(sec)
- 4번 : 30.1433(sec)

여러 번 반복 실험을 했을 때에도 시간의 편차는 꽤 크지만 4번의 경우가 가장 시간이 적게 걸리는 것을 확인할 수 있었다.(단 n이 충분히 큰 경우에만) 파이썬의 GIL 문제로 인하여 multi-thread(3번)는 병렬 연산을 제대로 수행하지 못하고 유독 시간이 오래 걸렸다. txt 파일을 열어보면 4번의 경우에 4개의 영역에서 뒤섞여서 list에 추가된 것을 볼 수 있는데 파이썬에서는 multi-process가 병렬 연산을 수행하는 기능을 담당하고 있음을 알 수 있다. 아래 그림은 코드 실행 중 CPU 사용량이다.

> single thread

![](https://user-images.githubusercontent.com/43771580/111174147-8bd89300-85ea-11eb-89ed-5008f8a4bbeb.png)

> multi thread

![](https://user-images.githubusercontent.com/43771580/111174408-bf1b2200-85ea-11eb-9d8f-a031d80ed54a.png)

> multi process

![](https://user-images.githubusercontent.com/43771580/111174382-baef0480-85ea-11eb-9633-8bf18f8e44c8.png)

확실히 multi process가 CPU 사용량이 압도적임을 확인할 수 있다.
import re 
from collections import Counter

def solution(s):
    answer = []
    counter = Counter(re.sub('[{}]','',s).split(','))
    sorted_counter = sorted(counter.items(), key=lambda item:-item[1])
    answer = [int(i) for i, j in sorted_counter]
    
    return answer
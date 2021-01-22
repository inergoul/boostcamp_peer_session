from solution_jinwoo import solution
#####^- 이자리에 자기 파일명

def test(case):
    for i in range(len(case)):
        c = testcase[i]
        parameter = c[0]
        result = c[1]
        print(f'{i+1}번째 테스트 실행 결과 : {solution(*parameter) == result}')

# programmers test case
testcase = []
testcase += [[[2,10,[7,4,5,6]], 8]]
testcase += [[[100,100,[10]], 101]]
testcase += [[[100,100,[10,10,10,10,10,10,10,10,10,10]], 110]]

# test case 추가
#testcase += [["인풋 리스트"], '여기 리턴']]


if __name__ == "__main__":
    test(testcase)
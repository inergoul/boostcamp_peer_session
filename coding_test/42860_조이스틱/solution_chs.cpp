#include <string>
#include <queue>
#include <algorithm>
using namespace std;

int solution(string name) {
	int answer = 0;

	deque<int> not_A_idx;
	for (int i = 0; i < name.size(); i++) {   //바꿀 인덱스 저장
		if (name[i] != 'A')
			not_A_idx.push_back(i);
	}

	if (not_A_idx[0] == 0) {  // 처음값을 바꿔야하면
		answer += min(name[0] - 'A', 26 - (name[0] - 'A'));
		not_A_idx.pop_front();
	}

	int cnt;
	int cur_i=0;
	while (!not_A_idx.empty()) {        //바꿀게 없을때 까지
		// 방향 계산
		int front = cur_i < not_A_idx.front() ? not_A_idx.front() - cur_i : name.size() - cur_i + not_A_idx.front();
		int back = cur_i < not_A_idx.back() ? name.size() - not_A_idx.back() + cur_i : cur_i - not_A_idx.back();

		if (front <= back) { //오른쪽으로 가는게 작을때
			answer += front;
			cur_i = not_A_idx.front();
			not_A_idx.pop_front();
		}
		else { // 왼쪽으로 가는게 작을때
			answer += back;
			cur_i = not_A_idx.back();
			not_A_idx.pop_back();
		}
		cnt = min(name[cur_i] - 'A', 26 - (name[cur_i] - 'A')); //위 아래 카운트
		answer += cnt;
	}
	
	return answer;
}
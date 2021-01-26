#include <string>
using namespace std;

int solution(string s) {
	int answer = s.size();

	if (s.size() == 1)
		return 1;

	for (int i = 1; i <= s.size() / 2; i++) { //비교 갯수 지정
		int cnt = 1;
		string f = s.substr(0, i);
		string cmp, new_string;

		for (int j = i; j < s.size(); j += i) { //처음부터 쭉 비교하기
			cmp = s.substr(j, i);

			if (!(f.compare(cmp)))  //비교 문자가 같으면 cnt 증가
				cnt++;
			else {
				if (cnt == 1) {
					new_string += f;
					f = cmp;
				}
				else {
					new_string = new_string + to_string(cnt) + f;
					f = cmp;
					cnt = 1;
				}
			}

			if (j + i >= s.size()) {  //마지막에 substr기준을 초과한 경우
				if (cnt != 1) {
					new_string = new_string + to_string(cnt) + f;
					break;
				}
				else {
					new_string = new_string + s.substr(j);
					break;
				}
			}
		}
		answer = (answer > new_string.size()) ? new_string.size() : answer;
	}

	return answer;
}
#include <string>
using namespace std;

string solution(string p) {
	string answer = "";
	string u, v;

	if (p.empty()) {   // 1번조건
		return "";
	}

	int left_count = 0, right_count = 0;   //2번 조건
	for (int i = 0; i < p.size(); i++) {
		if (p[i] == '(') left_count++;
		else right_count++;

		if (left_count == right_count) {   
			u = p.substr(0, i + 1);
			v = p.substr(i + 1, p.size() - i);
			break;
		}
	}


	for (int i = 0; i < u.size(); i++) {  //3번 조건  
		if (right_count < left_count)     // 올바른 괄호 문자열 검사
			break;						

		if (u[i] == ')') right_count--;
		else left_count--;
	}

	if (right_count == left_count) {  // 3-1 조건
		u += solution(v);
		return u;
	}
	else {									 //4번조건
		answer = "(" + solution(v) + ")";
		u.erase(u.begin());
		u.erase(u.end() - 1);

		for (int i = 0; i < u.size(); i++) {
			if (u[i] == '(') u[i] = ')';
			else u[i] = '(';
		}
		answer += u;
		return answer;
	}
}
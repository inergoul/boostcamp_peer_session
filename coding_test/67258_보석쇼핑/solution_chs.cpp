#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

map<string, int> m;

vector<int> solution(vector<string> gems) {
	vector<int> answer;
	int start = 0, end = 0;
	int min = 100000, min_start, min_end;
	for (string s : gems) {  // 보석 종류 구하기
		m[s]++;
	}

	int kinds = m.size();
	m.clear();


	for (int i = 0; i < gems.size(); i++) {
		end = i;
		m[gems[i]]++;

		if (m.size() == kinds) {               //구간안에 모든 보석을 담았을 때
			while (m.size() == kinds) {			//앞에서부터 하나씩 지워나감
				m[gems[start]]--;
				if (m[gems[start]] <= 0) {
					m.erase(gems[start]);
				}
				start++;
			}
			if (min > end - start - 1) {	
				min = end - start - 1;
				min_start = start - 1;
				min_end = end;
			}
		}
	}

	answer.push_back(min_start + 1);
	answer.push_back(min_end + 1);


	return answer;
}
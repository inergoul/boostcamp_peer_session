#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;

	vector<int> distribution;
	int day;
	for (int i = 0; i < progresses.size(); i++) {
		day = (100 - progresses[i]) / speeds[i];
		if ((100 - progresses[i]) % speeds[i] != 0)
			day++;
		distribution.push_back(day);
	}

	vector<int>::iterator it = distribution.begin();

	int max_day = distribution[0];
	int cnt = 0;
	while (it != distribution.end()) {
		if (max_day < *it) {
			answer.push_back(cnt);
			cnt = 0;
			max_day = *it;
		}
		cnt++;
		it++;
	}
	answer.push_back(cnt);

	return answer;
}
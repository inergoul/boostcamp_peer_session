#include <vector>
#include<algorithm>
using namespace std;

vector<int> solution(vector<int> answers) {
	vector<int> answer;

	vector<int> one{ 1,2,3,4,5 };
	vector<int> two{ 2,1,2,3,2,4,2,5 };
	vector<int> three{3,3,1,1,2,2,4,4,5,5};

	vector<int> ans(3);
	for (int i = 0; i < answers.size(); i++) {
		if (one[i % 5] == answers[i])
			ans[0]++;
		if (two[i % 8] == answers[i])
			ans[1]++;
		if (three[i % 10] == answers[i])
			ans[2]++;
	}

	int max_value = *max_element(ans.begin(),ans.end());
	
	for (int i = 0; i < 3; i++) {
		if (ans[i] == max_value)
			answer.push_back(i+1);
	}
	return answer;
}

int main() {
	vector<int>answer{ 1,2,3,4,5 };
	solution(answer);
	return 0;
}
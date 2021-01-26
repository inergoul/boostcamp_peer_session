#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int solution(vector<int> citations) {
	int answer = 0;

	sort(citations.begin(), citations.end(), greater<int>());
    
    int i;
	for (i = 0; i < citations.size(); i++) {
		if (citations[i] <= i) {
			answer = i;
			break;
		}
	}
    if (i==citations.size()) answer = i;
	return answer;
}
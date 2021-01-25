#include <vector>
#include<iostream>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;

	vector<int> students(n+2, 1);

	for (int i = 0; i < lost.size(); i++)
		students[lost[i]]--;
	for (int i = 0; i < reserve.size(); i++)
		students[reserve[i]]++;

	for (int i = 1; i < n+1; i++) {
		if (students[i] == 0) {
			if (students[i - 1] == 2) {
				students[i - 1]--; students[i]++;
			}
			else if (students[i + 1] == 2) {
				students[i + 1]--; students[i]++;
			}
		}
	}

	for (int i = 0; i < students.size(); i++) {
		if (students[i] == 0) n--;
	}

	answer = n;

	return answer;
}
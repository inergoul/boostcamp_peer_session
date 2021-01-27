#include <string>
#include <vector>
#include<iostream>
using namespace std;

long long solution(string expression) {
	long long answer = 0;

	vector<char> op;
	vector<long long> num;
	vector<string> cases{ "+-*", "+*-","-+*",
		"-*+","*+-","*-+" };

	int idx = 0;
	int number;
	for (int i = 0; i < expression.size(); i++) {
		if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
			op.push_back(expression[i]);
			number = stoi(expression.substr(idx, i));
			num.push_back(number);
			idx = i + 1;
		}
	}
	num.push_back(stoi(expression.substr(idx)));

	for (int i = 0; i < 6; i++) {
		vector<char> op_tmp = op;
		vector<long long> num_tmp = num;

		for (int j = 0; j < 3; j++) {

			for (int k = 0; k < op_tmp.size(); k++) {
				long long new_num;
				if (op_tmp[k] == cases[i][j]) {

					if (op_tmp[k] == '+') {
						new_num = num_tmp[k] + num_tmp[k + 1];
					}
					else if (op_tmp[k] == '-') {
						new_num = num_tmp[k] - num_tmp[k + 1];
					}
					else {
						new_num = num_tmp[k] * num_tmp[k + 1];
					}

					op_tmp.erase(op_tmp.begin() + k);
					num_tmp.erase(num_tmp.begin() + k, num_tmp.begin() + k + 2);
					num_tmp.insert(num_tmp.begin() + k, new_num);
					k--;
				}
			}
		}
		answer = answer < abs(num_tmp[0]) ? abs(num_tmp[0]) : answer;
	}

	return answer;
}
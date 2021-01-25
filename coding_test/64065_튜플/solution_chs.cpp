#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

vector<int> solution(string s) {
    vector<int> st(100001,0);
	vector<int> answer;
    
	string tmp;
	for (int i = 0; i<s.size(); i++) {
		if (s[i] - '0' >= 0 && s[i] - '0' <= 9) {
			tmp += s[i];
		}
		else {
			if (tmp.size())
				st[stoi(tmp)]++, tmp.clear();
		}
	}
	vector<pair<int, int>> v;
	for (int i = 0; i <100001; i++)
		if (st[i] != 0)
			v.push_back(make_pair(st[i], i ));

	sort(v.begin(), v.end(), greater<pair<int,int>>());
	for (int i=0;i<v.size();i++) 
        answer.push_back(v[i].second);
	return answer;
}
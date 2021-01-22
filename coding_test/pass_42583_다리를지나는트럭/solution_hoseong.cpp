#include<vector>
#include<queue>
using namespaces std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;

	queue<pair<int, int>> bridge;
	
	int time = 0;

	while (!truck_weights.empty()) {

		if (weight - truck_weights[0] >= 0) {
			bridge.push(make_pair(truck_weights[0], time + 1));
			weight -= truck_weights[0];
			truck_weights.erase(truck_weights.begin());
		}

		time++;

		if (time - bridge.front().second +1 == bridge_length) {
			weight += bridge.front().first;
			bridge.pop();
		}
	}

	answer = bridge.back().second + bridge_length;
	return answer;
}
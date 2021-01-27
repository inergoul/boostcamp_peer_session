#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
	int answer = 0;
	int pick;

	vector<vector<int>> new_board;
	
	for (int i = 0; i < board.size(); i++) {
		vector<int> x;
		for (int j = board[i].size() - 1; j >= 0; j--) {
			x.push_back(board[j][i]);
		}
		new_board.push_back(x);
	}

	vector<int> bucket;

	for (int i = 0; i < moves.size(); i++) {
		pick = moves[i]-1;

		if (new_board[pick].size() == 0) 
			continue;
		
		while (!new_board[pick].back()) {
			new_board[pick].pop_back();
		}

		if (!new_board[pick].empty()) {
			bucket.push_back(new_board[pick].back());
			new_board[pick].pop_back();
		}
		else
			continue;

		if (i != 0 && bucket.size() > 1 && bucket.back() == bucket.at(bucket.size() - 2)) {
			bucket.pop_back();
			bucket.pop_back();
			answer = answer + 2;
		}

	}

	return answer;
}
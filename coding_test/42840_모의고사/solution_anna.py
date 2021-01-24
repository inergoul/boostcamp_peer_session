#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> answers) {
    int m = 0;
    int hit[3] = {0, };
    int two[] = {2, 1, 2, 3, 2, 4, 2, 5};
    int thr[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    vector<int> answer;
    for(int i = 0; i < answers.size(); i++){
        hit[0] += (((i % 5) + 1) == answers[i]);
        hit[1] += ((two[i % (sizeof(two) / sizeof(two[0]))]) == answers[i]);
        hit[2] += ((thr[i % (sizeof(thr) / sizeof(thr[0]))]) == answers[i]);
        m = max(hit[0], max(hit[1], hit[2]));
    }
    for(int i = 0; i < 3; i++){
        if(hit[i] == m){
            answer.push_back(i + 1);
        }
    }
    return answer;
}

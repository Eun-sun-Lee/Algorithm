#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int w, u, v;
};

vector<int> parent;

// 부모 초기화
void init(int n) {
    parent.resize(n + 1);
    for (int i = 1; i <= n; ++i)
        parent[i] = i;
}

// 루트 찾기 (경로 압축)
int find(int i) {
    if (parent[i] == i) return i;
    return parent[i] = find(parent[i]);
}

// 두 노드 병합
void merge(int i, int j) {
    int ii = find(i);
    int jj = find(j);
    if (ii != jj)
        parent[ii] = jj;
}

int solution(int n, vector<vector<int>> costs) {
    vector<Edge> graph;
    vector<int> answer;
    int ans = 0;

    // 그래프 구성
    for (auto &c : costs)
        graph.push_back({c[2], c[0], c[1]});

    // 간선 가중치 기준 정렬
    sort(graph.begin(), graph.end(), [](Edge &a, Edge &b) {
        return a.w < b.w;
    });

    init(n);

    // 크루스칼 알고리즘
    for (auto &e : graph) {
        int p = find(e.u);
        int q = find(e.v);
        if (p != q) {
            merge(p, q);
            answer.push_back(e.w);
        }
    }

    // 결과 계산
    for (int i = 0; i < n - 1 && i < (int)answer.size(); ++i)
        ans += answer[i];

    // 디버깅용 출력
    cout << "Edges in MST (weights): ";
    for (auto w : answer) cout << w << " ";
    cout << "\nTotal cost: " << ans << endl;

    return ans;
}

// 테스트용 main
int main() {
    int n = 4;
    vector<vector<int>> costs = {
        {0, 1, 1},
        {0, 2, 2},
        {1, 2, 5},
        {1, 3, 1},
        {2, 3, 8}
    };

//     int result = solution(n, costs);
//     cout << "Result: " << result << endl;
    return 0;
}

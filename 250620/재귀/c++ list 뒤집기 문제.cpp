#include <iostream>
#include <vector>
using namespace std;

// 재귀 함수 정의
vector<int> reverse(const vector<int>& vec) {
    if (vec.size() <= 1) {
        return vec;
    }

    // 마지막 원소만 추출
    vector<int> last = { vec.back() };

    // 마지막 원소 제외한 앞부분 재귀 호출
    vector<int> rest(vec.begin(), vec.end() - 1);
    vector<int> reversed_rest = reverse(rest);

    // 두 벡터 이어 붙이기
    last.insert(last.end(), reversed_rest.begin(), reversed_rest.end());
    return last;
}

int main() {
    vector<int> my_list = {5, 2, 7, 1, 4};
    vector<int> reversed = reverse(my_list);

    // 결과 출력
    for (int num : reversed) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}


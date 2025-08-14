#include <iostream>
#include <cmath>   //ceil, round, floor
#include <iomanip> //fixed, setprecision
using namespace std;

int main() {
    int N;
    cin >> N;

    double sum { 0.0 };

    double arr[6];
    for(int i{0};i < N;i++){
        cin >> arr[i];
        sum += arr[i];
    }
    double avg = sum / (double) N;
    cout << round(avg * 10) /  10.0 << "\n";

    // 평균 소수 첫째 자리까지 출력 (반올림)
    //cout << fixed << setprecision(1) << avg << "\n"; 


    //소수점 아래를 자름, floor
    int res = static_cast<int>(avg);
    
    string eval;
    switch(res) {
        case 4: eval = "Perfect";
        break;

        case 3: eval = "Good";
        break;
        
        default: eval = "Poor";
    }
    cout << eval << "\n";
    return 0;
}

// double d = 3.14159;
// int i = static_cast<int>(d); // 소수점 이하 버림

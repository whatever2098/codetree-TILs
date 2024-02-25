#include <iostream>
using namespace std;

bool isLeapYear(int y){
    return (y % 4 == 0)? (y % 100 == 0 && y % 400 != 0)? false : true : false;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int y;
    cin >> y;
    cout << ((isLeapYear(y))? "true" : "false") << "\n";
    return 0;
}
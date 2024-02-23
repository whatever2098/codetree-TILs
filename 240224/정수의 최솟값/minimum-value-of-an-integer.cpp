#include <iostream>
using namespace std;

int minimum(int a, int b, int c){
    int min = a;
    if(b < min){ min = b; }
    if(c < min){ min = c; }
    return min;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c;
    cin >> a >> b >> c;
    cout << minimum(a, b, c);
    return 0;
}
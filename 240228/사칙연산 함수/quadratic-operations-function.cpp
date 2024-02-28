#include <iostream>
using namespace std;

int pl(int a, int c){
    return a + c;
}
int mi(int a, int c){
    return a - c;
}
int divide(int a, int c){
    return a / c;
}
int multiple(int a, int c){
    return a * c;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, c;
    char o;
    cin >> a >> o >> c;
    int res;
    switch(o){
        case '+': res = pl(a, c); break;
        case '-': res = mi(a, c); break;
        case '/': res = divide(a, c); break;
        case '*': res = multiple(a, c); break;
        default: cout << "False" << "\n"; return 0;
    }
    cout << a << ' ' << o << ' ' << c << " = " << res << "\n";
    return 0;
}
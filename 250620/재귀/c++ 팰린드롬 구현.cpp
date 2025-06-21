#include <iostream>
#include <string>
using namespace std;

bool is_palindrome_helper(const string& s, int left, int right) {
    if (left >= right) return true;
    if (s[left] != s[right]) return false;
    return is_palindrome_helper(s, left + 1, right - 1);
}

bool is_palindrome(const string& s) {
    return is_palindrome_helper(s, 0, s.length() - 1);
}

int main() {
    cout << boolalpha;  // true/false 출력
    cout << is_palindrome("기러기") << endl;
    cout << is_palindrome("토마토") << endl;
    cout << is_palindrome("바나나") << endl;
    cout << is_palindrome("racecar") << endl;
    cout << is_palindrome("radar") << endl;
    cout << is_palindrome("stars") << endl;
    cout << is_palindrome("123321") << endl;
}

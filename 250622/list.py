tasks = []

#인덱스로 접근해 보기
print("첫 번째 할 일:", tasks[0])
print("전체 할 일 목록:")
for idx, t in enumerate(tasks, start=1):   #enumerate(iterable 객체, 시작인덱스)
  print(f"{idx}, {t}")
'''# idx(번호), t(할 일) 쌍으로 순회하면서'''
'''# f-string으로 "번호. 할 일" 형태로 출력'''

''' C++
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<string> tasks;
    tasks.push_back("메일 확인");
    tasks.push_back("문서 작성");
    cout << tasks[0] << " , " << tasks.back() << "\n";
    for (int i = 0; i < tasks.size(); ++i)
        cout << i+1 << ". " << tasks[i] << "\n";
    return 0;
}'''

#cout << i+1 << ". " << tasks[i] << "\n";
'''cout
C++에서 콘솔(표준출력)으로 값을 보낼 때 쓰는 스트림 객체예요.

<< (삽입 연산자)
cout << 값; 형태로 값을 출력 버퍼에 “넣는다” 라고 생각하시면 됩니다. 여러 값을 연달아 쓰면 차례대로 이어서 출력돼요.

i+1

i는 0부터 시작하는 인덱스

사용자에게는 “1번, 2번, 3번…” 처럼 보여주고 싶으니 i+1을 출력합니다.
예를 들어 첫 번째 루프 때 i == 0이니 0+1 == 1을 출력하죠.

<< ". "

숫자 뒤에 붙일 문자열 리터럴입니다.

점(.)과 공백( ) 두 글자를 출력해서 “1. ”, “2. ”처럼 보이게 합니다.

<< tasks[i]

tasks는 vector<string>이니까, tasks[i]는 i번째 문자열(여기선 할 일 제목)입니다.

예를 들어 tasks[0] == "메일 확인" 이므로 “메일 확인”을 출력합니다.

<< "\n"

"\n"은 줄바꿈(newline) 문자입니다.

C++에서는 std::endl을 써도 되지만, 성능을 위해 보통 "\n"을 더 자주 씁니다.
'''
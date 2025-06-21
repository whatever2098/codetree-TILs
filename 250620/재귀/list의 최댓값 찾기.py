'''하위 문제: 첫 (n - 1)개의 요소들 중 최댓값을 찾는 것.
그 최댓값과 마지막 요소를 비교하면 전체리스트의 최댓값을 찾을 수 있습니다'''

#베이스 케이스
def max_list(my_list):
  if len(my_list) == 1:
    return my_list[0]
  
#재귀케이스
  max_sublist = max_list(my_list[:-1])
  if max_sublist >= my_list[-1]:
   return max_sublist
  else:
    return my_list[-1]
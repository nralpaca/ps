# ps
daily problem solving





----
python 값 제거 할 때

a = [1, 2, 3]
remove_list = []
for i in range(len(a)):
  if a[i] == 3:
    #p1 del a[i] --> range가 꼬임.
    #p2 remove_list.append(i)
    remove_list.append(a[i])
for r in remove_list:
  #p2 del a[r] --> index가 꼬임.
  a.remove(r) #--> 첫 번쨰 원소만 삭제. 값이 유일 할 때 허용
  
  

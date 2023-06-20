'''Программа считывает n строк с числами и выстраивает единый отсортированый по возрастанию список
   без использования функций sort(), sorted().
'''

n = int(input())

def quick_merge(list1, list2):
    list3 = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            list3.append(list1[p1])
            p1 += 1
        else:
            list3.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        list3.extend(list1[p1:])
    if p2 < len(list2):
        list3.extend(list2[p2:])
    return list3

def read_str(n):
    list_result, list2 = [], []
    for i in range(n):
        list2 += [int(x) for x in input().split()]
        list_result = quick_merge(list_result, list2)
        list2.clear()
    return list_result

print(*read_str(n))
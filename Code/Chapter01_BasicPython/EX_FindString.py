"""
User nhập vào 1 string và 1 sub string, tìm số lần xuất hiện 
của sub string trong string

Constraint: 1<= len(string) <= 200

Ví dụ:
Input
ABCDCDC 
CDC

Output 
2
"""

"""
A
AB
ABC
ABCD
ABCDC

"""

def count_substring(string, sub_string):
    cnt = 0
    for i in range(0, len(string)):
        if string[i:(i+len(sub_string))] == sub_string:
            cnt = cnt+1
    return cnt


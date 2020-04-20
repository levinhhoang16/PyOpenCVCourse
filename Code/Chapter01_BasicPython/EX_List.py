"""
Cho 1 list (list = []). Thực hiện 1 số công việc sau

1. insert i e: Insert integer  at position .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Input format:
Nhận vào input n là số command cần thực hiện, mỗi line tiếp theo là n command được mô tả ở trên

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints:
Các thành phần dc thêm vào list phải là integer

Output Format
Gặp command print thì xuất list ra

Sample Input 0

12
insert 0 5  ==>[5]
insert 1 10 ==>[5,10]
insert 0 6  ==>[6,5,10]
print
remove 6    ==>[5,10]
append 9    ==>[5,10,9]
append 1    ==>[5,10,9,1]
sort        ==>[1, 5, 9, 10]
print
pop         ==>[1, 5, 9]  
reverse     ==>[9, 5, 1]
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
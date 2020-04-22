"""
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked.

Constraints
1900 <= i <= 10^5

Output Format

Output is taken care of by the template. Your function must return a boolean value (True/False)

Sample Input 0

1990
Sample Output 0

False
Explanation 0

1990 is not a multiple of 4 hence it's not a leap year.
"""

"""
User nhập vào 1 số năm x, tìm xem năm có phải năm nhuận không.
Nếu là năm nhuận, thì in ra TRUE
Nếu kp thì in ra False

Để kiểm tra 1 năm có phải là năm nhuận k:
x chia hết cho 4 thì nó là năm nhuận trừ trường hợp:
        -x chia hết cho 100 => nó kp là năm nhuận
        -x chia hết cho 400 => nó vẫn là năm nhuận
"""

def is_namNhuan(year):
    isNhuan = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                isNhuan = True
            else:
                isNhuan = False
        isNhuan = True
    else:
        isNhuan = False
    return isNhuan

year = int(input())
isNamNhuan = is_namNhuan(year)
print(isNamNhuan)
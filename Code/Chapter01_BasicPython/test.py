# def myFunc(a,b):
#     return a+b

# x=myFunc(1,2)
# print(x)


# def add(a,b):
#     return a+b

# globarVar = "This is global variable"

# def functionScope():
#     localVar = "This is local variable"
#     print("Scope of function")
#     print("Access global Var {}".format(globarVar))
#     print("Acess local Var {}".format(localVar))
#     print("End function scope")
#     return


# functionScope()
# print("Acess global var in main {}".format(globarVar))
# print("Acess local var in main {}".format(localVar))

# from testModule import *

# print(addFunc(1,2))
# print(subFunc(1,2))

if __name__=="__main__":
    N = int(input())
    bangDiem = {}
    for i in range(N):
        diem = input().split()
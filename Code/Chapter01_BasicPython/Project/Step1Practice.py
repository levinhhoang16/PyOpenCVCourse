"""
Chương trình 1
Lấy đường dẫn thư mục input, file extension cần check
Open thư mục và Check extension của file
Output các file có extension là extension được user truyền vào
"""
import os

if __name__=="__main__":
    inputDirectory = input()
    print(inputDirectory)
    for file in os.listdir(inputDirectory):
        if os.path.isfile(os.path.join(inputDirectory,file)):
            if file.endswith(".py"):
                print(file)
                
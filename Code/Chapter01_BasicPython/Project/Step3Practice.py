"""
Chương trình tổ chức lại cái file trong thư mục dựa vào extension của file
VD:
File .img .jpg .jpeg sẽ đưa vào thư mục IMAGES...
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg",
                   ".heif", ".psd"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PLAINTEXT": (".txt", ".in", ".out"),
        "PDF": ".pdf",
        "PYTHON": ".py",
        "EXE": ".exe",
        "OTHER": "",
        "FOLDERS": ""
Chương trình nhận input là đường dẫn thư mục chứa các file cần sắp xếp
Output là thư mực được tổ chức lại
"""

import os
import shutil  

g_dirExtensionDict = {
    "HTML": (".html5", ".html", ".htm", ".xhtml"),
    "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
               "svg",
               ".heif", ".psd"),
    "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
               ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
    "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                  ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"),
    "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"),
    "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
              ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
    "PLAINTEXT": (".txt", ".in", ".out"),
    "PDF": ".pdf",
    "PYTHON": ".py",
    "EXE": ".exe",
    "OTHER": "",
    "FOLDERS": ""
}


def createDirectory(parentDir):
    for key in g_dirExtensionDict:
        if key not in os.listdir(parentDir):
            path = os.path.join(parentDir, key)
            os.mkdir(path)
    return


def organizeFileBasedOnExtension(parentDir):
    for file in os.listdir(parentDir):
        filePath = os.path.join(parentDir, file)
        if os.path.isfile(filePath):
            # if file.endswith(g_dirExtensionDict["PLAINTEXT"]):
            #     destPath = os.path.join(parentDir,"PLAINTEXT")
            #     print("Move file {} to {}".format(file, destPath))
            for key in g_dirExtensionDict:
                if file.endswith(g_dirExtensionDict[key]):
                    destPath = os.path.join(parentDir, key)
                    print("Move file {} to {}".format(filePath,destPath))
                    shutil.move(filePath, destPath)
                    break
    return


if __name__ == "__main__":
    print("Enter Input Directory path: ")
    inputDirectory = input()
    createDirectory(inputDirectory)
    organizeFileBasedOnExtension(inputDirectory)


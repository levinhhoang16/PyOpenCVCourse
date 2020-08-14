import os

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
if __name__=="__main__":
    inputDirectory = input()
    for entry in os.listdir(inputDirectory):
        if os.path.isfile(os.path.join(inputDirectory, entry)):
            for key in g_dirExtensionDict:
                extension = g_dirExtensionDict[key]
                if entry.endswith(extension):
                    print(entry)
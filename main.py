import os.path as path
import os
import win32.win32print

defaultPrinter = win32.win32print.GetDefaultPrinter()

def main():
    try:
        while True:
            inputDir = input("Input folder you want all files to be printed (ex. C:\\Users\\gsummerfield\\Documents\\..\\Important):\n")
            if path.isdir(inputDir) == True:
                print("Scanning folder...")
                for files in path.normpath(inputDir):
                    try:
                        os.system("print.exe " + path.normpath(files))
                    except Exception as identifier:
                        print("Oho noes!")
                        SystemExit(1)
            else:
                print("Not a folder!")
    except Exception as ex:
        print("Error:" + str(ex))
        exit()

if __name__ == "__main__":
    main()

import os.path as path
import os

def main():
    try:
        inputDir = input("Input folder you want all files to be printed (ex. C:\\Users\\gsummerfield\\Documents\\..\\Important):\n")
        if path.isdir(inputDir) == True:
            print("Scanning folder...")
            for files in path.normpath(inputDir):
                try:
                    os.system("print.exe " + path.normpath(files))
                except expression as identifier:
                    print("Oho noes!")
        else:
            print("Not a folder!")
    except:
        print("Error:" + Exception)
        exit()

if __name__ == "__main__":
    main()

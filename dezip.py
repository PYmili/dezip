import os
import sys

import Zip
import File7z

MODE = "decompression"

ZIP = False
COMPRESS_TYPE = "STORED"
_7Z = False
RAR = False

PASSWORD = None
FILE_OUT_PATH = os.getcwd()
FILES = []


def Help() -> None:
    print("Dezip (zip, 7z) Package processing tool.")
    print("Help Documents:")
    print("\t[--decompression, -d, --dec, -dec]\tDecompression file operation.")
    print("\t[--compress, -c, --com, -com]\t\tCompress file operation.")
    print("\t[--input_file, --input_files, -i]\tEnter the file to process.")
    print("\t[-o, --out]\t\t\t\tOutput file.")
    print("\t[--password, -p, -pwd]\t\t\tSet password.")
    print("\t[--see, -s, -see]\t\t\tView file operations.")
    print("\t[--7z, -7z, -7]\t\t\tDimension file type is 7z.")
    print("\t[--zip, -z, -zip]\t\t\tThe annotation file type is zip.")
    print("""\t
            Zip file compression methods
            
            STORED 0
            DEFLATED 1
            BZIP2 2
            LZMA 3
            """)


if __name__ == '__main__':
    """Get Command Argv"""
    line: int = 1
    for argv in sys.argv[1:]:
        if argv in ["--decompression", "-d", "--dec", "-dec"]:
            pass
        elif argv in ["--compress", "-c", "--com", "-com"]:
            MODE = "compress"
        elif argv in ["--see", "-s", "-see"]:
            MODE = "see"

        if argv in ["--zip", "-z", "-zip"]:
            ZIP = True
            """
            Zip file compression methods
            
            STORED 0
            DEFLATED 1
            BZIP2 2
            LZMA 3
            """
            try:
                ModeArg = str(sys.argv[1:][line])
            except IndexError:
                continue

            if ModeArg in ["DEFLATED", "1"]:
                COMPRESS_TYPE = "STORED"
            elif ModeArg in ["BZIP2", "2"]:
                COMPRESS_TYPE = "BZIP2"
            elif ModeArg in ["LZMA", "3"]:
                COMPRESS_TYPE = "LZMA"
            else:
                pass

        if argv in ["--7z", "-7z", "-7"]:
            _7Z = True

        if argv in ["--input_file", "--input_files", "-i"]:
            if os.path.isdir(sys.argv[1:][line]):
                FILES.append(os.path.split(sys.argv[1:][line])[-1])
                for root, dirs, files in os.walk(sys.argv[1:][line]):
                    for file in files:
                        FILES.append(os.path.join(root, file))

            for filepath in sys.argv[1:][line:]:
                if os.path.isfile(filepath):
                    FILES.append(filepath)
        if argv in ["--password", "-p", "-pwd"]:
            try:
                PASSWORD = bytes(sys.argv[1:][line], encoding="utf-8")
            except IndexError:
                print(f"\'{argv}\' No parameters.")
        if argv in ["-o", "--out"]:
            try:
                FILE_OUT_PATH = sys.argv[1:][line]
            except IndexError:
                print(f"\'{argv}\' Output path parameter not recognized.")
                continue
            if os.path.exists(FILE_OUT_PATH):
                pass
            else:
                print(f"{FILE_OUT_PATH} path does not exist!")
                FILE_OUT_PATH = None

        if argv in ['-h', '--help', 'help', 'h', '-help']:
            Help()

        line += 1

    """implement"""
    if ZIP:
        if MODE == "decompression":
            Zip.ZIP_OUT_PATH = FILE_OUT_PATH
            Zip.DEC_ZIP_FILES = FILES
            Zip.PASSWORD = PASSWORD
            Zip.DecompressionZip().Decs()
        elif MODE == "compress":
            Zip.ZIP_OUT_PATH = FILE_OUT_PATH
            Zip.C_ZIP_FILES = FILES
            Zip.PASSWORD = PASSWORD
            Zip.CompressZip(COMPRESS_TYPE).compress()
        elif MODE == "see":
            for file in FILES:
                print(f"{file}:")
                Zip.ZIP_FILE = file
                Zip.PASSWORD = PASSWORD
                Zip.ReadZipFile().Read()

    if _7Z:
        if MODE == "decompression":
            File7z.FILES = FILES
            File7z.PASSWORD = PASSWORD
            File7z.FILE_OUT_PATH = FILE_OUT_PATH
            File7z.Decompression7z().Decs()
        elif MODE == "compress":
            File7z.FILES = FILES
            File7z.PASSWORD = PASSWORD
            File7z.FILE_OUT_PATH = FILE_OUT_PATH
            File7z.Compress7z().compress()
        elif MODE == "see":
            File7z.FILES = FILES
            File7z.PASSWORD = PASSWORD
            for file in FILES:
                print(file)
                File7z.See7z().see()
    if RAR:
        pass

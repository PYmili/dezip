import os
import py7zr

from fileid import fileid
from tqdm import tqdm

PASSWORD: str = None
FILE_OUT_PATH = os.getcwd()
FILES = []


class Decompression7z:
    @staticmethod
    def Decs() -> bool:
        for file in FILES:
            if os.path.isfile(file) and py7zr.is_7zfile(file):
                with py7zr.SevenZipFile(file, mode="r", password=PASSWORD) as z:
                    pbar = tqdm(z.getnames())
                    for name in pbar:
                        z.extract(targets=name, path=FILE_OUT_PATH)
                        pbar.set_description(f"Decompression 7z | Processing %s" % name)
                return True
            else:
                print(f"{file} is not a .7z compressed package!")
                return False


class Compress7z:
    @staticmethod
    def compress() -> bool:
        __newFileName = None
        if FILE_OUT_PATH:
            if os.path.isdir(FILE_OUT_PATH):
                if len(FILES) == 1:
                    __LogVar = os.path.splitext(os.path.split(FILES[0])[-1])[0]
                    __newFileName = os.path.join(
                        FILE_OUT_PATH,
                        __LogVar
                    ) + ".7z"
                else:
                    __newFileName = os.path.join(
                        FILE_OUT_PATH,
                        os.path.split(FILES[0])[-1]
                    ) + ".7z"
                    del FILES[0]
            with py7zr.SevenZipFile(file=__newFileName, mode="w", password=PASSWORD) as wz:
                pbar = tqdm(FILES)
                for i in pbar:
                    if os.path.isfile(i):
                        wz.write(i)
                        pbar.set_description(f"Compress {FILE_OUT_PATH} | Processing %s" % i)
                    else:
                        print(f"{i} The file file does not exist!")
            return True
        else:
            print(f"The parameter of \'FILE_OUT_PATH\' cannot be empty!")
            return False


class See7z:
    @staticmethod
    def see() -> None:
        for i in FILES:
            with py7zr.SevenZipFile(file=i, mode="r") as rz:
                for file in rz.getnames():
                    info = rz.archiveinfo()
                    print("\t", file)
                    print("\t\tFile size before compression:", info.uncompressed)
                    print("\t\tFile size after compression:", info.size)
                    print("\t\tCompress Type:", info.method_names)
                    # print("\t\t", info.stat)
                    # print("\t\t", info.solid)
                    print("\t\tblocks = ", info.blocks)
                    print("\t\theader size = ", info.header_size)

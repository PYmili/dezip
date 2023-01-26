import os
import zipfile

from tqdm import tqdm
from fileid import fileid

"""info"""
ZIP_FILE: str = None
PASSWORD: bytes = None
ZIP_OUT_PATH: str = os.getcwd()
# COMPRESS_TYPE = zipfile.ZIP_DEFLATED

"""DecZip"""
DEC_ZIP_FILES = []

"""CompressZip"""
C_ZIP_FILES = []


class DecompressionZip:
    @staticmethod
    def Decs() -> bool:
        for __file in DEC_ZIP_FILES:
            if os.path.exists(__file) and zipfile.is_zipfile(__file):
                with zipfile.ZipFile(__file, "r") as zipR:
                    try:
                        pbar = tqdm(zipR.namelist())
                        for i in pbar:
                            zipR.extract(i, pwd=PASSWORD, path=ZIP_OUT_PATH)
                            pbar.set_description(f"Decompression | Processing %s" % i)

                    except RuntimeError:
                        print(f"The {__file} file package password is incorrect!")
                        return False
                return True
            else:
                print(f"\'{__file}\' Not a zip package.")
                return False


class CompressZip:
    def __init__(self, _compress_type: str = "DEFLATED") -> None:
        if _compress_type in ["DEFLATED", "1"]:
            self._compress_type = zipfile.ZIP_STORED
        elif _compress_type in ["BZIP2", "2"]:
            self._compress_type = zipfile.ZIP_BZIP2
        elif _compress_type in ["LZMA", "3"]:
            self._compress_type = zipfile.ZIP_LZMA
        else:
            self._compress_type = zipfile.ZIP_STORED
        self.str_compress_type = _compress_type

    def compress(self) -> bool:
        if ZIP_OUT_PATH is not None:
            if os.path.isdir(ZIP_OUT_PATH):
                if len(C_ZIP_FILES) == 1:
                    __LogVar = os.path.splitext(
                        os.path.split(C_ZIP_FILES[0])[-1]
                    )[0]
                    __newFilePath = os.path.join(
                        ZIP_OUT_PATH,
                        __LogVar
                    ) + ".zip"
                else:
                    __newFilePath = os.path.join(
                        ZIP_OUT_PATH,
                        os.path.split(C_ZIP_FILES[0])[-1]
                    ) + ".zip"
                    del C_ZIP_FILES[0]
            else:
                __newFilePath = ZIP_OUT_PATH

            print(f"Set PassWord: {PASSWORD.decode('utf-8') if PASSWORD else None}")
            with zipfile.ZipFile(__newFilePath, "w") as zipW:
                zipW.setpassword(PASSWORD)

                pbar = tqdm(C_ZIP_FILES)
                for i in pbar:
                    if os.path.isfile(i):
                        zipW.write(i, compress_type=self._compress_type)
                        pbar.set_description(f"Compress Type: {self.str_compress_type} | Processing %s" % i)
                    else:
                        print(f"{i} The file file does not exist!")
            return True
        else:
            print(f"ZIP_OU_PATH = \'{ZIP_OUT_PATH}\'")
            return False


class ReadZipFile:
    @staticmethod
    def Read() -> None:
        file_num = 0
        if zipfile.is_zipfile(ZIP_FILE):
            with zipfile.ZipFile(ZIP_FILE, "r") as zipR:
                for file in zipR.namelist():
                    info = zipR.getinfo(file)
                    print(f"\t{file}")
                    print(f"\t\tFile size before compression: {info.file_size}")
                    print(f"\t\tFile size after compression: {info.compress_size}")
                    date_list = [str(n) for n in info.date_time]
                    print(f"\t\tLast modified：{'-'.join(date_list[0:3])} {':'.join(date_list[4:])}")
                    if info.compress_type == 0:
                        info.compress_type = "STORED"
                    elif info.compress_type == 2:
                        info.compress_type = "BZIP2"
                    elif info.compress_type == 3:
                        info.compress_type = "LZMA"
                    else:
                        info.compress_type = "STORED"

                    print(f"\t\tCompress Type: {info.compress_type}")
                    print("\n")
                    file_num += 1
                print(f"\'{file}\' There are {file_num} files in total")
        else:
            print(f"{__file__} Class DecZip in \'{ZIP_FILE}\' Not a zip package.")

# dezip

dezip 是一个用Python编写的压缩包处理工具。

Dezip is a package processing tool written in Python.

___

dezip 使用Python的zipfile, py7zr等库实现对.zip和.7z压缩包的处理。

dezip --help

```
Dezip (zip, 7z) Package processing tool.
Help Documents:
        [--decompression, -d, --dec, -dec]      Decompression file operation.
        [--compress, -c, --com, -com]           Compress file operation.
        [--input_file, --input_files, -i]       Enter the file to process.
        [-o, --out]                             Output file.
        [--password, -p, -pwd]                  Set password.
        [--see, -s, -see]                       View file operations.
        [--7z, -7z, -7]                 Dimension file type is 7z.
        [--zip, -z, -zip]                       The annotation file type is zip.

            Zip file compression methods

            STORED 0
            DEFLATED 1
            BZIP2 2
            LZMA 3
```
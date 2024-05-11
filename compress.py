import py7zr
import os
import time
my_filter_BZIP2 = [{"id": py7zr.FILTER_BZIP2}]
my_filter_PPMD = [{"id": py7zr.FILTER_PPMD}]
my_filter_BROTLI = [{"id": py7zr.FILTER_BROTLI}]
my_filter_LZMA2 = [{"id": py7zr.FILTER_LZMA2, "preset": 7}]


def com_data(file_name, file_url, file_root):
    f_com_size = []
    x = 1
    y = 0
    folder = file_root + '/' + file_name + '_com_data'
    if not os.path.exists(folder):  
        os.makedirs(folder)  
    time_start = time.perf_counter()
    with py7zr.SevenZipFile(os.path.join(folder, "BZIP2.7z"), 'w', filters=my_filter_BZIP2) as archive:
        archive.write(file_url, file_name)
    time_end = time.perf_counter()
    time_sum = (time_end - time_start) * 60 * 60
    f_com_size.append(x * os.path.getsize(os.path.join(folder, "BZIP2.7z")) + y * time_sum)
        time_start = time.perf_counter()

    with py7zr.SevenZipFile(os.path.join(folder, "PPMD.7z"), 'w', filters=my_filter_PPMD) as archive:
        archive.write(file_url, file_name)
    time_end = time.perf_counter()
    time_sum = (time_end - time_start) * 60 * 60
    f_com_size.append(x * os.path.getsize(os.path.join(folder, "PPMD.7z")) + y * time_sum)
    time_start = time.perf_counter()

    
    with py7zr.SevenZipFile(os.path.join(folder, "BROTLI.7z"), 'w', filters=my_filter_BROTLI) as archive:
        archive.write(file_url, file_name)
    time_end = time.perf_counter()
    time_sum = (time_end - time_start) * 60 * 60
    f_com_size.append(x * os.path.getsize(os.path.join(folder, "BROTLI.7z")) + y * time_sum)
    time_start = time.perf_counter()


    with py7zr.SevenZipFile(os.path.join(folder, "LZMA2.7z"), 'w', filters=my_filter_LZMA2) as archive:
        archive.write(file_url, file_name)
    time_end = time.perf_counter()
    time_sum = (time_end - time_start) * 60 * 60
    f_com_size.append(x * os.path.getsize(os.path.join(folder, "LZMA2.7z")) + y * time_sum)
    print(file_name + " complete!")
    index = f_com_size.index(min(f_com_size))
    if index == 0:
        return "BZIP2",f_com_size
    elif index == 1:
        return "PPMD",f_com_size
    elif index == 2:
        return "BROTLI",f_com_size
    elif index == 3:
        return "LZMA2",f_com_size

import pandas as pd
f_name = []
f_type = []
f_size = []
f_algorithm = []
f_compress_size=[]
folder_1 = 'result_dir'
if not os.path.exists(folder_1): 
    os.makedirs(folder_1) 
def get_com_data(file_dir):
    dic={}
    for i in range(0,300):
        dic[i]=0
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            size=os.path.getsize(os.path.join(root, file))
            tmp_size=int(size/50000)
            if(tmp_size <300 and dic[tmp_size]<=20 and os.path.splitext(file)[1] == ".avi"):
                dic[tmp_size]+=1
                f_name.append(os.path.splitext(file)[0])
                f_type.append(os.path.splitext(file)[1])
                f_size.append(os.path.getsize(os.path.join(root, file)))
                algo,compress_size=(com_data(file, os.path.join(root, file), folder_1))
                f_algorithm.append(algo)
                f_compress_size.append(compress_size)

file_path = 'data'
get_com_data(file_path)
#output_excel = {"name":f_name,'type': f_type, 'size': f_size}
output_excel = {"name":f_name,'type': f_type, 'size': f_size, 'algorithm': f_algorithm,'compress_size':f_compress_size}
output = pd.DataFrame(output_excel)
output.to_excel('avi.xlsx', index=False)




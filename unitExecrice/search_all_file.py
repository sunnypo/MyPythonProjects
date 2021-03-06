from datetime import datetime
from pathlib import Path


ignore_files = ['.DS_Store']


def find_all_file(src_dir) -> list:
    result = []
    for i in Path(src_dir).iterdir():
        if i.is_file():
            result.append(i)
        else:
            for x in find_all_file(i):
                result.append(x)
    return result


def search_all_file(file_type_dic, src_dir) -> list:
    file_list = find_all_file(src_dir)
    file_tbc = []  # file to be changed
    for file in file_list:
        if file.name in ignore_files:
            pass
        theory = Path(src_dir, "undefined")
        for key in file_type_dic:
            p = file.suffix.lower()[1:]
            if p in file_type_dic[key]:
                theory = Path(src_dir, key)  # +the key
                break
        reality = file.parents[0]
        if not theory == reality:  # 字典找key（文件结尾）(theory)= (reality)parent
            file_name = file.name
            file_tbc.append(file)
            move_file(file, Path(theory, file_name))

    return file_tbc


def record_mv_log(action, target_path):
    log_file = open(
        "/Users/Sunny/Documents/myPythonProject/MyPythonProjects/unitExecrice/log.txt", 'a')
    log_line = (f"{datetime.now()}, {action}, ^{target_path}\n")
    log_file.write(log_line)
    log_file.close()


def move_file(src_file, dest_path):
    record_mv_log("_locate file to be sorted_", src_file)
    src_file.rename(dest_path)
    record_mv_log("_move the sort file from_", dest_path)

# 每行log可能是这样的：
# yyyy/mm/dd hh:MM:ss create /Users/hd/tmp/images
# yyyy/mm/dd hh:MM:ss mv /Users/hd/tmp/a.png /Users/hd/tmp/images/a.png

# yyyy/mm/dd hh:MM:ss 是年月日 时分秒


folder_name_dict = {
    "assets": ["template"],
    "sourceimages": ["jpg", "jpeg", "png", "heic", "exr"],
    "scripts": ["py", "mel"],
    "sound": ["wav", "mp3"],
    "animate": ["fla"]
}


for i in search_all_file(folder_name_dict, "/Users/Sunny/temp"):
    print(i)

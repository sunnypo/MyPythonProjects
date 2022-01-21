from pathlib import Path


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
            #file_tbc.append(Path(theory, file_name))
    return file_tbc


folder_name_dict = {
    "assets": ["template"],
    "sourceimages": ["jpg", "jpeg", "png", "heic", "exr"],
    "scripts": ["py", "mel"],
    "sound": ["wav", "mp3"],
    "animate": ["fla"]
}


for i in search_all_file(folder_name_dict, "/Users/Sunny/temp"):
    print(i)

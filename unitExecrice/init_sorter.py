from pathlib import Path
from typing import List

ignore_files = ['.DS_Store']


def get_folder_files(folder_name: str) -> List[Path]:
    files = []
    for item in Path(folder_name).iterdir():
        if item.is_file():
            files.append(item)
    return files


def get_suffix_folder_name(suffix: str, folder_dict) -> str:
    for key in folder_dict:
        if suffix in folder_dict[key]:
            return key
    return None


def move_file_to_dist_folder(folder_dict, src_folder: str, dest_folder: str = None):
    if dest_folder == None:
        dest_folder = src_folder
    undefined = "undefined"
    # if subfolder not exists yet, create it.
    for key in folder_dict.keys():
        p = Path(src_folder, key)
        if not p.exists():
            p.mkdir(parents=True)
            print(f"makedir {p} sucess.")
    p = Path(src_folder, undefined)
    if not p.exists():
        p.mkdir(parents=True)
    # get src_folder's files list
    files = get_folder_files(src_folder)
    # move files to dest_folder
    for file in files:
        if file.name in ignore_files:
            pass
        else:
            suffix = file.suffix.lower()[1:]
            folder = get_suffix_folder_name(suffix, folder_dict)
            if folder == None:
                target = Path(dest_folder, undefined, file.name)
            else:
                target = Path(dest_folder, folder, file.name)
            file.rename(target)


folder_name_dict = {
    "assets": ["template"],
    "sourceimages": ["jpg", "jpeg", "png", "heic", "exr"],
    "scripts": ["py", "mel"],
    "sound": ["wav", "mp3"],
    "animate": ["fla"]
}

move_file_to_dist_folder(
    folder_name_dict,
    "/Users/Sunny/temp"
)

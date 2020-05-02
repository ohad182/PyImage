import os
from features.compare.time import get_dated_path


def rename_file(file_path: str, preview: bool = True, dry: bool = True):
    new_path = None
    try:
        new_path = get_dated_path(file_path)
        if new_path is not None:
            if preview:
                print(f"{os.path.basename(file_path)} -> {os.path.basename(new_path)}")
            if not dry:
                if os.path.basename(file_path) == os.path.basename(new_path):
                    print(f"Already formatted, Skipping {file_path}")
                else:
                    os.rename(file_path, new_path)
        else:
            print(f"Unable to find date for {file_path}")
    except PermissionError as pe:
        print(str(pe))
    except FileExistsError:
        counter = 0
        ext = os.path.splitext(new_path)[1]
        while True:
            temp_path = new_path.replace(ext, f".{counter}{ext}")
            if not os.path.exists(temp_path):
                break
            counter = counter + 1
        if not dry:
            os.rename(file_path, temp_path)
    except IOError as e:
        print(f"File {file_path} IO error {e}")
    return new_path

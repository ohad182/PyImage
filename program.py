import os
from features.compare.time import get_dated_path

"""
    watcher = Watcher(backup_path, sync=True)
    watcher.include("my_cloud_mount_path, '*', name="My Cloud Home")
    watcher.include("google_drive_mount_path, '*', name="Google Drive")
    watcher.include("one_drive_mount_path, '*', name="One Drive")
    watcher.include("dropbox_drive_mount_path, '*', name="Dropbox Drive")


    watcher.watch()


"""


def rename_file(file_path: str, preview: bool, dry: bool):
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
    except FileExistsError as fee:
        counter = 0
        ext = os.path.splitext(new_path)[1]
        temp_path = None
        while True:
            temp_path = new_path.replace(ext, f".{counter}{ext}")
            if not os.path.exists(temp_path):
                break
            counter = counter + 1
        if not dry:
            os.rename(file_path, temp_path)
    except IOError as e:
        print("File " + file_path + "not found")

    return new_path

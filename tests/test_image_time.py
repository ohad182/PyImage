import pytest


@pytest.mark.skip
def test_image_time():
    from features.compare.time import get_image_date
    path = "D:\\תמונות 2017\\גלידה\\20170923_192308.jpg"
    date = get_image_date(path)
    assert date is not None


def test_get_time_folder():
    import os
    from core.file_manager import rename_file
    from os import walk
    print()
    folder_path = ""
    f = []
    for (dir_path, dir_names, file_names) in walk(folder_path):
        f.extend([f"{dir_path}{os.sep}{x}" for x in file_names])
        break
    counter = 1
    for fi in f:
        print(f"{counter} ", end="")
        date = rename_file(fi, dry=False)
        counter = counter + 1

        assert date is None if fi.endswith(".mp4") else not None

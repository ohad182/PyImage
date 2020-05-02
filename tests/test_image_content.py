def test_find_dups():
    import os
    from features.compare.content import is_same_content
    from os import walk
    print()
    folder_path = r""
    f = []
    for (dir_path, dir_names, file_names) in walk(folder_path):
        f.extend([f"{dir_path}{os.sep}{x}" for x in file_names if x.endswith("jpg")])
        break

    for counter, fi in enumerate(f):
        print(f"{counter + 1} ", end="")

        for i in range(counter + 1, len(fi) - 1):
            same = is_same_content(fi, f[i])
            if same:
                print(f"Found same image: {fi} and {f[counter]}")

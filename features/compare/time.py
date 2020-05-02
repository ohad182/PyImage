import os
import re
from os import path
from datetime import datetime
from PIL import Image, UnidentifiedImageError

from common import can_parse_int

STANDARD_DATE_FORMAT = '%Y:%m:%d %H:%M:%S.%f'
EXIF_DATE_TAGS = [(36867, 37521),  # (DateTimeOriginal, SubsecTimeOriginal)
                  (36868, 37522),  # (DateTimeDigitized, SubsecTimeOriginal)
                  (306, 37520), ]  # (DateTime, SubsecTime)


def get_image_date(file_path: str, preview: bool = True):
    image_date = None
    try:
        img = Image.open(file_path)
        exif_data = img.getexif()

        for t in EXIF_DATE_TAGS:
            dat = exif_data.get(t[0])
            sub = exif_data.get(t[1], 0)

            # PIL.PILLOW_VERSION >= 3.0 returns a tuple
            dat = dat[0] if type(dat) == tuple else dat
            sub = sub[0] if type(sub) == tuple else sub
            if dat is not None:
                # found date
                if not isinstance(sub, int):
                    if re.search("[a-zA-Z]", sub) is not None:
                        # found some letters in sub
                        sub = re.sub("[a-zA-Z]", '', sub)
                    sub = sub.replace('\x00', '')
                    chars_to_remove = [x for x in list(sub) if not can_parse_int(x)]
                    if len(chars_to_remove) > 0:
                        for char_to_remove in chars_to_remove:
                            sub = sub.replace(char_to_remove, "")
                break
        if dat is None:
            return None
        str_image_date = f"{dat}.{sub}"
        if preview:
            print(f"{path.basename(file_path)} -> {str_image_date}")
        image_date = datetime.strptime(str_image_date, STANDARD_DATE_FORMAT)
    except TypeError as e:
        print(f"No EXIF date Information found for file:{file_path}")
    except UnidentifiedImageError as e:
        print(f"File {file_path} is not Image type file")
    except ValueError as e:
        print(e)

    return image_date


def get_dated_path(file_path: str, date_format: str = "%Y%m%d_%H%M%S"):
    """
    Gets the path with the dated file name as described in date_format (not dependant on fs status)
    :param file_path: The full path to the file
    :param date_format: The format of the output file name
    :return:
    """
    new_path = None
    try:
        image_date = get_image_date(file_path, False)
        if image_date is not None:
            str_formatted_date = image_date.strftime(date_format)
            file_type = path.splitext(file_path)[1]
            new_file_name = f"{str_formatted_date}{file_type}"
            new_path = path.dirname(file_path) + os.sep + new_file_name
    except PermissionError as pe:
        print(str(pe))

    return new_path


# new_path = None
#     try:
#         image_date = get_image_date(file_path, False)
#         if image_date is not None:
#             str_formatted_date = image_date.strftime(date_format)
#             file_type = path.splitext(file_path)[1]
#             new_file_name = f"{str_formatted_date}{file_type}"
#             new_path = path.dirname(file_path) + os.sep + new_file_name
#             if preview:
#                 print(f"{path.basename(file_path)} -> {new_file_name}")
#             if not dry:
#                 if os.path.basename(file_path) == os.path.basename(new_path):
#                     print(f"Already formatted, Skipping {file_path}")
#                 else:
#                     os.rename(file_path, new_path)
#         else:
#             print(f"Unable to find date for {file_path}")
#     except PermissionError as pe:
#         print(str(pe))
#     except FileExistsError as fee:
#         counter = 0
#         ext = os.path.splitext(new_path)[1]
#         temp_path = None
#         while True:
#             temp_path = new_path.replace(ext, f".{counter}{ext}")
#             if not os.path.exists(temp_path):
#                 break
#             counter = counter + 1
#         if not dry:
#             os.rename(file_path, temp_path)
#     except IOError as e:
#         print("File " + file_path + "not found")
#
#     return new_path

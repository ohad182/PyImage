import time
from datetime import datetime
from PIL import Image

STANDART_DATE_FORMAT = '%Y:%m:%d %H:%M:%S.%f'
EXIF_DATE_TAGS = [(36867, 37521),  # (DateTimeOriginal, SubsecTimeOriginal)
                  (36868, 37522),  # (DateTimeDigitized, SubsecTimeOriginal)
                  (306, 37520), ]  # (DateTime, SubsecTime)



def get_image_date(file_path):
    exif = Image.open(file_path)._getexif()
    dat_stmp = None
    sub_stmp = None
    for t in EXIF_DATE_TAGS:
        dat_stmp = exif.get(t[0])
        sub_stmp = exif.get(t[1], 0)

        # PIL.PILLOW_VERSION >= 3.0 returns a tuple
        dat_stmp = dat_stmp[0] if type(dat_stmp) == tuple else dat_stmp
        sub_stmp = sub_stmp[0] if type(sub_stmp) == tuple else sub_stmp

        if dat_stmp != None: break  # Found one, go home

    if dat_stmp is None:
        return None

    full = '{}.{}'.format(dat_stmp, sub_stmp)
    T = datetime.strptime(full, STANDART_DATE_FORMAT)
    T = time.mktime(time.strptime(dT, '%Y:%m:%d %H:%M:%S')) + float('0.%s' % sub)
    return T


def imgDate(fn):
    "returns the image date from image (if available)\nfrom Orthallelous"
    std_fmt = '%Y:%m:%d %H:%M:%S.%f'
    # for subsecond prec, see doi.org/10.3189/2013JoG12J126 , sect. 2.2, 2.3
    tags = [(36867, 37521),  # (DateTimeOriginal, SubsecTimeOriginal)
            (36868, 37522),  # (DateTimeDigitized, SubsecTimeOriginal)
            (306, 37520), ]  # (DateTime, SubsecTime)
    exif = Image.open(fn)._getexif()

    for t in tags:
        dat_stmp = exif.get(t[0])
        sub_stmp = exif.get(t[1], 0)

        # PIL.PILLOW_VERSION >= 3.0 returns a tuple
        dat_stmp = dat_stmp[0] if type(dat_stmp) == tuple else dat_stmp
        sub_stmp = sub_stmp[0] if type(sub_stmp) == tuple else sub_stmp
        if dat_stmp != None: break

    if dat_stmp == None: return None
    full = '{}.{}'.format(dat_stmp, sub_stmp)
    T = datetime.strptime(full, std_fmt)
    T = time.mktime(time.strptime(dT, '%Y:%m:%d %H:%M:%S')) + float('0.%s' % sub)
    return T

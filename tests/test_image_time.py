def test_image_time():
    from features.time import get_image_date
    path = "D:\\תמונות 2017\\גלידה\\20170923_192308.jpg"
    date = get_image_date(path)
    assert date is not None

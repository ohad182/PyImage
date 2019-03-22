class Photo(object):
    """
    Database object for a photo
    to allow single uid calculation per full path
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.full_path = kwargs.get("full_path", "")
        self.date_taken = kwargs.get("date_taken", "")
        self.uid = kwargs.get("uid", "")

import locale

locale.setlocale(locale.LC_ALL, '')


class Item:
    def __init__(self):
        self.full_name = ''
        self.region = []
        self.quality = []
        self.plus = []
        self.gem1 = []
        self.gem2 = []
        self.price = 0
        self.seller = ''
        self.position = ''
        self.total_list = []

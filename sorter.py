class Sorter:
    @staticmethod
    def get_sort_by(sort_by):
        if sort_by == 'name':
            return 'AttributeName'
        elif sort_by == 'quality':
            return 'QualityName'
        elif sort_by == 'plus':
            return 'AdditionLevel'
        elif sort_by == 'gem1':
            return 'Gem1'
        elif sort_by == 'gem2':
            return 'Gem2'
        elif sort_by == 'seller':
            return 'SellerName'
        elif sort_by == 'price':
            return 'Price'

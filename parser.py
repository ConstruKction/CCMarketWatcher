class Parser:
    @staticmethod
    def parse_plus(plus):
        if plus == 0:
            return ''

        return f"(+{plus})"

    @staticmethod
    def parse_gems(gem1, gem2):
        dict_replacement = {
            'None': '',
            'Empty': 'E',
            'Normal': 'N',
            'Refined': 'R',
            'Super': 'S',
            'DragonGem': 'DG',
            'PhoenixGem': 'PG',
            'FuryGem': 'FG',
            'MoonGem': 'MG',
            'VioletGem': 'VG',
            'RainbowGem': 'RG',
            '[]': ''
        }

        gems = f"[{gem1}][{gem2}]"

        for key, value in dict_replacement.items():
            gems = gems.replace(key, value)

        return gems

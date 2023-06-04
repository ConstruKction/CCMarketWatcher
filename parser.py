class Parser:
    @staticmethod
    def parse_plus(plus):
        if plus == 0:
            return ''

        return f"(+{plus})"

    @staticmethod
    def abbreviate_gems(gem1, gem2):
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

    @staticmethod
    def expand_gems(gems):
        expanded_gems = []

        quality_dict_replacement = {
            'S': 'Super',
            'R': 'Refined',
            'N': 'Normal'
        }

        gem_dict_replacements = {
            'DG': 'DragonGem',
            'PG': 'PhoenixGem',
            'FG': 'FuryGem',
            'MG': 'MoonGem',
            'VG': 'VioletGem',
            'RG': 'RainbowGem'
        }

        for gem in gems:
            expanded_gems.append(f"{quality_dict_replacement.get(gem[0].upper())}"
                                 f"{gem_dict_replacements.get(gem[1:3].upper())}")

        return expanded_gems

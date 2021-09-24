# problem1
'''
class Mac:
    processor = 0
    memory = 0
    video_card = 0
    hard_disk = 0
    motherboard = 0
    screen_size = 0

    def __init__(self, name):
        self.name = name

comp = Mac('macOS Big Sur 11.6')
comp.processor = '8-core Intel Core i9 processor'
comp.memory = '512Gb'
comp.video_card = 'AMD Radeon Pro 5500M'
comp.motherboard = 'Logic Board 2.5GHz Core i5 '
comp.screen_size = '13 inch'
print(comp.__dict__)
'''
# problem2
colors = {
    "black": {"category": "hue", "type": "primary", "code": {"rgba": [255,255,255,1], "hex": "#000"}},
    "white": {"category": "value", "type": "primary", "code": {"rgba": [0,0,0,1], "hex": "#FFF"}},
    "red": {"category": "hue", "type": "primary", "code": {"rgba": [255,0,0,1], "hex": "#FF0"}},
    "blue": {"category": "hue", "type": "primary", "code": {"rgba": [0,0,255,1], "hex": "#00F"}},
    "yellow": {"category": "hue", "type": "primary", "code": {"rgba": [255,255,0,1], "hex": "#FF0"}},
    "green": {"category": "hue", "type": "secondary", "code": {"rgba": [0,255,0,1], "hex": "#0F0"}}
    }

class Colors:
    def __init__(self, dictt):
        self.dictt = dictt
    def tuples(self):
        t = tuple(self.dictt.keys())
        t2 = tuple(self.dictt["black"].keys())
        t3 = tuple(self.dictt["black"]["code"].keys())
        print(t, t2, t3)
        tt = tuple(self.dictt["black"].values())
        tt2 = tuple(self.dictt["black"]["code"].values())
        print(tt, tt2)
    def lists(self):
        a = list(self.dictt.keys())
        a1 = list(self.dictt["black"]["code"].keys())
        print(a, a1)
        aa = list(self.dictt["black"].values())
        aa1 = list(self.dictt["black"]["code"].values())
        print(aa, aa1)
    def sets(self):
        b = set(self.dictt.keys())
        print(b)
        # bb = set(self.dictt.values())
        # print(bb)

clrs = Colors(colors)
clrs.tuples()
clrs.lists()
clrs.sets()




#         a = colors.keys()
#         b = colors["black"].keys()
#         c = colors["black"]["code"].keys()
#         tuple_keys = (a, b, c)
#         black1 = colors["black"].values()
#         black = colors["black"]["code"].values()
# clrs = Colors
# print()
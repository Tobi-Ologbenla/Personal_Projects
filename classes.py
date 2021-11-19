class MMA():
    name = ''
    def __init__(self,name):
        self.name = name

    def fight(self):
        print('FIGHT')

class boxing(MMA):
    name = ''      
    def __init__(self,name):
        self.name = name
        self.fight

tyson = boxing('tyson')

tyson.fight()


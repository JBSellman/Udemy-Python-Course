class enemy:
    def __init__(self,hp,mp,type):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.type = type

    def get_hp(self):
        return self.hp

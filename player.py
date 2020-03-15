class Player:

    def __init__(self, is_human_player: bool, name: str = None):
        self.human = is_human_player
        self.username = name

    def is_human(self):
        return self.human

    def set_id(self, assigned_id: int):
        self.id = assigned_id





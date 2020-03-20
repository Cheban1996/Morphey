from morphey.models.base import BaseDBMorphey


class Bots(BaseDBMorphey):

    def __init__(self):
        super().__init__()
        self.bots = self.db['bots']  # collection bots

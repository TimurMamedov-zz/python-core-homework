class BaseAction:
    def __init__(self, name):
        self.name = name
        self.hash = hash(self.name)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        if self.hash != other.hash:
            return False
        return self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self == other:
            return False
        if self.name == 'Nothing':
            return True
        if self.name == 'Rock' and other.name == 'Paper':
            return True
        if self.name == 'Paper' and other.name == 'Scissors':
            return True
        if self.name == 'Scissors' and other.name == 'Rock':
            return True
        return False

    def __le__(self, other):
        if self == other:
            return True
        return self < other

    def __gt__(self, other):
        if self == other:
            return False
        return other < self

    def __ge__(self, other):
        if self == other:
            return True
        return self > other

class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')

class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')

class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

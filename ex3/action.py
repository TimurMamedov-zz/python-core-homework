class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if hash(self) != hash(other):
            return False
        return self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        raise Exception("Must be implemented in child class")

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

    def __lt__(self, other):
        return False


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')

    def __lt__(self, other):
        if self == other:
            return False
        if other.name == 'Paper':
            return True
        return False


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')

    def __lt__(self, other):
        if self == other:
            return False
        if other.name == 'Scissors':
            return True
        return False


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

    def __lt__(self, other):
        if other.name == 'Rock':
            return True
        return False
from operator import truediv


class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __gt__(self,other):
        if ((self.name == 'Rock') and (other.name == 'Scissors')):
            return True
        elif ((self.name == 'Scissor') and (other.name == 'Paper')):
            return True
        elif ((self.name == 'Paper') and (other.name == 'Rock')):
            return True
        else: 
            return False

    def __eq__(self,other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

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

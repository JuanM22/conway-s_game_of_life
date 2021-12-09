class Cell:

    def __init__(self, state, icon):
        self.state = state
        self.icon = icon

    def updateState(self, value):
        self.state = value
        self.icon = 'A' if(self.state) else 'D'

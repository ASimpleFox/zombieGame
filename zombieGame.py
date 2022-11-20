class Player:
    def __init__(self, target,):
        self.target = target    # Target score to get per turn
        self.score = 0          # Player score


class PlayerWithThreshold:
    def __init__(self, target, pointThreshold):
        self.target = target  # Target score to get per turn
        self.score = 0  # Player score
        # Indicates (win - opponent score) at which (self)
        # would go for a win instead of reaching target
        self.threshold = pointThreshold

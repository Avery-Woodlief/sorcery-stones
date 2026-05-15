class Block:

    def __init__(self, block_type, pos):
        self.type = block_type
        self.filename = f"../media/images/{self.type}.png"
        self.pos = pos
        self.left_neighbor = None
        self.right_neighbor = None
        self.top_neighbor = None
        self.bottom_neighbor = None

    def __str__(self):
        return f"{self.type} "

    def move(self, pos):
        self.pos = pos

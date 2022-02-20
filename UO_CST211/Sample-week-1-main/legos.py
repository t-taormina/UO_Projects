"""
in class - Legos
April 1, 2021
Author: Tyler
"""


class LegoBlock:

    def __init__(self, color: str, size: int): # constructor, initializes beginnig thing
        self.block_color = color
        self.size = size


    def repaint(self, new_color: str): # changes color of object
        self.block_color = new_color

    def __str__(self) -> str: # print for user
        return f"{self.block_color} block of size {self.size}"

    def __repr__(self) -> str: # print for debugging, look like a call to constructor
        return f"LegoBlock('{self.block_color}', {self.size})"

def main():
    orange_block = LegoBlock("orange", 4)
    print(orange_block)



#make lego box
class LegoBox:
    def __init__(self):
        self.my_blocks: List[LegoBlock] = []

    def put_away(self, block: LegoBlock):
        self.my_blocks.append(block)

    def __str__(self) -> str:
        return str(self.my_blocks)

# take blocks of a certain size an dput them form one box to another

    def select(self, selector) -> "LegoBox":
        """Return a box w/ blocks of desired size"""
        keep = []
        my_box = LegoBox()
        for block in self.my_blocks:
            if selector(block):
                my_box.put_away(block)
            else:
                keep.append(block)
        self.my_blocks = keep # replace at the end of loop
        return my_box
 # make select return box with the tiles we want



def main():
    orange_block = LegoBlock("orange", 2)
    blue_block = LegoBlock("blue", 3)
    green_block = LegoBlock("green", 2)
    box = LegoBox()
    box.put_away(orange_block)
    box.put_away(blue_block)
    box.put_away(green_block)
    print(f"Before selecting: {box}")
    selection = box.select(lambda b: b.block_color == 'blue')
    print(f"Big box: {box}")
    print(f"Selection box: {selection}")

if __name__ == "__main__": # if we've imported it, it'll have a different name
    main()
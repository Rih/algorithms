
class Node(object):
    depth = 0
    left = None
    right = None
    
    def __init__(self):
        pass
    
    @classmethod
    def set_child(cls, node):
        cls.left = node
        
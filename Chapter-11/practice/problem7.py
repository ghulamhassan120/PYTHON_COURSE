
class Vector:
    def __init__(self, elements):
        self.elements=elements

    def __len__(self):
        return len(self.elements)
e=Vector([2,3,3])
print(len(e))
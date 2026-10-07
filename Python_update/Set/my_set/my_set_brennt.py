from my_set import MySet

class Rammstein:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Rammstein):
            return False
        return self.id == other.id

p1 = Rammstein(1, "Till Lindemann")
p2 = Rammstein(2, "Richard Kruspe")
p3 = Rammstein(1, "Till Lindemann")

my_set_brennt = MySet()
my_set_brennt.add(p1)
my_set_brennt.add(p2)
my_set_brennt.add(p3)

for member in my_set_brennt:
    print(f"ID: {member.id}, Name: {member.name}")
class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


Animals = Enum(["DOG", "CAT", "HORSE"])
a = { Animals.DOG: "Dog"}
print Animals.DOG, a[Animals.DOG]

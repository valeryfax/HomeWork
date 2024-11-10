class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floors):
        self.new_floors = new_floors
        if 0 < new_floors <= self.floors:
            for i in range(1, int(new_floors) + 1):
                print(i)
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(6)
h2.go_to(10)

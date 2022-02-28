__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


def contract(needs, specialists):
    specialist_dict = {}
    for specialist in specialists:
        profession = specialist.profession()
        name = specialist.name
        price = specialist.price
        for need in needs:
            if need == profession:
                if profession in specialist_dict.keys():
                    if price < specialist_dict[profession][1]:
                        specialist_dict[profession] = [name, price]
                    else:
                        continue
                else:
                    specialist_dict[profession] = [name, price]
    contracts = [s[0] for s in specialist_dict.values()]
    return contracts


class Homeowner():
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs


class Specialist:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Electrician(Specialist):
    def profession(self):
        return "electrician"


class Painter(Specialist):
    def profession(self):
        return "painter"


class Plumber(Specialist):
    def profession(self):
        return "plumber"


alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
candice = Homeowner("Candice Candicedottir", "Candicelane 312", ["electrician", "painter"])

alice = Electrician("Alice Aliceville", 30)
bob = Painter("Bob Bobsville", 20)
craig = Plumber("Craig Craigsville", 30)
rachel = Electrician("Rachel Rachelville", 20)
specialists = [alice, bob, craig, rachel]

print("Alfred's contracts:", contract(alfred.needs, specialists))
print("Bert's contracts:", contract(bert.needs, specialists))
print("Candice's contracts:", contract(candice.needs, specialists))

import random

class Pet:
    def __init__(self, pet_type, name, personality):
        self.pet_type = pet_type
        self.name = name
        self.personality = personality
        self.hunger = 50
        self.happiness = 50
        self.tricks = []

    def feed(self):
        self.hunger -= random.randint(5, 15)
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.happiness += random.randint(5, 15)
        if self.happiness > 100:
            self.happiness = 100

    def teach_trick(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)

    def do_trick(self):
        if self.tricks:
            return random.choice(self.tricks)
        else:
            return "No tricks learned yet!"

class Player:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def adopt_pet(self, pet):
        self.pets.append(pet)

    def interact_with_pet(self, pet_name, action):
        for pet in self.pets:
            if pet.name == pet_name:
                if action == "feed":
                    pet.feed()
                elif action == "play":
                    pet.play()
                elif action.startswith("teach"):
                    trick = action.split(" ")[1]
                    pet.teach_trick(trick)
                return

# Sample usage
player1 = Player("Charan")
pet1 = Pet("Bittu", "Chimtu", "Pandu")
player1.adopt_pet(pet1)

print(f"{player1.name} adopts a {pet1.pet_type} named {pet1.name} with {pet1.personality} personality.")

player1.interact_with_pet("Buddy", "feed")
player1.interact_with_pet("Buddy", "play")
player1.interact_with_pet("Buddy", "teach sit")
player1.interact_with_pet("Buddy", "teach roll over")

print(f"{pet1.name} knows the following tricks: {', '.join(pet1.tricks)}")
print(f"{pet1.name} is feeling {pet1.happiness}% happy and {pet1.hunger}% hungry.")
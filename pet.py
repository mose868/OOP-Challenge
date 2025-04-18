class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # range for hunger
        self.energy = 5  # range for energy
        self.happiness = 5  # range for happiness
        self.tricks = []  # list storing tricks
        print(f"Pet {name} has been created!")
        
    def eat(self):
        '''feed the pet to reduce hunger and increase happiness'''
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        return f"{self.name} has been fed and is happier now"
    
    def sleep(self):
        '''Pet sleeps to gain energy'''
        self.energy = min(10, self.energy + 5)
        return f"{self.name} has slept and is now energized"
    
    def play(self):
        '''play with the pet to increase happiness but consume energy and increase hunger'''
        if self.energy < 2:
            return f"{self.name} is too tired to play right now"
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        return f"{self.name} says it was fun playing with you"
    
    def get_status(self):
        '''display the current status'''
        hunger_status = "full" if self.hunger <= 2 else "hungry" if self.hunger >= 8 else "ok"
        energy_status = "tired" if self.energy <= 2 else "energetic" if self.energy >= 8 else "ok"
        happiness_status = "sad" if self.happiness <= 2 else "happy" if self.happiness >= 8 else "ok"
        status = f"Status of {self.name}: \n"
        status += f"Hunger: {self.hunger}/10 ({hunger_status}) \n"
        status += f"Energy: {self.energy}/10 ({energy_status}) \n"
        status += f"Happiness: {self.happiness}/10 ({happiness_status})"
        return status
    
    def train(self, trick):
        '''teach the pet a new trick'''
        if trick in self.tricks:
            return f"{self.name} already knows how to {trick}"
        if self.energy < 3:
            return f"{self.name} is too tired to learn"
        
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 3)
        self.happiness = min(10, self.happiness + 1)
        return f"{self.name} has learned how to {trick}"
    
    def show_tricks(self):
        '''show all tricks'''
        if not self.tricks:
            return f"{self.name} has not learned any tricks yet"
        
        tricks_list = ", ".join(self.tricks)
        return f"{self.name} knows the following tricks: {tricks_list}"
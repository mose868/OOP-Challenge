# Import the Pet class from pet.py
from pet import Pet

# Interactive Pet Simulator
print("Welcome to the Virtual Pet Simulator!")
pet_name = input("Please enter a name for your pet: ")

# Create a new pet with the user's chosen name
my_pet = Pet(pet_name)

# Main interaction loop
while True:
    print("\nWhat would you like to do with your pet?")
    print("1. Check pet status")
    print("2. Feed pet")
    print("3. Play with pet")
    print("4. Train pet")
    print("5. Show tricks")
    print("6. Let pet sleep")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == '1':
        print("\n" + my_pet.get_status())
    
    elif choice == '2':
        print("\n" + my_pet.eat())
    
    elif choice == '3':
        print("\n" + my_pet.play())
    
    elif choice == '4':
        trick = input("What trick would you like to teach? ")
        print("\n" + my_pet.train(trick))
    
    elif choice == '5':
        print("\n" + my_pet.show_tricks())
    
    elif choice == '6':
        print("\n" + my_pet.sleep())
    
    elif choice == '7':
        print(f"\nGoodbye! Thanks for taking care of {my_pet.name}!")
        break
    
    else:
        print("\nInvalid choice. Please enter a number between 1 and 7.")
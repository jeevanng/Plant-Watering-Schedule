import json
from schedule_functions import PlantSchedule

file_name = "data.json"

# Check/create the .json file
schedule = PlantSchedule(file_name)


def create_menu():
    print("1. Enter 1 to Add a new plant to your schedule")
    print("2. Enter 2 to Remove a plant from your schedule")
    print("3. Enter 3 to View which plants need watering today")
    print("4. Enter 4 to Mark a plant as watered")
    print("5. Enter 5 to Update the amount of water needed for a plant")
    print("6. Enter 6 to View entire plant list")
    print("7. Enter 7 to Exit the program")
    print("--------------------------------")
    choice = input("Enter your selection: ")
    return choice


user_choice = ""

while user_choice != "7":
    user_choice = create_menu()

    if user_choice == "1":
        schedule.add_plant()
    elif user_choice == "2":
        schedule.remove_plant()
    elif user_choice == "3":
        schedule.plants_need_watering()
    elif user_choice == "4":
        schedule.water_plant()
    elif user_choice == "5":
        schedule.update_water_needed()
    elif user_choice == "6":
        schedule.view_all_plants()
    elif user_choice == "7":
        continue
    else:
        print("Invalid input. Please enter a number between 1-7")

    print("--------------------------------")
    input("Press enter to continue...")

print("Thank you for using the plant watering schedule. See you next time!")

import json
import colored
import style 

from schedule_functions import PlantSchedule
from colored import fg, bg, attr
from colored import stylize

angry = bg("indian_red_1a") + fg("white") + colored.attr("bold")
invalid = colored.fg("red")
text = colored.fg(107)
selection = colored.fg(3) + colored.attr("bold")

file_name = "data.json"
# Check/create the .json file
schedule = PlantSchedule(file_name)


def create_menu():
    print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")
    print(stylize("HELLO! Welcome to your Plant Watering Schedule.", angry))
    print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")
    print(style.bold("1.") + (stylize(" Enter 1 to Add a new plant to your schedule", text)))
    print(style.bold("2.") + (stylize(" Enter 2 to Remove a plant from your schedule", text)))
    print(style.bold("3.") + (stylize(" Enter 3 to View which plants need watering today", text)))
    print(style.bold("4.") + (stylize(" Enter 4 to Mark a plant as watered", text)))
    print(style.bold("5.") + (stylize(" Enter 5 to Update the amount of water needed for a plant", text)))
    print(style.bold("6.") + (stylize(" Enter 6 to View entire plant list", text)))
    print(style.bold("7.") + (stylize(" Enter 7 to Exit the program", text)))
    print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")
    choice = input(stylize("Enter your selection: ", selection))
    print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")
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
        print(stylize("Invalid input. Please enter a number between 1-7", invalid))

    print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")
    input("Press enter to continue...")

print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")
print(stylize("Thank you for using the plant watering schedule. See you next time!", angry))
print(f"{fg(1)}--------------------------------------------------------------{attr(0)}")

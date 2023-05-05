import json
import colored

from datetime import datetime, date, timedelta
from colored import fg, bg, attr
from colored import stylize

angry = bg("indian_red_1a") + fg("white") + colored.attr("bold")
invalid = colored.fg("red")
text = colored.fg(107)
selection = colored.fg(3) + colored.attr("bold")


class PlantSchedule:
    def __init__(self, file_name):
        self.file_name = file_name

        file_name = "data.json"
        data = []

        # Check to see if .json file exists
        try:
            with open(self.file_name) as f:
                schedule_data = json.load(f)
            # If it exists, then all fine

        # If it does not exit, create and write new file
        except FileNotFoundError as e:
            with open(self.file_name, "w") as f:
                json.dump(data, f)

    # Function to add new plant to schedule
    def add_plant(self):
        print(
            f"{fg(1)}--------------------------------------------------------------{attr(0)}")
        print(stylize("Add plant to Watering Schedule", angry))
        name = input(stylize("Enter name of plant: ", text))

        print(f"You entered {name}.")
        print(
            f"{fg(1)}--------------------------------------------------------------{attr(0)}")

        while True:
            frequency = input(
                stylize("Enter frequency of watering (weekly, fortnightly or monthly): ", text))
            try:
                if frequency.lower() == "q" or frequency.lower() == "quit":
                    exit()
                if frequency.lower() not in ["weekly", "fortnightly", "monthly"]:
                    raise ValueError(stylize(
                        "Invalid input. Please enter 'weekly', 'fortnightly' or 'monthly'. \nOtherwise type 'q' or 'quit' to exit to main menu", invalid))
                break
            except ValueError as e:
                print(e)

        print(f"You entered the frequency as {frequency}.")
        print(
            f"{fg(1)}--------------------------------------------------------------{attr(0)}")

        while True:
            last_watered_str = input(stylize(
                "Enter the date of when the plant was last watered in this format (YYYY-MM-DD): ", text))
            if last_watered_str.lower() == "q" or last_watered_str.lower() == "quit":
                exit()
            try:
                last_watered = datetime.strptime(last_watered_str, '%Y-%m-%d')
                break
            except ValueError as e:
                print(stylize(
                    "Invalid input! Please enter the date in the format YYYY-MM-DD. \nType 'q' or 'quit' to exit to main menu.", invalid))

        print(f"{name} was last watered on {last_watered_str}.")
        print(
            f"{fg(1)}--------------------------------------------------------------{attr(0)}")

        while True:
            amount_of_water = input(
                stylize("Enter how much water the plant needs (mL): ", text))
            if amount_of_water.lower() == "q" or amount_of_water.lower() == "quit":
                exit()
            try:
                int_amount_of_water = int(amount_of_water)
                if int_amount_of_water >= 0:
                    break
            except ValueError as e:
                print(stylize("Invalid input! Please enter a number greater than or equal to 0. \nType 'q' or 'quit' to exit to main menu and start again.", invalid))

        print(f"This plant needs {amount_of_water} mL every {frequency[:-2]}.")
        print(
            f"{fg(1)}--------------------------------------------------------------{attr(0)}")

        with open(self.file_name) as f:
            data = json.load(f)
            data.append({
                "Name": name,
                "Frequency": frequency,
                "Last_Watered": last_watered_str,
                "Water_Needed": amount_of_water
            })

        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file,
                      indent=4,
                      separators=(',', ': '))

    # Function to remove plant from schedule
    def remove_plant(self):
        print(stylize("Remove plant from Watering Schedule", angry))
        name = input(stylize(
            "Enter the name of the plant you wish to remove from the watering schedule (case sensitive): ", text))
        plant_list = []

        with open(self.file_name) as f:
            data = json.load(f)
            for plant in data:
                if name != plant["Name"]:
                    plant_list.append(plant)

        with open(self.file_name, "w") as json_file:
            json.dump(plant_list, json_file,
                      indent=4,
                      separators=(',', ': '))

    # Function to see which plants need watering
    def plants_need_watering(self):
        now = datetime.now()
        print(stylize("These plants need to be watered today;", angry))

        with open(self.file_name) as f:
            data = json.load(f)

        for plant in data:
            last_watered_date_time = datetime.strptime(
                plant["Last_Watered"], '%Y-%m-%d')
            difference_days = (now - last_watered_date_time).days

            if plant["Frequency"].lower() == "weekly" and difference_days >= 7 or plant["Frequency"].lower() == "fortnightly" and difference_days >= 14 or plant["Frequency"].lower() == "monthly" and difference_days >= 30:
                print(
                    f"{plant['Name']}, last watered {difference_days} days ago ({plant['Frequency']} schedule)")

    # Function to indicate which plant has been watered
    def water_plant(self):
        print(stylize("Indicate that the plant has been watered", angry))
        name = input(stylize(
            "Type the name of which plant has been watered (case sensitive): ", text))
        today = date.today()
        today_str = today.strftime('%Y-%m-%d')

        with open(self.file_name) as f:
            data = json.load(f)

            for plant in data:
                if name == plant["Name"]:
                    plant["Last_Watered"] = today_str
                    break

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file,
                      indent=4,
                      separators=(',', ': '))

        print(f"{name} has been marked as watered.")

    # Function to update how much water a plant needs
    def update_water_needed(self):
        print(stylize("Update amount of water needed for a plant", angry))
        name = input(stylize(
            "Enter the name (case sensitive) of the plant for which you would like to update the watering amount: ", text))

        with open(self.file_name) as f:
            data = json.load(f)

            while True:
                amount_of_water = input(
                    stylize("Enter how much water the plant needs (mL): ", text))
                if amount_of_water.lower() == "q" or amount_of_water.lower() == "quit":
                    exit()
                try:
                    int_amount_of_water = int(amount_of_water)
                    if int_amount_of_water >= 0:
                        break
                except ValueError as e:
                    print(stylize(
                        "Invalid input! Please enter a number greater than or equal to 0. \nType 'q' or 'quit' to exit to main menu and start again.", invalid))

            for plant in data:
                if name == plant["Name"]:
                    plant["Water_Needed"] = amount_of_water
                    break

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file,
                          indent=4,
                          separators=(',', ': '))

        print(f"{name} has been updated to require {amount_of_water} mL of water.")

    # Function to view entire plant list
    def view_all_plants(self):

        with open(self.file_name) as f:
            data = json.load(f)

            print(stylize("Your watering schedule contains the following plants;", angry))
            for plant in data:
                print(
                    f"{plant['Name']}, last watered {plant['Last_Watered']} ({plant['Frequency']} schedule)")

import json
from datetime import datetime, date, timedelta 


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
        print("Add plant to Watering Schedule")
        name = input("Enter name of plant: ")
        print(f"You entered {name}.")
        print("-------------------------------------------")

        while True:
            frequency = input("Enter frequency of watering (weekly, fortnightly or monthly): ") 
            try: 
                if frequency.lower() == "q" or frequency.lower() == "quit":
                    exit()
                if frequency.lower() not in ["weekly", "fortnightly", "monthly"]:
                    raise ValueError("Invalid input. Please enter 'weekly', 'fortnightly' or 'monthly'. \nOtherwise type 'q' or 'quit' to exit to main menu")
                break
            except ValueError as e:
                print(e)
        print(f"You entered the frequency as {frequency}.")
        print("-------------------------------------------")

        while True:
            last_watered_str = input("Enter the date of when the plant was last watered in this format (YYYY-MM-DD): ")
            if last_watered_str.lower() == "q" or last_watered_str.lower() == "quit":
                exit()
            try:
                last_watered = datetime.strptime(last_watered_str, '%Y-%m-%d')
                break
            except ValueError as e:
                print("Invalid input! Please enter the date in the format YYYY-MM-DD. \nType 'q' or 'quit' to exit to main menu.")

        print(f"{name} was watered on {last_watered_str}.")
        print("-------------------------------------------")

        while True:
            amount_of_water = input("Enter how much water the plant needs (mL): ")
            if amount_of_water.lower() == "q" or amount_of_water.lower() == "quit":
                exit()
            try:
                int_amount_of_water = int(amount_of_water)
                if int_amount_of_water >= 0:
                    break
            except ValueError as e:
                print("Invalid input! Please enter a number greater than or equal to 0. \nType 'q' or 'quit' to exit to main menu and start again.")
        print(f"This plant needs {amount_of_water} mL every {frequency[:-2]}.")
        print("-------------------------------------------")


        
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
                                separators=(',',': '))
                
    def remove_plant(self):
        print("Remove plant from Watering Schedule")
        name = input("Enter the name of the plant you wish to remove from the watering schedule: ")
        plant_list = []

        with open(self.file_name) as f:
            data = json.load(f)
            for plant in data:
                if name != plant["Name"]:
                    plant_list.append(plant)

        with open(self.file_name, "w") as json_file:
            json.dump(plant_list, json_file, 
                                    indent=4,  
                                    separators=(',',': '))
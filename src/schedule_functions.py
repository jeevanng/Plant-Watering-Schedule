import json

class PlantSchedule:
    def __init__(self, file_name):
        self.file_name = file_name
        
        file_name = "data.json"
        data = []

        #Check to see if .json file exists 
        try: 
            with open(file_name) as f:
                schedule_data = json.load(f)

            #If it exists, then all fine
            print("In try block")
            print(schedule_data)

        except FileNotFoundError as e:
            with open(file_name, "w") as f:
                json.dump(data, f)
            print("In except block")

    def add_plant(self):
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
            last_watered = input("Enter when the plant was last watered (number in days): ")
            if last_watered.lower() == "q" or last_watered.lower() == "quit":
                exit()
            try:
                int_last_watered = int(last_watered)
                if int_last_watered >= 0:
                    break
            except ValueError as e:
                print("Invalid input! Please enter a number greater than or equal to 0. \nType 'q' or 'quit' to exit to main menu.")
        print(f"{name} was watered {last_watered} days ago.")
        print("-------------------------------------------")

        while True:
            amount_of_water = input("Enter how much water the plant needs (mL): ")
            if last_watered.lower() == "q" or last_watered.lower() == "quit":
                exit()
            try:
                int_amount_of_water = int(amount_of_water)
                if int_amount_of_water >= 0:
                    break
            except ValueError as e:
                print("Invalid input! Please enter a number greater than or equal to 0. \nType 'q' or 'quit' to exit to main menu and start again.")
        print(f"This plant needs {amount_of_water} mL every {frequency}.")
        print("-------------------------------------------")

        with open(self.file_name) as f:
            schedule_data = json.load(f)

        print(schedule_data)

        print(name)
        print(frequency)
        print(last_watered)
        print(amount_of_water)



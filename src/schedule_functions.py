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


import json 
from schedule_functions import PlantSchedule

file_name = "data.json"

schedule = PlantSchedule(file_name)

schedule.add_plant()
schedule.remove_plant()
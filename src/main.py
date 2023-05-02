import json 
from schedule_functions import PlantSchedule

file_name = "data.json"

schedule = PlantSchedule(file_name)

# schedule.add_plant()
# schedule.remove_plant()
schedule.plants_need_watering()
# schedule.water_plant()
# schedule.update_water_needed()
# schedule.view_all_plants()
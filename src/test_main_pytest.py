import pytest
import json

from schedule_functions import PlantSchedule
from unittest.mock import patch


file_name = "test_data.json"


def test_add_plant():
    with patch('builtins.input', side_effect=["Monstera", "monthly", "2023-04-10", "300"]):
        test_add = PlantSchedule(file_name)
        test_add.add_plant()

    with open(file_name) as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["Name"] == "Monstera"
    assert data[0]["Frequency"] == "monthly"
    assert data[0]["Last_Watered"] == "2023-04-10"
    assert data[0]["Water_Needed"] == "300"

    


def test_remove_plant():
    with patch('builtins.input', side_effect=["Monstera", "monthly", "2023-04-10", "300"]):
        test_add = PlantSchedule(file_name)
        test_add.remove_plant()

    with open(file_name) as f:
        data = json.load(f)

    assert len(data) == 2

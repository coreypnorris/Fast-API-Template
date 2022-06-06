import json
from app.data.schemas import CarOutput

def load_db() -> list[CarOutput]:
    """Load a list of Car objects from a JSON file"""
    with open(".\\app\\json\\cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]


def save_db(cars: list[CarOutput]):
    with open(".\\app\\json\\cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)
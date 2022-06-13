import json
from app.data.schemas import CarOutput, User

def load_cars_db() -> list[CarOutput]:
    with open(".\\app\\json\\cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]


def save_cars_db(cars: list[CarOutput]):
    with open(".\\app\\json\\cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)


def load_users_db() -> list[User]:
    with open(".\\app\\json\\users.json") as f:
        return [User.parse_obj(obj) for obj in json.load(f)]
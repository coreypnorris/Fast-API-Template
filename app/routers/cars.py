from fastapi import HTTPException, APIRouter, Depends
from typing import Optional
from app.data.schemas import CarInput, CarOutput, TripOutput, TripInput, User
from app.data.db import load_cars_db, save_cars_db
from app.routers.auth import get_authenticated_user
from fastapi_pagination import Page, paginate


router = APIRouter(prefix="/api/cars")
db = load_cars_db()


@router.get("/", response_model=Page[CarOutput])
def get_cars() -> list:
    return paginate(db)


@router.get("/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.post("/", response_model=CarOutput)
def add_car(input: CarInput, user: User = Depends(get_authenticated_user)) -> CarOutput:
    new_car = CarOutput(size=input.size, doors=input.doors,
                        fuel=input.fuel, transmission=input.transmission,
                        id=len(db)+1)
    db.append(new_car)
    save_cars_db(db)
    return new_car


@router.delete("/{id}", status_code=204)
def remove_car(id: int, user: User = Depends(get_authenticated_user)) -> None:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_cars_db(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.put("/{id}", response_model=CarOutput)
def change_car(id: int, input: CarInput, user: User = Depends(get_authenticated_user)) -> CarOutput:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        car.fuel = input.fuel
        car.transmission = input.transmission
        car.size = input.size
        car.doors = input.doors
        save_cars_db(db)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


class BadTripException(Exception):
    pass


@router.post("/{car_id}/trips", response_model=TripOutput)
def add_trip(car_id: int, input: TripInput, user: User = Depends(get_authenticated_user)) -> TripOutput:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        output = TripOutput(id=len(car.trips)+1,
                            start=input.start, end=input.end,
                            description=input.description)

        if output.end < output.start:
            raise BadTripException("Trip end before start")

        car.trips.append(output)
        save_cars_db(db)
        return output
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
        
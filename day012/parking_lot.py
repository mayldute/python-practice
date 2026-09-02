"""
Task:
Implement a parking lot management system using object-oriented programming
and algorithms.

Requirements:
- Create `Vehicle`, `ParkingSpot`, and `ParkingLot` classes.
- A Vehicle has a license plate and a vehicle type.
- A ParkingSpot has a number, a spot type, and may contain a vehicle.
- A ParkingLot manages parking spots and parked vehicles.
- License plates must uniquely identify vehicles.
- Spot numbers must be unique.
- A vehicle can only park in a compatible spot.
- A parking spot can contain at most one vehicle.
- A vehicle cannot be parked in multiple spots at the same time.
- Vehicles can be removed from the parking lot.
- The parking lot can find where a vehicle is parked.
- The parking lot can find available compatible spots.
- The parking lot can calculate its occupancy rate.

Rules:

Vehicle:
- License plate cannot be empty.
- Vehicle type must be one of:
    - "car"
    - "motorcycle"
    - "truck"
- Vehicles with the same license plate are considered equal.

ParkingSpot:
- Spot number must be greater than 0.
- Spot type must be one of:
    - "car"
    - "motorcycle"
    - "truck"
- A spot can contain only one vehicle.
- A vehicle can only use a spot with the same type.

ParkingLot:
- Adding a spot with an existing spot number must raise `ValueError`.
- A vehicle that is already parked cannot be parked again.
- Parking a vehicle when no compatible spot is available must raise `ValueError`.
- Removing an unknown vehicle must raise `ValueError`.
- Finding an unknown vehicle returns `None`.
- If there are no available compatible spots, return an empty list.
- If the parking lot has no spots, occupancy rate is `0.0`.

Methods:

Vehicle:
    - `__eq__`

ParkingSpot:
    - store the current vehicle

ParkingLot:
    - `add_spot(spot)`
    - `park_vehicle(vehicle)`
    - `remove_vehicle(license_plate)`
    - `find_vehicle(license_plate)`
    - `available_spots(vehicle_type)`
    - `occupancy_rate()`

Algorithm:
- `park_vehicle()` finds the first available compatible spot.
- `find_vehicle()` searches for the spot containing a particular vehicle.
- `available_spots()` filters spots according to availability and vehicle type.
- `occupancy_rate()` calculates the percentage of occupied spots.
"""

from enum import Enum


class VehicleType(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType) -> None:
        if not license_plate:
            raise ValueError("License plate cannot be empty.")

        if not isinstance(vehicle_type, VehicleType):
            raise TypeError(f"Wrong vehicle type. Choose from: {list(VehicleType)}.")

        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented

        return self.license_plate == other.license_plate


class ParkingSpot:
    def __init__(self, spot_number: int, spot_type: VehicleType) -> None:
        if spot_number <= 0:
            raise ValueError("Spot number must be greater than 0.")

        if not isinstance(spot_type, VehicleType):
            raise TypeError(f"Wrong spot type. Choose from: {list(VehicleType)}.")

        self.spot_number = spot_number
        self.spot_type = spot_type
        self.current_vehicle: Vehicle | None = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ParkingSpot):
            return NotImplemented

        return self.spot_number == other.spot_number


class ParkingLot:
    def __init__(self) -> None:
        self.spots: list[ParkingSpot] = []

    def _find_vehicle(self, license_plate: str) -> Vehicle | None:
        for spot in self.spots:
            if (
                spot.current_vehicle is not None
                and spot.current_vehicle.license_plate == license_plate
            ):
                return spot.current_vehicle

        return None

    def _find_spot(self, license_plate: str) -> ParkingSpot | None:
        for spot in self.spots:
            if (
                spot.current_vehicle is not None
                and spot.current_vehicle.license_plate == license_plate
            ):
                return spot

        return None

    def add_spot(self, spot: ParkingSpot) -> None:
        for existing_spot in self.spots:
            if existing_spot == spot:
                raise ValueError("Spot has already been added.")

        self.spots.append(spot)

    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self._find_vehicle(vehicle.license_plate) is not None:
            raise ValueError("Vehicle has already been parked.")

        for spot in self.spots:
            if spot.spot_type == vehicle.vehicle_type and spot.current_vehicle is None:
                spot.current_vehicle = vehicle
                return

        raise ValueError("No compatible spots available.")

    def remove_vehicle(self, license_plate: str) -> None:
        spot = self._find_spot(license_plate)

        if spot is None:
            raise ValueError("Unknown vehicle.")

        spot.current_vehicle = None

    def find_vehicle(self, license_plate: str) -> ParkingSpot | None:
        return self._find_spot(license_plate)

    def available_spots(self, vehicle_type: VehicleType) -> list[ParkingSpot]:
        return [
            spot
            for spot in self.spots
            if (spot.spot_type == vehicle_type and spot.current_vehicle is None)
        ]

    def occupancy_rate(self) -> float:
        if not self.spots:
            return 0.0

        occupied = sum(spot.current_vehicle is not None for spot in self.spots)

        return occupied / len(self.spots) * 100

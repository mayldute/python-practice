"""
Elevator System

Task:
    Build a system that manages elevators in a building.

Requirements:

    Elevator:
        - Has an ID.
        - Has a current floor.
        - Has a maximum floor.
        - Has a state: IDLE or OUT_OF_SERVICE.
        - Can move to a requested floor.
        - Cannot move outside the building's floor range.
        - Cannot move if it is OUT_OF_SERVICE.
        - Can be taken out of service and returned to service.

    ElevatorSystem:
        - Stores multiple elevators.
        - Can add an elevator.
        - Can find an elevator by ID.
        - Can request an elevator from a specific floor.
        - The requested elevator should be selected based on:
            1. Prefer an IDLE elevator.
            2. Among suitable elevators, choose the one
               closest to the requested floor.
        - Can display all available elevators.
        - Can calculate how many elevators are currently in service.

    Additional rules:
        - Elevator IDs must be unique.
        - Two elevators cannot have the same ID.
        - Invalid floors should raise an appropriate exception.
        - Trying to move an OUT_OF_SERVICE elevator should raise an exception.
        - If no suitable elevator exists, the system should indicate that
          no elevator is available.
"""

from enum import Enum


class ElevatorState(Enum):
    idle = "IDLE"
    out_of_service = "OUT_OF_SERVICE"


class Elevator:
    def __init__(self, elevator_id: str, maximum_floor: int) -> None:
        if not elevator_id:
            raise ValueError("ID can not be empty.")

        if maximum_floor <= 0:
            raise ValueError("Maximum floor must be greater than 0.")

        self.elevator_id = elevator_id
        self.maximum_floor = maximum_floor
        self.current_floor: int = 1
        self.state: ElevatorState = ElevatorState.idle

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Elevator):
            return NotImplemented

        return self.elevator_id == other.elevator_id

    def move_elevator(self, floor: int) -> None:
        if self.state is ElevatorState.out_of_service:
            raise ValueError("Elevator out of service.")

        if floor > self.maximum_floor or floor < 1:
            raise ValueError("Elevator cannot move outside the building's floor range.")

        self.current_floor = floor
        self.state = ElevatorState.idle

    def take_out_of_service(self) -> None:
        if self.state is ElevatorState.out_of_service:
            raise ValueError("Elevator has already taken out of service.")

        self.state = ElevatorState.out_of_service

    def return_to_service(self) -> None:
        if self.state is ElevatorState.out_of_service:
            self.state = ElevatorState.idle
            return

        raise ValueError("Elevator has already returned to service.")


class ElevatorSystem:
    def __init__(self) -> None:
        self.elevators: list[Elevator] = []

    def add_elevator(self, elevator: Elevator) -> None:
        for existing_elevator in self.elevators:
            if existing_elevator == elevator:
                raise ValueError("Elevator already added.")

        self.elevators.append(elevator)

    def find_elevator(self, elevator_id: str) -> Elevator:
        for existing_elevator in self.elevators:
            if existing_elevator.elevator_id == elevator_id:
                return existing_elevator

        raise ValueError("Elevator not found.")

    def available_elevators(self) -> list[Elevator]:
        return [
            elevator
            for elevator in self.elevators
            if elevator.state is ElevatorState.idle
        ]

    def currently_in_service(self) -> int:
        return len(
            [
                elevator
                for elevator in self.elevators
                if elevator.state is not ElevatorState.out_of_service
            ]
        )

    def request_elevator(self, floor: int) -> None:
        free_elevators = self.available_elevators()

        free_elevators = [
            elevator for elevator in free_elevators if elevator.maximum_floor >= floor
        ]

        if not free_elevators:
            raise ValueError("No available elevators.")

        elevator = min(
            free_elevators, key=lambda elevator: abs(elevator.current_floor - floor)
        )
        elevator.move_elevator(floor)

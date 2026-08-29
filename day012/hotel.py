"""
Task:
Implement a simple hotel reservation system using object-oriented
programming and algorithms.

Requirements:
- Create `Room`, `Guest`, and `Hotel` classes.
- A Room has a number, a room type, and a price per night.
- A Guest has an ID and a name.
- A Hotel manages rooms, guests, and reservations.
- A guest can reserve a room for a specific number of nights.
- A room can have only one active reservation at a time.
- A guest can have multiple reservations.
- The hotel can calculate the total cost of a reservation.
- The hotel can find the most expensive available room.
- The hotel can find all rooms currently reserved by a guest.
"""


class Room:
    def __init__(self, number: int, type: str, price_per_night: float) -> None:
        if number <= 0:
            raise ValueError("Room number must be positive.")

        if not type:
            raise ValueError("Room type can not be empty.")

        if price_per_night <= 0:
            raise ValueError("Price per night must be greater than 0.")

        self.number = number
        self.type = type
        self.price_per_night = price_per_night
        self.reservation: tuple[Guest, int] | None = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Room):
            return NotImplemented

        return self.number == other.number


class Guest:
    def __init__(self, guest_id: str, name: str) -> None:
        if not guest_id:
            raise ValueError("Guest ID cannot be empty.")

        if not name:
            raise ValueError("Guest name cannot be empty.")

        self.guest_id = guest_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Guest):
            return NotImplemented

        return self.guest_id == other.guest_id


class Hotel:
    def __init__(self) -> None:
        self.rooms: list[Room] = []
        self.guests: list[Guest] = []

    def _find_room(self, room_number: int) -> Room | None:
        for room in self.rooms:
            if room.number == room_number:
                return room

        return None

    def _find_guest(self, guest_id: str) -> Guest | None:
        for guest in self.guests:
            if guest.guest_id == guest_id:
                return guest

        return None

    def add_room(self, room: Room) -> None:
        for existing_room in self.rooms:
            if existing_room == room:
                raise ValueError("Room has already added to hotel.")

        self.rooms.append(room)

    def add_guest(self, guest: Guest) -> None:
        for existing_guest in self.guests:
            if existing_guest == guest:
                raise ValueError("Guest has already added to hotel.")

        self.guests.append(guest)

    def reserve_room(self, guest_id: str, room_number: int, nights: int) -> None:
        guest = self._find_guest(guest_id)
        room = self._find_room(room_number)

        if guest is None:
            raise ValueError("Guest does not exist in hotel.")

        if room is None:
            raise ValueError("Room does not exist in hotel.")

        if nights <= 0:
            raise ValueError("Nights must be greater than 0.")

        if room.reservation is not None:
            raise ValueError("An already reserved room cannot be reserved again.")

        room.reservation = tuple(guest, nights)

    def cancel_reservation(self, room_number: int) -> None:
        room = self._find_room(room_number)

        if room is None:
            raise ValueError("Room does not exist in hotel.")

        if room.reservation is None:
            raise ValueError("Room is not reserved.")

        room.reservation = None

    def reservation_cost(self, room_number: int) -> float:
        room = self._find_room(room_number)

        if room is None:
            raise ValueError("Room does not exist in hotel.")

        if room.reservation is None:
            raise ValueError("Room is not reserved currently.")

        return room.price_per_night * room.reservation[-1]

    def guest_rooms(self, guest_id: str) -> list[Room]:
        guest = self._find_guest(guest_id)

        if guest is None:
            raise ValueError("Guest does not exist in hotel.")

        reserved_rooms = []

        for room in self.rooms:
            if room.reservation is not None and room.reservation[0] == guest:
                reserved_rooms.append(room)

        return reserved_rooms

    def most_expensive_available_room(self) -> Room | None:
        available_rooms = [room for room in self.rooms if room.reservation is None]

        if not available_rooms:
            return None

        return max(available_rooms, key=lambda room: room.price_per_night)

"""
Smart Home System

Task:
    Build a system that manages smart devices in a house.

Requirements:

    Device:
        - Has a unique ID.
        - Has a name.
        - Has a state: ON or OFF.
        - Can be turned on.
        - Can be turned off.
        - Can report its current state.

    Light:
        - Inherits from Device.
        - Has a brightness level from 0 to 100.
        - Can change its brightness.
        - Brightness cannot be changed if the light is OFF.

    Thermostat:
        - Inherits from Device.
        - Has a target temperature.
        - Can change the target temperature.
        - The target temperature must be between 10 and 30 degrees.

    SmartHome:
        - Stores multiple devices.
        - Can add a device.
        - Device IDs must be unique.
        - Can find a device by ID.
        - Can turn all devices on.
        - Can turn all devices off.
        - Can return all currently active devices.
        - Can count how many devices are currently ON.

Additional rules:
    - An empty device ID should raise ValueError.
    - An empty device name should raise ValueError.
    - Adding a device with an existing ID should raise ValueError.
    - Finding a missing device should raise ValueError.
    - Invalid brightness or temperature should raise ValueError.
"""


class Device:
    def __init__(self, device_id: str, name: str) -> None:
        if not device_id or not name:
            raise ValueError("Device must have ID and name.")

        self.device_id = device_id
        self.name = name
        self.state: bool = False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Device):
            return NotImplemented

        return self.device_id == other.device_id

    def turn_on(self) -> None:
        if self.state:
            raise ValueError("Device has already turned on.")

        self.state = True

    def turn_off(self) -> None:
        if not self.state:
            raise ValueError("Device has already turned off.")

        self.state = False

    def current_state(self) -> bool:
        return self.state


class Light(Device):
    def __init__(self, device_id: str, name: str, brightness_level: int) -> None:
        if brightness_level < 0 or brightness_level > 100:
            raise ValueError("Brightness level must be from 0 to 100.")

        super().__init__(device_id, name)
        self.brightness_level = brightness_level

    def change_brightness(self, brightness_level: int) -> None:
        if not self.state:
            raise ValueError("Light is off.")

        if brightness_level < 0 or brightness_level > 100:
            raise ValueError("Brightness level must be from 0 to 100.")

        self.brightness_level = brightness_level


class Thermostat(Device):
    def __init__(self, device_id: str, name: str, target_temp: int) -> None:
        if target_temp < 10 or target_temp > 30:
            raise ValueError(
                "The target temperature must be between 10 and 30 degrees."
            )

        super().__init__(device_id, name)
        self.target_temp = target_temp

    def change_target_temp(self, target_temp: int) -> None:
        if not self.state:
            raise ValueError("Thermostat is off.")

        if target_temp < 10 or target_temp > 30:
            raise ValueError(
                "The target temperature must be between 10 and 30 degrees."
            )

        self.target_temp = target_temp


class SmartHome:
    def __init__(self) -> None:
        self.devices: list[Device] = []

    def add_device(self, device: Device) -> None:
        for existing_device in self.devices:
            if existing_device == device:
                raise ValueError("Device has already added to SmartHome.")

        self.devices.append(device)

    def find_device(self, device_id: str) -> Device:
        for device in self.devices:
            if device.device_id == device_id:
                return device

        raise ValueError("Device not found.")

    def turn_on(self) -> None:
        for device in self.devices:
            if not device.state:
                device.turn_on()

    def turn_off(self) -> None:
        for device in self.devices:
            if device.state:
                device.turn_off()

    def currently_active_devices(self) -> list[Device]:
        return [device for device in self.devices if device.state]

    def count_active_devices(self) -> int:
        return len(self.currently_active_devices())

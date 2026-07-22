class TrafficDevice:
    """Parent Class representing a generic traffic device."""
    def activate(self):
        print("Device activated.")

class TrafficLight(TrafficDevice):
    """Child Class representing a traffic signal light."""
    def activate(self):
        print("Traffic Light: Signals set to GREEN for smooth flow.")

class SpeedCamera(TrafficDevice):
    """Child Class representing a radar speed tracking camera."""
    def activate(self):
        print("Speed Camera: Monitoring vehicular speed and recording violations.")

class PedestrianSignal(TrafficDevice):
    """Child Class representing a crosswalk signal."""
    def activate(self):
        print("Pedestrian Signal: 'WALK' sign displayed for crosswalk access.")


class EmergencySiren(TrafficDevice):
    """Child Class representing an emergency warning siren."""
    def activate(self):
        print("Emergency Siren: BLARED! Emergency vehicle approaching clear lanes!")



if __name__ == "__main__":
    devices = [
        TrafficLight(),
        SpeedCamera(),
        PedestrianSignal(),
        EmergencySiren()  
    ]

    print("--- Activating Smart City Traffic Devices ---")
    for device in devices:
        device.activate()
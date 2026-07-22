class TrafficDevice:
    def activate(self):
        print("Device activated.")

class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic Light: Signals set to GREEN for smooth flow.")

class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed Camera: Monitoring vehicular speed and recording violations.")

class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian Signal: 'WALK' sign displayed for crosswalk access.")

class EmergencySiren(TrafficDevice):
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

import time
import random
import csv
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None

API_URL = "https://example.com/emergency_signal"


class SmartTrafficLight:
    def __init__(self):
        self.green_time = 10
        self.red_time = 10
        self.traffic_density = "low"
        self.ambulance_incoming = False
        self.motorcade_incoming = False
        self.speed_violators = 0
        self.data_file = "traffic_data.csv"
        self.setup_csv()

    def setup_csv(self):
        try:
            with open(self.data_file, "x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Timestamp",
                    "Traffic Density",
                    "Green Time",
                    "Ambulance",
                    "Motorcade",
                    "Speed Violators"
                ])
        except FileExistsError:
            pass

    def check_emergency_signal(self):
        if not requests:
            self.ambulance_incoming = False
            self.motorcade_incoming = False
            return

        try:
            response = requests.get(API_URL, timeout=2)
            data = response.json()
            self.ambulance_incoming = bool(data.get("ambulance"))
            self.motorcade_incoming = bool(data.get("motorcade"))
        except Exception:
            self.ambulance_incoming = False
            self.motorcade_incoming = False

    def read_traffic_sensor(self):
        return random.choice(["low", "medium", "high"])

    def check_speed_violators(self):
        return random.randint(0, 5)

    def adjust_light_timing(self):
        if self.ambulance_incoming:
            self.green_time = 25
            message = "🚑 Ambulance Incoming – Priority Green"
        elif self.motorcade_incoming:
            self.green_time = 30
            message = "🚓 Motorcade Incoming – Road Cleared"
        else:
            density_map = {
                "low": 7,
                "medium": 12,
                "high": 20
            }
            self.green_time = density_map[self.traffic_density]
            message = f"🚦 Traffic: {self.traffic_density.capitalize()}"

        print(f"📟 DISPLAY: {message}")

    def log_traffic_data(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.data_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                self.traffic_density,
                self.green_time,
                self.ambulance_incoming,
                self.motorcade_incoming,
                self.speed_violators
            ])

    def run(self, cycles=10):
        print("🚦 Smart Traffic Light System Online")

        for _ in range(cycles):
            self.check_emergency_signal()
            self.traffic_density = self.read_traffic_sensor()
            self.speed_violators = self.check_speed_violators()
            self.adjust_light_timing()
            self.log_traffic_data()

            print(
                f"🔄 Update | Traffic: {self.traffic_density} "
                f"| Green: {self.green_time}s"
            )

            if self.speed_violators:
                print(f"⚠️ {self.speed_violators} Speeding Vehicles Detected")

            time.sleep(5)


if __name__ == "__main__":
    SmartTrafficLight().run(cycles=20)

""""April 8th, 2021 live coding
Author: Tyler

"""


class Alarm:
    def __init__(self, armed: bool = False):
        self._armed = armed

    def send_alert(self):
        raise NotImplementedError("Each concrete class should implement 'send_alert'")

    def arm(self):
        self._armed = True

    def disarm(self):
        self._armed = False


class CarAlarm(Alarm):
    def send_alert(self):
        if self._armed:
            print("beepbeepBEEEEEP")


class SMS_Alarm(Alarm):
    def send_alert(self):
        if self._armed:
            print("Calling SMS to owner phone...")


class Vehicle:

    def __init__(self, alarm: Alarm = None):
        self.alarms = []
        if alarm:
            self.alarms.append(alarm)

    def install_alarm(self, alarm: Alarm):
        self.alarms.append(alarm)

    def moving(self):
        for alarm in self.alarms:
            alarm.send_alert()

    def alarm_on(self):
        for alarm in self.alarms:
            alarm.arm()

    def alarm_off(self):
        for alarm in self.alarms:
            alarm.disarm()


class Car(Vehicle):

    def __init__(self, model: str, make: str, tier: str, alarm: CarAlarm = None):
        self.model = model
        self.make = make
        self.tier = tier
        super().__init__(alarm)


def main():
    car1 = Car("Prius", "Toyota", "Hatchback")
    car1_alarm = CarAlarm()
    print("Starting...")

    car1.alarm_on()
    car1.moving()
    print("alarming car!")
    car1.install_alarm(car1_alarm)
    car1.alarm_on()
    car1.moving()


if __name__ == "__main__":
    main()

class IPhone:
    __name__ = "iPhone"

    def __init__(self):
        self.connected = False

    def use_lightning(self):
        self.connected = True
        print("Connected to lightning charger")

    def reload(self):
        if self.connected:
            print("Loading...")
            print("Battery recharged.")
        else:
            print("Connect to lighning charger first")


class Android:
    __name__ = "Android"

    def __init__(self):
        self.connected = False

    def use_micro_usb(self):
        self.connected = True
        print("Connected to Micro USB charger")

    def reload(self):
        if self.connected:
            print("Loading...")
            print("Battery recharged.")
        else:
            print("Connect to Micro USB charger first")


class IPhoneAdapter:
    def __init__(self, mobile: IPhone):
        self.cellular = mobile

    def reload(self):
        self.cell.recharge()

    def use_micro_usb(self):
        print("Connected to Micro USB charger")
        self.cellular.use_lightning()


class AndroidLoader:
    def __init__(self):
        self.phone = Android()
        self.phone.use_micro_usb()
        self.phone.recharge()


class IPhoneCharger:
    def __init__(self):
        self.phone = IPhone()
        self.phone.use_lightning()
        self.phone.recharge()


class IPhoneMicroUSBCharger:
    def __init__(self):
        self.phone = IPhone()
        self.telephone_adapter = IPhoneAdapter(self.telephone)
        self.phone_adapter.use_micro_usb()
        self.phone_adapter.recharge()


if __name__ == '__main__':
        print("Recharging Android with MicroUSB")
        AndroidLoader()
        print()

        print("Recharging iPhone with MicroUSB using adapter.")
        IPhoneMicroUSBCharger()
        print()

        print("Recharging iPhone with Lightning.")
        IPhoneCharger()
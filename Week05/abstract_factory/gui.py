from platform import system

# Family Products for Windows
class BottonWindows:
    def __init__(self):
        print("I' m a Windows botton")

class WindowWindows:
    def __init__(self):
        print("I' m a Windows window")

# Family Products for Linux
class BottonLinux:
    def __init__(self):
        print("I' m a Linux botton")

class WindowLinux:
    def __init__(self):
        print("I' m a Linux window")


# Family Products for MacOS
class BottonMac:
    def __init__(self):
        print("I' m a MacOS botton")


class WindowMac:
    def __init__(self):
        print("I' m a MacOs window")


class FactoryGUI:
    """
    Factory Class define OS type and select corretly factory
    """
    def __init__(self):
        if system() == "Windows":
            self.factory = FactoryWindows()
        elif system() == "Linux":
            self.factory = FactoryLinux()
        elif system() == "Darwin":
            self.factory = FactoryMacOS()
        else:
            raise TypeError("OS don't identify.")

    def create_botton(self):
        return self.factory.create_botton()

    def create_windows(self):
        return self.factory.create_windows()


class FactoryWindows:
    """
    Components Factory for Windows OS
    """
    def create_botton(self):
        return BottonWindows()

    def create_windows(self):
        return WindowWindows()


class FactoryLinux:
    """
    Components Factory for Linux OS
    """
    def create_botton(self):
        return BottonLinux()

    def create_windows(self):
        return WindowLinux()


class FactoryMacOS:
    """
    Components Factory for MacOs
    """
    def create_botton(self):
        return BottonMac()

    def create_windows(self):
        return WindowMac()


if __name__ == '__main__':
    factory_gui = FactoryGUI()
    factory_gui.create_windows()
    factory_gui.create_botton()

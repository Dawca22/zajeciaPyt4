class Monitor(object):
    """Monitor komputerowy"""
    def __init__(self, prod, przek, proporcje="16:9"):
        """Tworzy instancję obiektu typu monitor
        :param prod: str - producent
        :param przek: int - przekątna ekranu w calach
        :param proporcje: str - proporcje ekranu, defaultowo 16:9"""

        self.producent = prod
        self.przekatna = przek
        self.proporcje = proporcje
        self.kolor = "czarny"
        self.wlaczony = False

    def wlacz(self):
        if not self.wlaczony:
            self.wlaczony = True
            print(f"Monitor {self.producent} został włączony.")
        else:
            print("Monitor jest już wyłączony")

    def wylacz(self):
        if self.wlaczony:
            self.wlaczony = False
            print(f"Monitor {self.producent} został wyłączony.")
        else:
            print("Już jest przecież włączony")

    def __str__(self):
        return f"Monitor producent: {self.producent} \n"
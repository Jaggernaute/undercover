from src.core.Inspector import Inspector
from src.core.Interactor import Interactor
from src.core.Service import Service


class Game:
    def __init__(self):                        # def __init__(self, config):
        Interactor().call_system(f"Creating... {self}")

        # --------------------------- DATA VARIABLES ---------------------------
        self.players = Service().rules["PLAYERS"]["ROLE_PLAYERS"]
        self.white_players = Service().rules["PLAYERS"]["WHITE_PLAYERS"]
        self.undercover_players = Service().rules["PLAYERS"]["UNDERCOVER_PLAYERS"]
        self.civilian_players = Service().rules["PLAYERS"]["CIVILIAN_PLAYERS"]
        self.roles = Service().rules["ROLES"]

        # --------------------------- RULES VARIABLES ---------------------------
        self.sum_players = 0

    def __enter__(self):
        # self.load()
        Interactor().call_system(f"Opening... {self}")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # self.save_state()
        # self.close()
        if exc_value:
            Inspector().exception(exc_value)
        Interactor().call_system(f"Exiting... {self}")
        return self

    def config(self):
        print(Service().rules)
        # --------------------------- PLAYERS ---------------------------
        self.sum_players = Interactor().call_int_input("Players : ")

        for index in range(1, self.sum_players + 1):
            self.players[Interactor().call_input(f"Name of player ({index}) : ")] = None

        Service().compute_rules()

    def run(self):
        Interactor().call_system(f"Running... {self}")
        print(Service().rules)
        print(Service().words)

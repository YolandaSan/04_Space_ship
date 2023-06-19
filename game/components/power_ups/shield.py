from game.components.power_ups.power_up import Power_up
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(Power_up):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)
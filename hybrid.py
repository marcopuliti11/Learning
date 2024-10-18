from electric import Electric
from petrol import Petrol

class Hybrid(Electric, Petrol):
    pass


nissan = Hybrid()
nissan.can_charge = False
nissan.engine_size = 2500
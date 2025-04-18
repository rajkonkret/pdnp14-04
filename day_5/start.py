# import kl2
#
# kl2.cz1.ruszaj()
import pakiet

# pakiet.powitanie() # AttributeError: module 'pakiet' has no attribute 'powitanie'

from pakiet import fun

fun.powitanie()  # Cześć

import pakiet.fun as pk

pk.powitanie()  # Cześć

# po dodaniu __all__ = ["info"]
import pakiet
pakiet.info()
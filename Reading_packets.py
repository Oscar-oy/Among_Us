import collections

import numpy as np
import pyshark

cap = pyshark.FileCapture('Juego1.pcapng',only_sumaries = True)
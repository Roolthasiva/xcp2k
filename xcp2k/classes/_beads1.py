from xcp2k.inputsection import InputSection
from xcp2k.classes._coord6 import _coord6
from xcp2k.classes._velocity7 import _velocity7


class _beads1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.COORD = _coord6()
        self.VELOCITY = _velocity7()
        self._name = "BEADS"
        self._subsections = {'COORD': 'COORD', 'VELOCITY': 'VELOCITY'}


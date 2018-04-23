from xcp2k.inputsection import InputSection


class _beef5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self._name = "BEEF"
        self._keywords = {'Scale_x': 'SCALE_X'}
        self._attributes = ['Section_parameters']

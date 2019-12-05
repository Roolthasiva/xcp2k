from xcp2k.inputsection import InputSection


class _opbend1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Phi0 = None
        self._name = "OPBEND"
        self._keywords = {'Atoms': 'ATOMS', 'Kind': 'KIND', 'K': 'K', 'Phi0': 'PHI0'}


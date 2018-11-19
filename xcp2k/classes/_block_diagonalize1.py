from xcp2k.inputsection import InputSection


class _block_diagonalize1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Block = []
        self.Ignore_excited = None
        self.Recursive_diagonalization = None
        self._name = "BLOCK_DIAGONALIZE"
        self._keywords = {'Recursive_diagonalization': 'RECURSIVE_DIAGONALIZATION', 'Ignore_excited': 'IGNORE_EXCITED'}
        self._repeated_keywords = {'Block': 'BLOCK'}


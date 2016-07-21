from xcp2k.inputsection import InputSection


class _mol_displacements1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rmbond = None
        self.Rmangle = None
        self.Rmdihedral = None
        self.Rmrot = None
        self.Rmtrans = None
        self._name = "MOL_DISPLACEMENTS"
        self._keywords = {'Rmtrans': 'RMTRANS', 'Rmangle': 'RMANGLE', 'Rmdihedral': 'RMDIHEDRAL', 'Rmbond': 'RMBOND', 'Rmrot': 'RMROT'}

from xcp2k.inputsection import InputSection


class _atom_group3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Coeff = []
        self.Constraint_type = None
        self.Fragment_constraint = None
        self._name = "ATOM_GROUP"
        self._keywords = {'Atoms': 'ATOMS', 'Constraint_type': 'CONSTRAINT_TYPE', 'Fragment_constraint': 'FRAGMENT_CONSTRAINT'}
        self._repeated_keywords = {'Coeff': 'COEFF'}


from xcp2k.inputsection import InputSection


class _bse4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Num_z_vectors = None
        self.Threshold_min_trans = None
        self.Max_iter = None
        self._name = "BSE"
        self._keywords = {'Threshold_min_trans': 'THRESHOLD_MIN_TRANS', 'Max_iter': 'MAX_ITER', 'Num_z_vectors': 'NUM_Z_VECTORS'}
        self._aliases = {'Eps': 'Threshold_min_trans'}


    @property
    def Eps(self):
        """
        See documentation for Threshold_min_trans
        """
        return self.Threshold_min_trans

    @Eps.setter
    def Eps(self, value):
        self.Threshold_min_trans = value
from xcp2k.inputsection import InputSection
from _coulomb1 import _coulomb1
from _exchange1 import _exchange1
from _screening1 import _screening1
from _lr_correction1 import _lr_correction1
from _neighbor_lists2 import _neighbor_lists2
from _memory1 import _memory1
from _print22 import _print22
from _ga1 import _ga1


class _se1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Orthogonal_basis = None
        self.Sto_ng = None
        self.Analytical_gradients = None
        self.Delta = None
        self.Integral_screening = None
        self.Periodic = None
        self.Force_kdso_d_exchange = None
        self.Dispersion = None
        self.Dispersion_parameter_file = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3_scaling = None
        self.COULOMB = _coulomb1()
        self.EXCHANGE = _exchange1()
        self.SCREENING = _screening1()
        self.LR_CORRECTION = _lr_correction1()
        self.NEIGHBOR_LISTS = _neighbor_lists2()
        self.MEMORY = _memory1()
        self.PRINT = _print22()
        self.GA = _ga1()
        self._name = "SE"
        self._keywords = {'Analytical_gradients': 'ANALYTICAL_GRADIENTS', 'Dispersion': 'DISPERSION', 'Integral_screening': 'INTEGRAL_SCREENING', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'Orthogonal_basis': 'ORTHOGONAL_BASIS', 'D3_scaling': 'D3_SCALING', 'Sto_ng': 'STO_NG', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'Periodic': 'PERIODIC', 'Delta': 'DELTA', 'Force_kdso_d_exchange': 'FORCE_KDSO-D_EXCHANGE', 'Dispersion_radius': 'DISPERSION_RADIUS'}
        self._subsections = {'LR_CORRECTION': 'LR_CORRECTION', 'COULOMB': 'COULOMB', 'EXCHANGE': 'EXCHANGE', 'SCREENING': 'SCREENING', 'GA': 'GA', 'MEMORY': 'MEMORY', 'PRINT': 'PRINT', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS'}

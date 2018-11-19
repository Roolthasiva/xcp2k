from xcp2k.inputsection import InputSection
from _program_run_info49 import _program_run_info49
from _forces4 import _forces4
from _grid_information3 import _grid_information3
from _total_numbers1 import _total_numbers1
from _distribution2 import _distribution2
from _distribution2d1 import _distribution2d1
from _distribution1d1 import _distribution1d1
from _stress_tensor1 import _stress_tensor1


class _print68(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info49()
        self.FORCES = _forces4()
        self.GRID_INFORMATION = _grid_information3()
        self.TOTAL_NUMBERS = _total_numbers1()
        self.DISTRIBUTION = _distribution2()
        self.DISTRIBUTION2D = _distribution2d1()
        self.DISTRIBUTION1D = _distribution1d1()
        self.STRESS_TENSOR = _stress_tensor1()
        self._name = "PRINT"
        self._subsections = {'TOTAL_NUMBERS': 'TOTAL_NUMBERS', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'GRID_INFORMATION': 'GRID_INFORMATION', 'DISTRIBUTION1D': 'DISTRIBUTION1D', 'STRESS_TENSOR': 'STRESS_TENSOR', 'FORCES': 'FORCES', 'DISTRIBUTION': 'DISTRIBUTION', 'DISTRIBUTION2D': 'DISTRIBUTION2D'}


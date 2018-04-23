from xcp2k.inputsection import InputSection
from _each265 import _each265


class _ks_csr_write1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Threshold = None
        self.Upper_triangular = None
        self.EACH = _each265()
        self._name = "KS_CSR_WRITE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Upper_triangular': 'UPPER_TRIANGULAR', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Threshold': 'THRESHOLD'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

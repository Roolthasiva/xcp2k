from xcp2k.inputsection import InputSection
from _each378 import _each378


class _fit_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each378()
        self._name = "FIT_BASIS"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

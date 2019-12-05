from xcp2k.inputsection import InputSection
from xcp2k.classes._each64 import _each64


class _coordinates1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Format = None
        self.EACH = _each64()
        self._name = "COORDINATES"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Format': 'FORMAT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']


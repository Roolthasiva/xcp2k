from xcp2k.inputsection import InputSection
from _each353 import _each353


class _cell5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.EACH = _each353()
        self._name = "CELL"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Unit': 'UNIT', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']


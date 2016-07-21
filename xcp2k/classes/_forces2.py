from xcp2k.inputsection import InputSection
from _each87 import _each87


class _forces2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Format = None
        self.EACH = _each87()
        self._name = "FORCES"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Format': 'FORMAT', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

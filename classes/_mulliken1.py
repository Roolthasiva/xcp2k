from xcp2k.inputsection import InputSection
from _each216 import _each216


class _mulliken1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Print_gop = None
        self.Print_all = None
        self.EACH = _each216()
        self._name = "MULLIKEN"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Print_gop': 'PRINT_GOP', 'Print_all': 'PRINT_ALL', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

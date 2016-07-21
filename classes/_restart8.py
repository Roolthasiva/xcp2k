from xcp2k.inputsection import InputSection
from _each141 import _each141


class _restart8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Backup_copies = None
        self.EACH = _each141()
        self._name = "RESTART"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Backup_copies': 'BACKUP_COPIES', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

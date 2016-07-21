from xcp2k.inputsection import InputSection
from _each116 import _each116


class _neighbor_lists1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Sab_orb_full = None
        self.Sab_orb_molecular = None
        self.Sac_kin = None
        self.EACH = _each116()
        self._name = "NEIGHBOR_LISTS"
        self._keywords = {'Sab_orb_full': 'SAB_ORB_FULL', 'Sab_orb_molecular': 'SAB_ORB_MOLECULAR', 'Log_print_key': 'LOG_PRINT_KEY', 'Sac_kin': 'SAC_KIN', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

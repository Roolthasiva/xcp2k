from xcp2k.inputsection import InputSection
from _print53 import _print53


class _localize4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_iter = None
        self.Max_crazy_angle = None
        self.Crazy_scale = None
        self.Crazy_use_diag = None
        self.Use_history = None
        self.Eps_occupation = None
        self.Out_iter_each = None
        self.Eps_localization = None
        self.Min_or_max = None
        self.Method = None
        self.Jacobi_fallback = None
        self.Restart = None
        self.Lochomo_restart_file_name = None
        self.Loclumo_restart_file_name = None
        self.Operator = None
        self.List = []
        self.List_unoccupied = []
        self.States = None
        self.Energy_range = None
        self.PRINT = _print53()
        self._name = "LOCALIZE"
        self._keywords = {'States': 'STATES', 'Eps_localization': 'EPS_LOCALIZATION', 'Loclumo_restart_file_name': 'LOCLUMO_RESTART_FILE_NAME', 'Energy_range': 'ENERGY_RANGE', 'Use_history': 'USE_HISTORY', 'Crazy_use_diag': 'CRAZY_USE_DIAG', 'Out_iter_each': 'OUT_ITER_EACH', 'Max_iter': 'MAX_ITER', 'Crazy_scale': 'CRAZY_SCALE', 'Jacobi_fallback': 'JACOBI_FALLBACK', 'Min_or_max': 'MIN_OR_MAX', 'Max_crazy_angle': 'MAX_CRAZY_ANGLE', 'Lochomo_restart_file_name': 'LOCHOMO_RESTART_FILE_NAME', 'Eps_occupation': 'EPS_OCCUPATION', 'Operator': 'OPERATOR', 'Method': 'METHOD', 'Restart': 'RESTART'}
        self._repeated_keywords = {'List_unoccupied': 'LIST_UNOCCUPIED', 'List': 'LIST'}
        self._subsections = {'PRINT': 'PRINT'}
        self._attributes = ['Section_parameters']

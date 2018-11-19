from xcp2k.inputsection import InputSection
from _each278 import _each278
from _interpolator3 import _interpolator3


class _electric_field_gradient1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Interpolation = None
        self.Gspace_smoothing = None
        self.Debug = None
        self.EACH = _each278()
        self.INTERPOLATOR = _interpolator3()
        self._name = "ELECTRIC_FIELD_GRADIENT"
        self._keywords = {'Gspace_smoothing': 'GSPACE_SMOOTHING', 'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Debug': 'DEBUG', 'Interpolation': 'INTERPOLATION'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']


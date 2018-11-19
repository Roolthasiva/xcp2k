from xcp2k.inputsection import InputSection
from _each363 import _each363


class _total_dipole4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Periodic = None
        self.Reference = None
        self.Reference_point = None
        self.EACH = _each363()
        self._name = "TOTAL_DIPOLE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Reference': 'REFERENCE', 'Reference_point': 'REFERENCE_POINT', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Periodic': 'PERIODIC', 'Add_last': 'ADD_LAST'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Ref_point': 'Reference_point', 'Ref': 'Reference'}
        self._attributes = ['Section_parameters']


    @property
    def Ref(self):
        """
        See documentation for Reference
        """
        return self.Reference

    @property
    def Ref_point(self):
        """
        See documentation for Reference_point
        """
        return self.Reference_point

    @Ref.setter
    def Ref(self, value):
        self.Reference = value

    @Ref_point.setter
    def Ref_point(self, value):
        self.Reference_point = value

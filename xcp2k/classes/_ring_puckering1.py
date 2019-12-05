from xcp2k.inputsection import InputSection
from xcp2k.classes._point16 import _point16


class _ring_puckering1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Coordinate = None
        self.POINT_list = []
        self._name = "RING_PUCKERING"
        self._keywords = {'Atoms': 'ATOMS', 'Coordinate': 'COORDINATE'}
        self._repeated_subsections = {'POINT': '_point16'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point16()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def Points(self):
        """
        See documentation for Atoms
        """
        return self.Atoms

    @Points.setter
    def Points(self, value):
        self.Atoms = value

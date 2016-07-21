from xcp2k.inputsection import InputSection
from _point68 import _point68


class _xyz_outerdiag4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Component_a = None
        self.Component_b = None
        self.Pbc = None
        self.POINT_list = []
        self._name = "XYZ_OUTERDIAG"
        self._keywords = {'Component_b': 'COMPONENT_B', 'Component_a': 'COMPONENT_A', 'Pbc': 'PBC', 'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point68'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point68()
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
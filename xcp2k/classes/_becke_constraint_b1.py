from xcp2k.inputsection import InputSection
from _program_run_info44 import _program_run_info44
from _atom_group3 import _atom_group3
from _dummy_atoms3 import _dummy_atoms3


class _becke_constraint_b1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Strength = None
        self.Target = None
        self.Adjust_size = None
        self.Atomic_radii = None
        self.Should_skip = None
        self.Atomic_charges = None
        self.Cavity_confine = None
        self.Cavity_shape = None
        self.Cavity_use_bohr = None
        self.Cavity_print = None
        self.Cavity_radius = None
        self.Eps_cavity = None
        self.Cutoff_type = None
        self.Global_cutoff = None
        self.Element_cutoff = None
        self.In_memory = None
        self.Fragment_a_file_name = None
        self.Fragment_b_file_name = None
        self.Fragment_a_spin_file = None
        self.Fragment_b_spin_file = None
        self.Flip_fragment_a = None
        self.Flip_fragment_b = None
        self.PROGRAM_RUN_INFO = _program_run_info44()
        self.ATOM_GROUP_list = []
        self.DUMMY_ATOMS_list = []
        self._name = "BECKE_CONSTRAINT_B"
        self._keywords = {'Cavity_use_bohr': 'CAVITY_USE_BOHR', 'Global_cutoff': 'GLOBAL_CUTOFF', 'Strength': 'STRENGTH', 'Fragment_a_file_name': 'FRAGMENT_A_FILE_NAME', 'Fragment_a_spin_file': 'FRAGMENT_A_SPIN_FILE', 'Eps_cavity': 'EPS_CAVITY', 'Element_cutoff': 'ELEMENT_CUTOFF', 'Cutoff_type': 'CUTOFF_TYPE', 'Cavity_radius': 'CAVITY_RADIUS', 'Atomic_charges': 'ATOMIC_CHARGES', 'Cavity_confine': 'CAVITY_CONFINE', 'Fragment_b_spin_file': 'FRAGMENT_B_SPIN_FILE', 'Flip_fragment_b': 'FLIP_FRAGMENT_B', 'Target': 'TARGET', 'Flip_fragment_a': 'FLIP_FRAGMENT_A', 'Cavity_print': 'CAVITY_PRINT', 'Adjust_size': 'ADJUST_SIZE', 'Atomic_radii': 'ATOMIC_RADII', 'Cavity_shape': 'CAVITY_SHAPE', 'In_memory': 'IN_MEMORY', 'Should_skip': 'SHOULD_SKIP', 'Fragment_b_file_name': 'FRAGMENT_B_FILE_NAME'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}
        self._repeated_subsections = {'DUMMY_ATOMS': '_dummy_atoms3', 'ATOM_GROUP': '_atom_group3'}
        self._aliases = {'Fragment_a_file': 'Fragment_a_file_name', 'Fragment_a_spin_file_name': 'Fragment_a_spin_file', 'Fragment_b_spin_file_name': 'Fragment_b_spin_file', 'Fragment_b_file': 'Fragment_b_file_name'}
        self._attributes = ['ATOM_GROUP_list', 'DUMMY_ATOMS_list']

    def DUMMY_ATOMS_add(self, section_parameters=None):
        new_section = _dummy_atoms3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DUMMY_ATOMS_list.append(new_section)
        return new_section

    def ATOM_GROUP_add(self, section_parameters=None):
        new_section = _atom_group3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.ATOM_GROUP_list.append(new_section)
        return new_section


    @property
    def Fragment_a_file(self):
        """
        See documentation for Fragment_a_file_name
        """
        return self.Fragment_a_file_name

    @property
    def Fragment_b_file(self):
        """
        See documentation for Fragment_b_file_name
        """
        return self.Fragment_b_file_name

    @property
    def Fragment_a_spin_file_name(self):
        """
        See documentation for Fragment_a_spin_file
        """
        return self.Fragment_a_spin_file

    @property
    def Fragment_b_spin_file_name(self):
        """
        See documentation for Fragment_b_spin_file
        """
        return self.Fragment_b_spin_file

    @Fragment_a_file.setter
    def Fragment_a_file(self, value):
        self.Fragment_a_file_name = value

    @Fragment_b_file.setter
    def Fragment_b_file(self, value):
        self.Fragment_b_file_name = value

    @Fragment_a_spin_file_name.setter
    def Fragment_a_spin_file_name(self, value):
        self.Fragment_a_spin_file = value

    @Fragment_b_spin_file_name.setter
    def Fragment_b_spin_file_name(self, value):
        self.Fragment_b_spin_file = value
from xcp2k.inputsection import InputSection
from xcp2k.classes._eri_mme_info7 import _eri_mme_info7
from xcp2k.classes._cutoff_calib7 import _cutoff_calib7


class _eri_mme7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_minimax = None
        self.Cutoff = None
        self.Sum_precision = None
        self.Do_calibrate_cutoff = None
        self.Print_calib = None
        self.Debug = None
        self.Debug_tolerance = None
        self.Debug_nsum_max = None
        self.ERI_MME_INFO = _eri_mme_info7()
        self.CUTOFF_CALIB = _cutoff_calib7()
        self._name = "ERI_MME"
        self._keywords = {'N_minimax': 'N_MINIMAX', 'Cutoff': 'CUTOFF', 'Sum_precision': 'SUM_PRECISION', 'Do_calibrate_cutoff': 'DO_CALIBRATE_CUTOFF', 'Print_calib': 'PRINT_CALIB', 'Debug': 'DEBUG', 'Debug_tolerance': 'DEBUG_TOLERANCE', 'Debug_nsum_max': 'DEBUG_NSUM_MAX'}
        self._subsections = {'ERI_MME_INFO': 'ERI_MME_INFO', 'CUTOFF_CALIB': 'CUTOFF_CALIB'}


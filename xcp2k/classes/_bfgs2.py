from xcp2k.inputsection import InputSection
from xcp2k.classes._restart2 import _restart2


class _bfgs2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Trust_radius = None
        self.Use_model_hessian = None
        self.Use_rat_fun_opt = None
        self.Restart_hessian = None
        self.Restart_file_name = None
        self.RESTART = _restart2()
        self._name = "BFGS"
        self._keywords = {'Trust_radius': 'TRUST_RADIUS', 'Use_model_hessian': 'USE_MODEL_HESSIAN', 'Use_rat_fun_opt': 'USE_RAT_FUN_OPT', 'Restart_hessian': 'RESTART_HESSIAN', 'Restart_file_name': 'RESTART_FILE_NAME'}
        self._subsections = {'RESTART': 'RESTART'}


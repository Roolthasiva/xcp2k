from xcp2k.inputsection import InputSection
from _nablavks_cubes1 import _nablavks_cubes1
from _g_tensor1 import _g_tensor1
from _response_function_cubes3 import _response_function_cubes3


class _print53(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NABLAVKS_CUBES = _nablavks_cubes1()
        self.G_TENSOR = _g_tensor1()
        self.RESPONSE_FUNCTION_CUBES = _response_function_cubes3()
        self._name = "PRINT"
        self._subsections = {'RESPONSE_FUNCTION_CUBES': 'RESPONSE_FUNCTION_CUBES', 'G_TENSOR': 'G_TENSOR', 'NABLAVKS_CUBES': 'NABLAVKS_CUBES'}

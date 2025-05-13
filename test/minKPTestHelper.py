
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.minKP import MinKP


class TestMinKPHelper:

    TEST_CASE: list[str] = [

        'res/mono_minKP_15_1.txt',
        'res/mono_minKP_25_1.txt',
        'res/mono_minKP_35_1.txt',
        'res/multi_minKP_5_2.txt',
        'res/multi_minKP_15_3.txt',
        'res/multi_minKP_15_5.txt',
        'res/multi_minKP_25_3.txt',
        'res/multi_minKP_25_5.txt',
        'res/multi_minKP_35_3.txt',
        'res/multi_minKP_35_5.txt',

    ]

    @staticmethod
    def minKPSolverTest(fp: str, mode: int, expected: bool) -> None:
        assert os.path.isfile(fp), f"Path {fp} is not a file."
        m: MinKP = MinKP(fp, mode=mode, verbose=False)
        assert m.solve() == expected, f"Expected {expected} for file {fp} with mode {mode}."


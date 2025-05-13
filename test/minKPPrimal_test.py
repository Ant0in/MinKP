
from minKPTestHelper import TestMinKPHelper
    
# Test each test case with the specified mode 0

def testMonoMinKPPrimal15_1() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[0], 0, True)
def testMonoMinKPPrimal25_1() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[1], 0, True)
def testMonoMinKPPrimal35_1() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[2], 0, True)
def testMultiMinKPPrimal5_2() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[3], 0, True)
def testMultiMinKPPrimal15_3() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[4], 0, True)
def testMultiMinKPPrimal15_5() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[5], 0, False)
def testMultiMinKPPrimal25_3() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[6], 0, True)
def testMultiMinKPPrimal25_5() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[7], 0, True)
def testMultiMinKPPrimal35_3() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[8], 0, True)
def testMultiMinKPPrimal35_5() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[9], 0, True)

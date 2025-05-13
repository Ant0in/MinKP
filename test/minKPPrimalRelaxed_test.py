
from minKPTestHelper import TestMinKPHelper
    
# Test each test case with the specified mode 1

def testMonoMinKPPrimalRelaxed15_1() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[0], 1, True)
def testMonoMinKPPrimalRelaxed25_1() -> None:  TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[1], 1, True)
def testMonoMinKPPrimalRelaxed35_1() -> None:  TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[2], 1, True)
def testMultiMinKPPrimalRelaxed5_2() -> None:  TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[3], 1, True)
def testMultiMinKPPrimalRelaxed15_3() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[4], 1, True)
def testMultiMinKPPrimalRelaxed15_5() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[5], 1, True)
def testMultiMinKPPrimalRelaxed25_3() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[6], 1, True)
def testMultiMinKPPrimalRelaxed25_5() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[7], 1, True)
def testMultiMinKPPrimalRelaxed35_3() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[8], 1, True)
def testMultiMinKPPrimalRelaxed35_5() -> None: TestMinKPHelper.minKPSolverTest(TestMinKPHelper.TEST_CASE[9], 1, True)

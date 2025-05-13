
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, LpStatusOptimal
from KPParser import KPParser



class MinKP:
    
    def __init__(self, fp: str, mode: int = 0) -> None:
        self.data: dict = KPParser.parseFile(fp=fp)
        self.mode: int = mode

    def solve(self) -> any:

        assert self.data is not None, "Data is Nill, parse most likely failed."

        # Choose the solver based on the mode (0, 1, or 2)
        solver: MinKP | None = None
        match self.mode:
            case 0: solver = MinKPPrimalIntegerSolution
            case 1: solver = MinKPPrimalRelaxedSolution
            case 2: solver = MinKPDualRelaxedSolution
            case _: raise ValueError(f"Invalid mode: {self.mode}. Must be 0, 1, or 2.")

        print(f"[i] Solving MinKP with {solver.__name__} (mode={self.mode})")

        # Solve the problem based on the number of knapsacks
        if self.data["numberOfKnapsacks"] == 1: return solver.solveSingleKnapsack(data=self.data)
        elif self.data["numberOfKnapsacks"] > 1: return solver.solveMultipleKnapsacks(data=self.data)
        else: raise ValueError(f"Invalid number of knapsacks: {self.data['numberOfKnapsacks']}. Must be > 0.")

    @staticmethod
    def solveSingleKnapsack(data: dict) -> any:
        raise NotImplementedError("This method should be implemented in the subclass.")
    
    @staticmethod
    def solveMultipleKnapsacks(data: dict) -> any:
        raise NotImplementedError("This method should be implemented in the subclass.")



class MinKPPrimalIntegerSolution(MinKP):

    @staticmethod
    def solveSingleKnapsack(data: dict) -> ...:
        
        # Create the problem
        prob = LpProblem("MinKP", LpMinimize)

    @staticmethod
    def solveMultipleKnapsacks(data: dict) -> ...:
        ...



class MinKPPrimalRelaxedSolution(MinKP):

    @staticmethod
    def solveSingleKnapsack(data: dict) -> ...:
        ...

    @staticmethod
    def solveMultipleKnapsacks(data: dict) -> ...:
        ...



class MinKPDualRelaxedSolution(MinKP):

    @staticmethod
    def solveSingleKnapsack(data: dict) -> ...:
        ...

    @staticmethod
    def solveMultipleKnapsacks(data: dict) -> ...:
        ...





if __name__ == "__main__":
    
    # Example usage
    m: MinKP = MinKP('res/mono_minKP_15_1.txt', mode=0)
    m.solve()



from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, LpStatusOptimal, LpStatusNotSolved, LpBinary, PULP_CBC_CMD
import os
import argparse



class ArgParser:

    @staticmethod
    def parseArgs() -> dict[str, any]:

        parser: argparse.ArgumentParser = argparse.ArgumentParser(description="MinKP ArgParser")
        parser.add_argument("filePath", type=str, help="Path to the file containing the knapsack problem data.")
        parser.add_argument("mode", type=int, choices=[0, 1, 2], help="Mode of the solver (0: Primal Integer, 1: Primal Relaxed, 2: Dual Relaxed).")
        parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    
        # parse the arguments
        args: argparse.Namespace = parser.parse_args()

        return {
            "fp": str(args.filePath),
            "mode": int(args.mode),
            "verbose": bool(args.verbose)
        }



class KPParser:

    KP_FORMAT_LINES: int = 5
    
    @staticmethod
    def _readFile(fp: str) -> list[str]:

        assert os.path.exists(fp), f"File {fp} does not exist."
        assert os.path.isfile(fp), f"Path {fp} is not a file."
        
        with open(fp, 'r') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    
    @staticmethod
    def _parseLines(lines: list[str]) -> dict:
        
        assert len(lines) == KPParser.KP_FORMAT_LINES, f"Expected {KPParser.KP_FORMAT_LINES} lines, got {len(lines)}."

        numberOfKnapsacks = int(lines[0])
        numberOfItems = int(lines[1])
        demands = [int(x) for x in lines[2].split()]
        weights = [int(x) for x in lines[3].split()]
        costs = [int(x) for x in lines[4].split()]

        # Validate the parsed data
        assert len(demands) == numberOfKnapsacks, f"Expected {numberOfKnapsacks} demands, got {len(demands)}."
        assert len(weights) == numberOfItems, f"Expected {numberOfItems} weights, got {len(weights)}."
        assert len(costs) == numberOfItems, f"Expected {numberOfItems} costs, got {len(costs)}."
        assert all(d > 0 for d in demands), "All demands must be positive."
        assert all(w > 0 for w in weights), "All weights must be positive."
        assert all(c > 0 for c in costs), "All costs must be positive."

        return {
            "numberOfKnapsacks": numberOfKnapsacks,
            "numberOfItems": numberOfItems,
            "demands": demands,
            "weights": weights,
            "costs": costs
        }

    @staticmethod
    def parseFile(fp: str) -> dict:
        
        """
        Parses a file containing knapsack problem data.

        :param fp: Path to the file containing the knapsack problem data.
        :raises AssertionError: If the file does not exist, is not a file, or the data format is invalid.
        :return: A dictionary containing the parsed data with the following keys:\n\n
            - "numberOfKnapsacks" (int): The number of knapsacks.\n
            - "numberOfItems" (int): The number of items.\n
            - "demands" (list[int]): The demands for each knapsack.\n
            - "weights" (list[int]): The weights of the items.\n
            - "costs" (list[int]): The costs of the items.\n

        """

        lines: list[str] = KPParser._readFile(fp)
        problemData: dict = KPParser._parseLines(lines)
        return problemData



class MinKP:
    
    def __init__(self, fp: str, mode: int = 0, verbose: bool = True) -> None:
        self.fp: str = fp
        self.data: dict = KPParser.parseFile(fp=fp)
        self.mode: int = mode
        self.verbose: bool = verbose

    def solve(self) -> bool:

        assert self.data is not None, "Data is Nill, parse most likely failed."

        # Choose the solver based on the mode (0, 1, or 2)
        solver: MinKP | None = None
        match self.mode:
            case 0: solver = MinKPPrimalIntegerSolution
            case 1: solver = MinKPPrimalRelaxedSolution
            case 2: solver = MinKPDualRelaxedSolution
            case _: raise ValueError(f"Invalid mode: {self.mode}. Must be 0, 1, or 2.")

        algorithm: callable | None = None
        if (self.data['numberOfKnapsacks'] == 1): algorithm = solver.solveSingleKnapsack
        elif (self.data['numberOfKnapsacks'] > 1): algorithm = solver.solveMultipleKnapsacks
        else: raise ValueError(f"Invalid number of knapsacks: {self.data['numberOfKnapsacks']}. Must be > 0.")


        print(f"[i] Solving MinKP with {solver.__name__} (mode={self.mode}) for file {self.fp}... (using {algorithm.__name__})")

        # Solve the problem based on the number of knapsacks
        return algorithm(data=self.data, v=self.verbose)

    @staticmethod
    def solveSingleKnapsack(data: dict, v: bool) -> bool:
        raise NotImplementedError("This method should be implemented in the subclass.")

    @staticmethod
    def solveMultipleKnapsacks(data: dict, v: bool) -> bool:
        raise NotImplementedError("This method should be implemented in the subclass.")



class MinKPPrimalIntegerSolution(MinKP):

    @staticmethod
    def solveSingleKnapsack(data: dict, v: bool) -> bool:
        # Create the problem
        problem: LpProblem = LpProblem("MinKP", LpMinimize)
        # Create decision variables (x is a binary variable, 0 or 1, representing whether an item is included in the knapsack)
        x = LpVariable.dicts("x", range(data["numberOfItems"]), lowBound=0, upBound=1, cat="Binary")
        # Objective function (minimize total cost)
        problem += lpSum(data["costs"][i] * x[i] for i in range(data["numberOfItems"])), "TotalCost"
        # Constraints (ensure the total weight of selected items is greater than or equal to the demand)
        problem += lpSum(data["weights"][i] * x[i] for i in range(data["numberOfItems"])) >= data["demands"][0], "WeightConstraint"
        # Solve the problem and print the results
        problem.solve(PULP_CBC_CMD(msg=v))
        MinKPPrimalIntegerSolution.printSingleKnapsackResults(problem=problem, data=data, x=x)
        return problem.status == LpStatusOptimal
     
    @staticmethod
    def solveMultipleKnapsacks(data: dict, v: bool) -> bool:
        
        # Create the problem
        problem: LpProblem = LpProblem("MinKP", LpMinimize)
        # Create decision variables (x is a binary variable, 0 or 1, representing whether an item is included in the nth knapsack)
        x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(data["numberOfKnapsacks"])] for i in range(data["numberOfItems"])]
        # Objective function (minimize total cost)
        problem += lpSum(data["costs"][i] * x[i][j] for i in range(data["numberOfItems"]) for j in range(data["numberOfKnapsacks"])), "TotalCost"
        # Constraint 1 (ensure the total weight of selected items is greater than or equal to the demand for each knapsack)
        # Constraint 2 (ensure each item is assigned to at most one knapsack)
        for j in range(data["numberOfKnapsacks"]): problem += lpSum(data["weights"][i] * x[i][j] for i in range(data["numberOfItems"])) >= data["demands"][j], f"WeightConstraint_{j}"
        for i in range(data["numberOfItems"]): problem += lpSum(x[i][j] for j in range(data["numberOfKnapsacks"])) <= 1, f"ItemAssignment_{i}"
        # Solve the problem and print the results
        problem.solve(PULP_CBC_CMD(msg=v))
        MinKPPrimalIntegerSolution.printMultipleKnapsackResults(problem=problem, data=data, x=x)
        return problem.status == LpStatusOptimal

    @staticmethod
    def printSingleKnapsackResults(problem: LpProblem, data: dict, x: LpVariable) -> None:

        print(f"[{'✓' if problem.status == LpStatusOptimal else 'X'}] Status: {LpStatus[problem.status]}\n")
        if problem.status != LpStatusOptimal:
            return
        
        print(f"[c] Total Cost: {problem.objective.value()}")
        print(f"[w] Total Weight: {lpSum(data['weights'][i] * x[i].varValue for i in range(data['numberOfItems']))} (should be >= {data['demands'][0]})\n")

        print("[i] Selected Items:")
        for i in range(data["numberOfItems"]):
            if x[i].varValue > 0: print(f"► Item {i+1}: Cost={data['costs'][i]}, Weight={data['weights'][i]}")

    @staticmethod
    def printMultipleKnapsackResults(problem: LpProblem, data: dict, x: list[list[LpVariable]]) -> None:

        print(f"[{'✓' if problem.status == LpStatusOptimal else 'X'}] Status: {LpStatus[problem.status]}\n")
        if problem.status != LpStatusOptimal:
            return
        
        print(f"[c] Total Cost: {problem.objective.value()}")
        print(f"[w] Total Weight: {lpSum(data['weights'][i] * x[i][j].varValue for i in range(data['numberOfItems']) for j in range(data['numberOfKnapsacks']))} (should be >= {sum(data['demands'])})")

        for j in range(data["numberOfKnapsacks"]):
            print(f"\n[w] Total Weight for Knapsack {j+1}: {lpSum(data['weights'][i] * x[i][j].varValue for i in range(data['numberOfItems']))} (should be >= {data['demands'][j]})")
            print("[i] Selected Items:")
            for i in range(data["numberOfItems"]):
                if x[i][j].varValue > 0: print(f"► Item {i+1}: Cost={data['costs'][i]}, Weight={data['weights'][i]}")



class MinKPPrimalRelaxedSolution(MinKP):

    @staticmethod
    def solveSingleKnapsack(data: dict, v: bool) -> bool:
        raise NotImplementedError("This method is not implemented for the Primal Relaxed solution.")

    @staticmethod
    def solveMultipleKnapsacks(data: dict, v: bool) -> bool:
        raise NotImplementedError("This method is not implemented for the Primal Relaxed solution.")



class MinKPDualRelaxedSolution(MinKP):

    @staticmethod
    def solveSingleKnapsack(data: dict, v: bool) -> bool:
        raise NotImplementedError("This method is not implemented for the Dual Relaxed solution.")

    @staticmethod
    def solveMultipleKnapsacks(data: dict, v: bool) -> bool:
        raise NotImplementedError("This method is not implemented for the Dual Relaxed solution.")





if __name__ == "__main__":
    
    # Example usage
    # m: MinKP = MinKP('res/multi_minKP_35_5.txt', mode=0, verbose=False)
    # m.solve()

    # Command line usage
    # python3 src/minKP.py -fp res/multi_minKP_35_5.txt -m 0 -v

    args: dict = ArgParser.parseArgs()
    m: MinKP = MinKP(fp=args['fp'], mode=args['mode'], verbose=args['verbose'])
    m.solve()


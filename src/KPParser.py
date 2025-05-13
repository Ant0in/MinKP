
import os


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


if __name__ == "__main__":

    # Example usage
    # print(KPParser.parseFile("res/mono_minKP_15_1.txt"))
    ...

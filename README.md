<!-- markdownlint-disable MD033 MD041 -->

<!-- pretty badges -->
<div align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0_alpha-red" alt="Version Badge">
  <img src="https://img.shields.io/badge/License-MIT-dark_green.svg" alt="License Badge"/>
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language Badge"/>
  <img src="https://img.shields.io/badge/School-ULB-yellow" alt="School Badge"/>
  <img src="https://github.com/Ant0in/MinKP/actions/workflows/ci.yml/badge.svg" alt="Build Status"/>
</div>

# 🧳 MinKP Solver

Welcome to the **MinKP Solver**! This project focuses on solving the **Minimum Knapsack Problem** (MinKP). The goal is to minimize the total cost of selected items while respecting weight constraints across one or more knapsacks.

## 📜 Description

This project implements a **Python-based solution** for the **MinKP** using optimization techniques such as **Linear Programming** (LP) and **Integer Programming** (IP), leveraging the **PuLP** library.

For more detailed problem specifications and additional information, please refer to the accompanying documentation: `./pdf/consignes.pdf`.

## 🚀 Features

- Solves **Single Knapsack** and **Multiple Knapsack** versions of the problem.
- Supports **Primal Integer Solution**, **Primal Relaxed Solution**, and **Dual Relaxed Solution**.
- Implements **linear programming** optimization using **PuLP**.

## ⚙️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ant0in/MinKP.git
    cd MinKP
    ```

2. Set up a **virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. If you don't have `requirements.txt`, you can manually install **PuLP** and **pytest**:

    ```bash
    pip install pulp pytest
    ```

## 🛠️ Usage

### Running the Solver

To run the solver, you can use the following command line :

```bash
python3 ./src/minKP.py
```


## 🧪 Testing with pytest

To run the tests for the project, use the following command:

```bash
pytest  # -vvv flag can be added for extra verbose
```

This will automatically run all the unit tests and provide feedback.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgements

This project was developed for the **`Algorithmique et recherche opérationnelle`** course **`INFO-F310`**. Special thanks to `Dimitrios Papadimitriou (ULB)` and `Hugo Callebaut (ULB)` for their guidance and support.

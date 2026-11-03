# 🧮 Scientific Calculator

> A Python calculator library with history tracking and comprehensive unit tests.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- Basic operations: add, subtract, multiply, divide
- Scientific: power, square root, factorial
- Calculation history tracking
- 100% test coverage
- Type-annotated API

## 🚀 Quick Start

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(10, 5))       # 15
print(calc.sqrt(144))        # 12.0
print(calc.factorial(5))     # 120
calc.show_history()          # prints all calculations
```

## 🧪 Tests

```bash
pip install pytest
pytest tests/ -v --tb=short
```

## 📁 Structure

```
calculator/
├── calculator.py
├── tests/test_calculator.py
└── README.md
```

## 📝 License

MIT

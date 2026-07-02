# Python Placement Training — Day 1 & Day 2

Clean, runnable Python code from a placement-readiness training program (60 students selected across branches). Covers **Python fundamentals** (Day 1) and **Object-Oriented Programming** (Day 2), organized by topic with docstrings and runnable demos for every concept.

## 📁 Repository Structure

```
.
├── day1_python_fundamentals/
│   ├── 01_list_operations.py             # Slicing, indexing, in-place modification, matrices
│   ├── 02_gotchas_mutability_and_copying.py  # Mutable default args, shallow vs deep copy
│   ├── 03_tuples_and_zip.py              # Tuple basics, zip() for parallel iteration
│   ├── 04_dictionaries.py                # Tuple keys, key-type coercion, sorting, id()
│   ├── 05_string_manipulation.py         # Reverse, palindrome check, remove duplicates
│   └── 06_interview_problems.py          # Repeated numbers, common elements, max consecutive 1s
│
├── day2_oop_concepts/
│   ├── 01_classes_and_constructors.py    # Classes, objects, __init__
│   ├── 02_instance_vs_static_variables.py # Instance vs class variables, static methods
│   ├── 03_inheritance.py                 # Single, multilevel, multiple inheritance, MRO
│   ├── 04_abstraction.py                 # Abstract base classes (ABC)
│   ├── 05_polymorphism.py                # Overloading via defaults, method/constructor overriding
│   └── 06_encapsulation.py               # Public, protected, private members
│
├── requirements.txt
├── LICENSE
└── .gitignore
```

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/python-placement-training.git
cd python-placement-training
python3 day1_python_fundamentals/01_list_operations.py
```

Every file is self-contained and runnable on its own — each has a `if __name__ == "__main__":` block that demonstrates the concept with sample output. No external dependencies are required (standard library only).

## 📚 Topics Covered

**Day 1 — Python Fundamentals**
- List slicing, indexing, and in-place modification
- Mutable default argument pitfall
- Shallow copy vs deep copy
- Tuples and the `zip()` function
- Dictionaries: tuple keys, key-type coercion, sorting, `id()`
- String manipulation: reversal, palindrome check, deduplication
- Common interview problems: repeated elements, common elements across lists, max consecutive ones

**Day 2 — Object-Oriented Programming**
- Classes, objects, and constructors (`__init__`)
- Instance variables vs static (class) variables, static methods
- Inheritance: single-level, multilevel, multiple, and the diamond problem / MRO
- Abstraction using `abc.ABC` and `@abstractmethod`
- Polymorphism: simulating overloading with default arguments, method/constructor overriding
- Encapsulation: public, protected (`_attr`), and private (`__attr`) members

## 🧑‍💻 Author

**Bhagyavardhan Nagane**
Final-year Electronics & Telecommunication Engineering, SITRC, Nashik

## 📄 License

This project is licensed under the [MIT License](LICENSE).

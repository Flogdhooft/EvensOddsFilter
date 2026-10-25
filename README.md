# Python Number Filter CLI

A **Command Line Interface (CLI) application** built as a personal practice project to reinforce core Python concepts. This project was self-designed to master function modularity, input validation (`try/except`), and interactive control loops (`while True`). *NumberFilter* allows users to input a custom sequence of integers and interactively filter them based on parity (`1. even numbers`, `2. odd numbers`, `3. both even and odd numbers`). 

---

## Key Features

- **Interactive CLI Interface :** Multi-step console application guiding the user through input and mode selection.
- **Filtering Modes :**
  - Filter and display **even numbers** only.
  - Filter and display **odd numbers** only.
  - Filter and display **both even and odd numbers** simultaneously with list length counts.
- **Robust Input Validation :**
  - Prevents empty submissions with user-friendly retry prompts.
  - Catches invalid non-integer inputs using `try/except` exception handling.
  - Validates menu choice selection in a control loop.
- **Functional Separation :** Logic split into dedicated helper functions (`get_user_numbers`, `filter_even_numbers`, `filter_odd_numbers`).

---

## Concepts & Technologies Applied

- **Python 3**
- **List Comprehensions :** Efficient inline list filtering (`[num for num in numbers if num % 2 == 0]`).
- **Modulo Arithmetic :** Modulo operator (`%`) for checking parity.
- **Error & Exception Handling :** Input parsing using `try/except ValueError`.
- **Control Flow :** `while` loops, conditional logic (`if/elif/else`), and string methods (`split()`, `strip()`).

---

## Usage Example

```text
/// Bienvenue dans le programme de filtrage. ///

Saisissez plusieurs nombres entiers séparés par des espaces. 
(Par exemple : 24 6 490 1 9 123)

24 6 490 1 9 123

Quel mode de filtrage choisissez-vous ?
  1. Ne filtrer que les nombres pairs
  2. Ne filtrer que les nombres impairs
  3. Filtrer les nombres pairs et impairs

Votre choix (1, 2 ou 3) : 

3

>> Nombres pairs (3) : [24, 6, 490]
>> Nombres impairs (3) : [1, 9, 123]

<div align="center">

<img src="assets/banner.svg" alt="The Ohm Calculator" width="100%">

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![No dependencies](https://img.shields.io/badge/dependencies-none-2ea44f?style=for-the-badge)](#-requirements)
[![CLI](https://img.shields.io/badge/interface-CLI-f72585?style=for-the-badge&logo=windowsterminal&logoColor=white)](#-usage)
[![Last commit](https://img.shields.io/github/last-commit/Nxhon-bot/The-Ohm-Calculator?style=for-the-badge&color=4cc9f0)](https://github.com/Nxhon-bot/The-Ohm-Calculator/commits/main)

**Solve Ohm's Law in seconds, straight from your terminal.**

[Features](#-features) •
[Ohm's Law](#-ohms-law) •
[Installation](#-installation) •
[Usage](#-usage) •
[Author](#-author)

</div>

---

## ✨ Features

- 🔌 **Three calculations in one** – find resistance, voltage, or current.
- ⌨️ **Forgiving input** – type `r`, `R`, `v`, `V`, `i`, or `I`.
- 🛡️ **Error-proof** – rejects letters, empty input, and division by zero, then asks again.
- 📦 **Zero dependencies** – a single Python file, nothing to install.

---

## 📐 Ohm's Law

<table>
<tr>
<td width="45%" align="center">
<img src="assets/ohm-triangle.svg" alt="Ohm's Law triangle" width="300">
</td>
<td>

Ohm's Law links the three basic quantities of an electric circuit.
Cover the value you want on the triangle, and the other two show the formula.

| You want | Formula | Unit |
|:---:|:---:|:---:|
| 🟣 **R** · Resistance | `R = V ÷ I` | Ohms (Ω) |
| 🔵 **V** · Voltage | `V = I × R` | Volts (V) |
| 🟡 **I** · Current | `I = V ÷ R` | Amps (A) |

</td>
</tr>
</table>

---

## 🚀 Installation

### Requirements

- [Python 3.8+](https://www.python.org/downloads/)

### Get the code

```bash
git clone https://github.com/Nxhon-bot/The-Ohm-Calculator.git
cd The-Ohm-Calculator
```

---

## 🖥️ Usage

```bash
python The_Ohm_Calculator.py
```

Choose the value you are looking for, then enter the other two.

```text
Welcome to your favorite calculator: The Ohm Calculator
Please enter the value you are looking for (R, V, or I):v
Please enter the resistance (R):10
Please enter the current (I):2
The voltage is:  20.0  Volts
Thank you for using the Ohm Calculator. Made by JB's
```

<details>
<summary><b>More examples</b></summary>

<br>

| Looking for | Inputs | Result |
|:---:|---|---|
| **R** | V = `12`, I = `0.5` | `24.0 Ohms` |
| **V** | R = `220`, I = `0.02` | `4.4 Volts` |
| **I** | V = `9`, R = `450` | `0.02 Amps` |

</details>

---

## 📁 Project structure

```text
The-Ohm-Calculator/
├── assets/
│   ├── banner.svg            # README banner
│   └── ohm-triangle.svg      # Ohm's Law triangle
├── The_Ohm_Calculator.py     # The calculator
└── README.md
```

---

## 👤 Author

<div align="center">

**Jhon Bustos · JB's**

[![GitHub](https://img.shields.io/badge/GitHub-Nxhon--bot-181717?style=for-the-badge&logo=github)](https://github.com/Nxhon-bot)

⭐ If this calculator saved you some math, give the repo a star!

</div>

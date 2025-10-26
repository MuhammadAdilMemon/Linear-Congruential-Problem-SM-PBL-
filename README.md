# 💻 SM PBL – Linear Congruential Problem (LCG Implementation)

A **simple interactive web presentation** built using **HTML, CSS, and JavaScript** to demonstrate the working of the **Linear Congruential Generator (LCG)** — one of the oldest and simplest methods for generating pseudo-random numbers.  
This project was developed as part of the **Software Modeling (SM) PBL** activity.

---

## 🧩 Problem Statement / Question

**Q:**  
Generate a sequence of pseudo-random numbers using the **Linear Congruential Generator (LCG)** method with the following parameters:

\[
a = 5,\quad c = 3,\quad m = 16,\quad X_0 = 7
\]

Then, verify whether the generator achieves a **full period (m = 16)** using the **Hull–Dobell Theorem**.

---

## 📘 Overview

The **Linear Congruential Generator (LCG)** is based on the recurrence relation:

\[
X_{i+1} = (aX_i + c) \mod m
\]

where:
- **a** → multiplier  
- **c** → increment  
- **m** → modulus  
- **X₀** → seed (initial value)

The output random number is then calculated as:

\[
R_i = \frac{X_i}{m}
\]

---

## 🧮 Parameters Used

| Symbol | Description | Value |
|:-------:|--------------|:------:|
| a | Multiplier | 5 |
| c | Increment | 3 |
| m | Modulus | 16 |
| X₀ | Seed | 7 |

---

## ⚙️ Features

✅ Step-by-step slide-style presentation (Intro → Problem → Steps → Calculations → Validation → Conclusion)  
✅ Auto-generated LCG calculation table using JavaScript  
✅ Modern UI using only **HTML + CSS + JS**  
✅ Responsive layout with smooth slide transitions  

---

## 🚀 How to Run

1. Clone or download this repository  
   ```bash
   git clone https://github.com/your-username/linear-congruential-problem-sm-pbl.git

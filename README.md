# QrandomSelection

This repository contains the source code for the research paper titled **"A Generalized Quantum Algorithm for Assuring Fairness in Random Selection Among 2ⁿ Participants."** The paper was published in **SN Computer Science (Springer Nature Journal)** on **March 14, 2020**.

## 📜 **Research Paper Details**

- **📝 Paper Title:** A Generalized Quantum Algorithm for Assuring Fairness in Random Selection Among 2ⁿ Participants
- **👨‍💻 Author:** [Ravin Kumar](https://mr-ravin.github.io/)
- **📚 Publisher:** Springer
- **📅 Publication Date:** March 14, 2020
- **🔗 Publication Link:** [Springer](https://link.springer.com/article/10.1007/s42979-020-0091-z)
- **🔍 DOI:** [https://doi.org/10.1007/s42979-020-0091-z](https://doi.org/10.1007/s42979-020-0091-z)

### 📖 **Cite this Paper:**

```bibtex
Kumar, R. A Generalized Quantum Algorithm for Assuring Fairness in Random Selection Among 2N Participants.  
SN COMPUT. SCI. 1, 86 (2020). https://doi.org/10.1007/s42979-020-0091-z
```

---

## 🔧 **Development Details**

- **👨‍💻 Developer:** [Ravin Kumar](https://mr-ravin.github.io)
- **📂 GitHub Repository:** [QrandomSelection](https://github.com/mr-ravin/QrandomSelection)

### 📦 **Dependencies**

```
qiskit-terra version: 0.7.0
qiskit-aqua version: 0.4.1
```

---

## 📥 **Installation**

Install using pip:

```sh
pip install qrandom
```

Or directly from GitHub:

```sh
pip install git+https://github.com/mr-ravin/QrandomSelection.git
```

---

## 🚀 **Usage Guide**

### 🎲 **Random Selection Using a Quantum Circuit**

Generate a quantum circuit for 'N' participants:

```python
import qrandom
res = qrandom.select(8)  # 8 represents the total number of participants.
```

### 🖼 **Visualizing the Quantum Circuit**

Save the pictorial representation of the quantum circuit:

```python
import qrandom
qrandom.vis_circuit(8, "file_name.png")  # Saves the circuit diagram for 8 participants as file_name.png
```

![fig 1](quantum_circuit.png)

**Fig. 1** Quantum Circuit for 8 participants.

---

## ⚖️ **License**

```text
Copyright (c) 2018 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```


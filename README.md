# QrandomSelection
This repository contains the source code of research paper titled: " A generalized quantum algorithm for assuring fairness in random selection among 2^n participants". Research paper is currenty under analysis phase.

Author: Ravin Kumar

#### Qiskit Version:
##### qiskit-terra version: 0.7.0
##### qiskit-aqua version: 0.4.1

- ### Create quantum circuit for 'N' participants
Our module provides a direct method for creating quantum circuit for 'n' participants.
```python
import qrandom
res=qrandom.select(8) ### here 8 is total number of participants.
```
- ### Visualization of quantum circuit
A simple method is given to save the pictorial repreentation of quantum circuit for 'n' participants.
```python
import qrandom
chk=qrandom.vis_circuit(8,"file_name.png") ### it saves the generalized quantum circuit for 8 participants in file_name.png file. 

# QrandomSelection
This repository contains the source code of research paper titled: " A generalized quantum algorithm for assuring fairness in random selection among 2<sup>n</sup> participants". Research paper is published in SN Computer Science Springer Nature Journal, 14th march 2020.

#### Paper Title: A Generalized Quantum Algorithm for Assuring Fairness in Random Selection Among 2<sup>N</sup> Participants
#### Author: [Ravin Kumar](https://mr-ravin.github.io/)

#### Publication: 14th March 2020

#### Publication Link: https://link.springer.com/article/10.1007/s42979-020-0091-z

#### Doi: https://doi.org/10.1007/s42979-020-0091-z

##### Cite as:
```
Kumar, R. A Generalized Quantum Algorithm for Assuring Fairness in Random Selection Among 2N Participants. 
SN COMPUT. SCI. 1, 86 (2020). https://doi.org/10.1007/s42979-020-0091-z
```

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
```

![quantum circuit](https://github.com/mr-ravin/QrandomSelection/blob/master/quantum_circuit.png)

<b>Fig.1</b> Quantum Circuit for 8 participants.

### Installing module using PyPi:
```python
pip install qrandom
```

```python

Copyright (c) 2018 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

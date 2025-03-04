import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrandom",
    version="1.7",
    author="Ravin Kumar",
    author_email="mr.ravin_kumar@hotmail.com",
    description="This repository contains the source code of research paper titled: \"A Generalized Quantum Algorithm for Assuring Fairness in Random Selection Among 2ⁿ Participants.\"",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-ravin/QrandomSelection",
    keywords=[
        'Quantum Algorithm', 'Quantum Fairness', 'One to One', 
        'Quantum Random Number', 'Random Selection', 'Lucky Draw'
    ],
    install_requires=[
        'qiskit==0.46.0',
        'pylatexenc==2.10',
        ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# Compilers-finalProject
Real numbers RegExr Python - Compiler final project 

RegExr: (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?

NFA:
![Real Numbers RegExr](https://github.com/mohammadT77/Compilers-finalProject/blob/master/default/real%20num%20regex.png)

main.py

INPUT:  text or .txt file path

OUTPUT: substrings that match with RegExpr in text
  
CONSOLE COMMANDS:

py main.py


py main.py [readfile_path] [save_outputfile_path (default=last_output.txt)]
  
  example:
  ```
  py main.py
  ```
  output:
  ```
  Enter your Text: ...
  .
  .
  .
  ```
  
  ----------
  ```
  py main.py file_input_test.txt
  ```
  output:
  ```
  File Path: file_input_test.txt
  ------------------------------------------------------
  INPUT TEXT:
  - test file:
  - 123.23
  - 22E2
  - 231E-12
  - 21.11E-123
  -
  - >invalid:
  - >asdsa
  - >1sd
  - >we1
  - >123-23
  ------------------------------------------------------
  RegExr: (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?
  ------------------------------------------------------
  NFA:
  .
  .
  .
  OUTPUT:
  1)123.23
  2)22E2
  3)231E-12
  4)21.11E-123

  ======================================================
  Save Path: last_output.txt
  Saved!
  ```
  Now Check Saved Path
  

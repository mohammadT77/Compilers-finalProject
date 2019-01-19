# Compilers-finalProject
Real numbers RegExr Python - Compiler final project 

RegExr: (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?

NFA:
![Real Numbers RegExr]https://github.com/mohammadT77/Compilers-finalProject/blob/master/default/real%20num%20regex.png


main.py:
  INPUT:  text or .txt file path
  OUTPUT: substrings that match with RegExpr in text
  
  CONSOLE COMMANDS:
  -py main.py
  -py main.py [readfile_path] [save_outputfile_path (default=last_output.txt)]
  
  example:
  ```
  py main.py
  ```
  output:
  ```
  Enter your Text:
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
  - 1)123123
  - 2)2323.2312
  - 3)123
  ------------------------------------------------------
  RegExr: (([0 - 9] +)?\.)?[0 - 9] + ([eE][-+]?[0-9]+)?
  ------------------------------------------------------
  NFA:
  .
  .
  .
  ```
  Now Check Saved Path
  

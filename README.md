## Submission description ##
Student: Joshua Stein  
Student ID: V00951354  
This submission attempts the basic task and all three extended tasks. The included files are described below.

### README.md ###
This README outlines the contents of this submission.

### sud2sat ###
Python script that **requires Python 3.8 or later**. Translates the sudoku file on stdin to a CNF file output to stdout. Uses minimal encoding by default. Lines 30-33 control which encoding is used. Uncomment **exactly one of these lines** and save the script to change which encoding is used. Alternatively, sud2sat accepts command line arguments `MINIMAL`, `EFFICIENT`, and `EXTENDED`.

| Encoding  | Main method function to uncomment  | Equivalent command line expression               |
| :---      | :---                               | :---                                             |
| Minimal   | Uncomment sud2sat() on line 30     | `./sud2sat < puzzle.txt > puzzle.cnf`            |
|           | OR Uncomment sud2sat1() on line 31 | OR `./sud2sat MINIMAL < puzzle.txt > puzzle.cnf` |
| Efficient | Uncomment sud2sat2() on line 32    | `./sud2sat EFFICIENT < puzzle.txt > puzzle.cnf`  |
| Extended  | Uncomment sud2sat3() on line 33    | `./sud2sat EXTENDED < puzzle.txt > puzzle.cnf`   |


### sat2sud ###
Python script that **requires Python 3.8 or later**. Converts `minisat` solve file on stdin to a readable sudoku output to stdout. Usage: `./sat2sud < assign.txt > solution.cnf`.

### report.md ###
Documents approach to testing and evaluation. Includes raw and summarised statistics on `minisat` solves for CNF files produced by `sud2sat`. Specifically,
- Analyses minisat stat output for 50 'easy' minimal-encoded CNFs
- Analyses minisat stat output for 95 'hard' minimal-encoded CNFs
- Analyses minisat stat output for 50 easy and 95 hard efficient-encoded CNFs
- Analyses minisat stat output for 50 easy and 95 hard extended-encoded CNFs


### tester.py ###
Python script used as testing harness and stat generator. Provided for reference.
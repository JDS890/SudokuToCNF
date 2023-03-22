## Implementation details ##
The `sud2sat` Python script converts the puzzle to a 0-indexed 2D array (implemented as a list of lists). Fixed cells keep their allocated number (1 - 9) whereas all free cells are converted to number 0. The number 0 was chosen to represent free cells since it's naturally 'falsey' in Python. Once quirk about this design choice is that since i,j,k are 0-indexed in the encoding rules, the value in the sudoku at row i column j is array[i][j]-1 rather than just array[i][j]. Further details about the implementation are thoroghly documented in the comments of the script.

## Test Approach ##
Used `sud2sat` to translate each sudoku puzzle to three CNFs with minimal, extended and efficient encoding. Each CNF was then solved using `minisat`, and the resulting stat files were accumulated to produce a maximum, minimum and average score for each generic statistic. These stats were calculated independently for the p096Usudoku.txt ('easy') and top95.txt ('hard') sudoku sets. See the [raw test results](#test-results-raw).

## Test Results Summary ##
As expected, the more restrictive CNF encodings required more clauses to enforce the extra rules. For example, the average number of clauses for the hard sudoku set was `2734.4`, `3213.5`, `3385.6` for minimal, efficient and extended encodings, repectively. The opposite was true for the average number of propagations. That is, on average, extended encodings were solved using the least number of propagations (`1255.6` for hard sudoku set), whereas minimal encodings were solved using the most number of propagations on average (`7421.0` for hard sudoku set). The average CPU time was smallest for extended encoding solves and largest for efficient encoding solves. This is emphasised for the hard sudoku set, where the average CPU time was `0.0056711s`, `0.0068861s`, `0.0074462s` for the extended, minimal and efficient encoding solves, respectively.

## Basic task ##
Given minimal encodings of 50 easy puzzles, on average, `minisat` solved puzzles of 1721.5 clauses in 4.1ms using 755.04 propagations. See summary of all stats [here](#cnf-set-p096usudokutxt-with-minimal-encoding).

## Extended task 1 ##
Given minimal encodings of 95 hard puzzles, on average, `minisat` solved puzzles of 2734.4 clauses in 6.9ms using 7421.0 propagations. See summary of all stats [here](#cnf-set-top95txt-with-minimal-encoding).

## Extended task 2 ##
Given efficient encodings of 50 easy puzzles, on average, `minisat` solved puzzles of 1904.4 clauses in 4.5ms using 728.7 propagations. See summary of all stats [here](#cnf-set-p096usudokutxt-with-efficient-encoding).  
Given efficient encodings of 95 hard puzzles, on average, `minisat` solved puzzles of 3213.5 clauses in 7.4ms using 6515.7 propagations. See summary of all stats [here](#cnf-set-top95txt-with-efficient-encoding).

## Extended task 3 ##
Given extended encodings of 50 easy puzzles, on average, `minisat` solved puzzles of 1963.5 clauses in 4.1ms using 514.8 propagations. See summary of all stats [here](#cnf-set-p096usudokutxt-with-extended-encoding).  
Given extended encodings of 95 hard puzzles, on average, `minisat` solved puzzles of 3385.6 clauses in 5.7ms using 1255.6 propagations. See summary of all stats [here](#cnf-set-top95txt-with-extended-encoding).

## Discussion about results ##
It's interesting that the extended encoding requires less CPU time and propagations to solve (on average) than the minimal encoding, despite having more clauses. Perhaps the extra clauses provided in the extended encoding allow minisat to converge more quickly on whether the CNF is satisfiable.

## Test Results Raw ##

### CNF set: p096Usudoku.txt with MINIMAL encoding ###
CNFs solved: 50 (50 SAT, 0 UNSAT)  

| Stat                     |             Max |             Min |             Ave |
| :---                     |            ---: |            ---: |            ---: |
| Number of variables      |           729.0 |           721.0 |          727.88 |
| Number of clauses        |          2529.0 |           805.0 |          1721.5 |
| Parse time (s)           |             0.0 |             0.0 |             0.0 |
| Eliminated clauses (Mb)  |             0.0 |             0.0 |             0.0 |
| Simplification time (s)  |             0.0 |             0.0 |             0.0 |
| restarts                 |             2.0 |             1.0 |            1.02 |
| conflicts                |           117.0 |             0.0 |            8.22 |
| decisions                |           157.0 |             1.0 |           16.78 |
| propagations             |          3963.0 |           419.0 |          755.04 |
| conflict literals        |          1032.0 |             0.0 |           50.04 |
| Memory used (Mb)         |            0.44 |            0.27 |          0.3434 |
| CPU time (s)             |        0.005661 |        0.002885 |       0.0041397 |

<br>

### CNF set: p096Usudoku.txt with EFFICIENT encoding ###
CNFs solved: 50 (50 SAT, 0 UNSAT)  

| Stat                     |             Max |             Min |             Ave |
| :---                     |            ---: |            ---: |            ---: |
| Number of variables      |           729.0 |           721.0 |          727.88 |
| Number of clauses        |          2953.0 |           805.0 |          1904.4 |
| Parse time (s)           |             0.0 |             0.0 |             0.0 |
| Eliminated clauses (Mb)  |             0.0 |             0.0 |             0.0 |
| Simplification time (s)  |             0.0 |             0.0 |             0.0 |
| restarts                 |             2.0 |             1.0 |            1.02 |
| conflicts                |           111.0 |             0.0 |            7.56 |
| decisions                |           143.0 |             1.0 |           15.22 |
| propagations             |          4042.0 |           425.0 |           728.7 |
| conflict literals        |           969.0 |             0.0 |           46.98 |
| Memory used (Mb)         |            0.43 |            0.27 |          0.3432 |
| CPU time (s)             |        0.006808 |        0.003049 |       0.0045345 |

<br>

### CNF set: p096Usudoku.txt with EXTENDED encoding ###
CNFs solved: 50 (50 SAT, 0 UNSAT)  

| Stat                     |             Max |             Min |             Ave |
| :---                     |            ---: |            ---: |            ---: |
| Number of variables      |           729.0 |           721.0 |          727.88 |
| Number of clauses        |          3120.0 |           805.0 |          1963.5 |
| Parse time (s)           |             0.0 |             0.0 |             0.0 |
| Eliminated clauses (Mb)  |             0.0 |             0.0 |             0.0 |
| Simplification time (s)  |             0.0 |             0.0 |             0.0 |
| restarts                 |             1.0 |             1.0 |             1.0 |
| conflicts                |             3.0 |             0.0 |            0.26 |
| decisions                |             6.0 |             1.0 |             1.5 |
| propagations             |           752.0 |           441.0 |          514.18 |
| conflict literals        |             9.0 |             0.0 |            0.54 |
| Memory used (Mb)         |            0.48 |            0.27 |          0.3402 |
| CPU time (s)             |        0.005419 |        0.003115 |       0.0041386 |

<br>

### CNF set: top95.txt with MINIMAL encoding ###
CNFs solved: 95 (95 SAT, 0 UNSAT)  

| Stat                     |             Max |             Min |             Ave |
| :---                     |            ---: |            ---: |            ---: |
| Number of variables      |           729.0 |           721.0 |          728.15 |
| Number of clauses        |          3374.0 |          1967.0 |          2734.4 |
| Parse time (s)           |             0.0 |             0.0 |             0.0 |
| Eliminated clauses (Mb)  |             0.0 |             0.0 |             0.0 |
| Simplification time (s)  |             0.0 |             0.0 |             0.0 |
| restarts                 |             8.0 |             1.0 |          2.0316 |
| conflicts                |          1245.0 |             3.0 |          170.18 |
| decisions                |          2138.0 |            10.0 |          300.72 |
| propagations             |      5.5302e+04 |           582.0 |          7421.0 |
| conflict literals        |      1.9441e+04 |            35.0 |          2100.1 |
| Memory used (Mb)         |             0.6 |            0.32 |         0.41537 |
| CPU time (s)             |        0.020406 |        0.004625 |       0.0068861 |

<br>

### CNF set: top95.txt with EFFICIENT encoding ###
CNFs solved: 95 (95 SAT, 0 UNSAT)  

| Stat                     |             Max |             Min |             Ave |
| :---                     |            ---: |            ---: |            ---: |
| Number of variables      |           729.0 |           721.0 |          728.15 |
| Number of clauses        |          4037.0 |          2300.0 |          3213.5 |
| Parse time (s)           |             0.0 |             0.0 |             0.0 |
| Eliminated clauses (Mb)  |             0.0 |             0.0 |             0.0 |
| Simplification time (s)  |             0.0 |             0.0 |             0.0 |
| restarts                 |             9.0 |             1.0 |          1.8316 |
| conflicts                |          1316.0 |             4.0 |          146.17 |
| decisions                |          1896.0 |            10.0 |          245.25 |
| propagations             |      6.0808e+04 |           605.0 |          6515.7 |
| conflict literals        |      1.8545e+04 |            44.0 |          1846.3 |
| Memory used (Mb)         |            0.64 |            0.33 |         0.46895 |
| CPU time (s)             |        0.023123 |        0.005062 |       0.0074462 |

<br>

### CNF set: top95.txt with EXTENDED encoding ###
CNFs solved: 95 (95 SAT, 0 UNSAT)  

| Stat                     |             Max |             Min |             Ave |
| :---                     |            ---: |            ---: |            ---: |
| Number of variables      |           729.0 |           721.0 |          728.15 |
| Number of clauses        |          4208.0 |          2468.0 |          3385.6 |
| Parse time (s)           |             0.0 |             0.0 |             0.0 |
| Eliminated clauses (Mb)  |             0.0 |             0.0 |             0.0 |
| Simplification time (s)  |             0.0 |             0.0 |             0.0 |
| restarts                 |             1.0 |             1.0 |             1.0 |
| conflicts                |            40.0 |             0.0 |          9.9579 |
| decisions                |            92.0 |             4.0 |          22.979 |
| propagations             |          3053.0 |           537.0 |          1255.6 |
| conflict literals        |           254.0 |             0.0 |          57.737 |
| Memory used (Mb)         |            0.59 |            0.36 |         0.46789 |
| CPU time (s)             |        0.006617 |        0.004763 |       0.0056711 |
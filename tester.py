#!/usr/bin/env python3

# CSC 322 Project 1
# Joshua Stein
# V00951354

import sys
import re
import subprocess

STAT_FIELD_NAMES = [
    "Number of variables",
    "Number of clauses",
    "Parse time (s)",
    "Eliminated clauses (Mb)",
    "Simplification time (s)",
    "restarts",
    "conflicts",
    "decisions",
    "propagations",
    "conflict literals",
    "Memory used (Mb)",
    "CPU time (s)",
]

STAT_FIELD_RE = re.compile(r'^\W*(?:(?:\w| )*\w) *: *(-?[0-9]*\.?[0-9]*)', flags=re.MULTILINE)

EASY_TEST_TXT = 'p096_sudoku.txt'
EASY_TEST_DIR = 'p096_sudoku_tests'
EASY_TEST_COUNT = 50

HARD_TEST_TXT = 'top95.txt'
HARD_TEST_DIR = 'top95_sudoku_tests'
HARD_TEST_COUNT = 95

CNF_ENC_MINIMAL =   'MINIMAL'
CNF_ENC_EFFICIENT = 'EFFICIENT'
CNF_ENC_EXTENDED =  'EXTENDED'



def main():
    # run_test(encoding=CNF_ENC_MINIMAL, easy_test=True) # fine
    # run_test(encoding=CNF_ENC_EFFICIENT, easy_test=True) # fine
    # run_test(encoding=CNF_ENC_EXTENDED, easy_test=True) # fine
    # run_test(encoding=CNF_ENC_MINIMAL, easy_test=False) # fine
    # run_test(encoding=CNF_ENC_EFFICIENT, easy_test=False) # fine
    run_test(encoding=CNF_ENC_EXTENDED, easy_test=False) # fine
    


def run_test(encoding=CNF_ENC_MINIMAL, easy_test=True):
    print("Generating CNFs...")
    generate_cnfs(encoding=encoding, easy_test=easy_test)
    print("Solving CNFs...")
    solve_cnfs(easy_test=easy_test)
    print("Analysing solves...")
    analyse_solves(easy_test=easy_test)


def read_sudokus_easy():
    sudokus = [''] * EASY_TEST_COUNT
    with open(EASY_TEST_TXT, 'r') as file:
        for i in range(EASY_TEST_COUNT):
            file.readline() # Read past 'Grid XX'
            for j in range(9): sudokus[i] += file.readline()
    return sudokus


def read_sudokus_hard():
    sudokus = [''] * HARD_TEST_COUNT
    with open(HARD_TEST_TXT, 'r') as file:
            for i in range(HARD_TEST_COUNT):
                sudokus[i] = file.readline()
    return sudokus


def generate_cnfs(encoding=CNF_ENC_MINIMAL, easy_test=True):

    # Create sudoku list
    TEST_COUNT = EASY_TEST_COUNT if easy_test else HARD_TEST_COUNT
    TEST_DIR = EASY_TEST_DIR if easy_test else HARD_TEST_DIR
    TEST_TXT = EASY_TEST_TXT if easy_test else HARD_TEST_TXT
    sudokus = read_sudokus_easy() if easy_test else read_sudokus_hard()

    for i in range(TEST_COUNT):
        with open(f"{TEST_DIR}/cnfs/puzzle{i+1}.cnf", 'w') as file:
            p = subprocess.run(['python3', 'sud2sat.py', encoding], input=sudokus[i], text=True, stdout=file, stderr=sys.stderr)
            if p.returncode:
                print(f"Error processing sudoku i={i} in {TEST_TXT} using {encoding} encoding", file=sys.stderr)
                exit(1)


def solve_cnfs(easy_test=True):
    # minisat puzzle.cnf assign.txt >stat.txt
    TEST_COUNT = EASY_TEST_COUNT if easy_test else HARD_TEST_COUNT
    TEST_DIR = EASY_TEST_DIR if easy_test else HARD_TEST_DIR

    for i in range(TEST_COUNT):
        cnf_filename =      f'{TEST_DIR}/cnfs/puzzle{i+1}.cnf'
        assign_filename =   f'{TEST_DIR}/assigns/assign{i+1}.txt'
        stat_filename =     f'{TEST_DIR}/stats/stat{i+1}.txt'
        with open(stat_filename, 'w') as file:
            p = subprocess.run(['minisat', cnf_filename, assign_filename], stdout=file, stderr=sys.stderr)


def analyse_solves(easy_test=True):
    TEST_COUNT = EASY_TEST_COUNT if easy_test else HARD_TEST_COUNT
    TEST_DIR = EASY_TEST_DIR if easy_test else HARD_TEST_DIR

    unsat_puzzles = [] # stores indexes (0-indexed) of all unsat puzzles
    stat_summaries = []

    for i in range(TEST_COUNT):

        # Check assign file
        assign_filename = f'{TEST_DIR}/assigns/assign{i+1}.txt'
        with open(assign_filename, 'r') as assign_file:
            sat_result = assign_file.readline()
        if sat_result.startswith('UNSAT'): unsat_puzzles.append(i)
        if not sat_result.startswith('SAT'):
            print(f"Error: unexpected first line in {assign_filename}", file=sys.stderr)
            exit(1)
        
        # Read stat summary from stat field
        stat_filename = f'{TEST_DIR}/stats/stat{i+1}.txt'
        with open(stat_filename, 'r') as stat_file:
            stat_summary_raw = STAT_FIELD_RE.findall(stat_file.read())
            if len(stat_summary_raw) != len(STAT_FIELD_NAMES):
                print(f"Error: unexpected stat lines read from {stat_filename}", file=sys.stderr)
                exit(1)
            stat_summaries.append([float(stat) for stat in stat_summary_raw])

    stats_max = [stat for stat in stat_summaries[0]]
    stats_min = [stat for stat in stat_summaries[0]]
    stats_sum = [stat for stat in stat_summaries[0]]

    for i in range(1, TEST_COUNT):
        for j in range(len(STAT_FIELD_NAMES)):
            stat = stat_summaries[i][j]
            if stat > stats_max[j]: stats_max[j] = stat
            elif stat < stats_min[j]: stats_min[j] = stat
            stats_sum[j] += stat
    
    print(f"Puzzles analysed: {TEST_COUNT} ({TEST_COUNT - len(unsat_puzzles)} SAT, {len(unsat_puzzles)} UNSAT)")

    # Print stats
    headers = ['Stat', 'Max', 'Min', 'Ave']
    print(f"{headers[0]:24}{headers[1]:>15}{headers[2]:>15}{headers[3]:>15}")
    for i in range(len(STAT_FIELD_NAMES)):
        print(f"{STAT_FIELD_NAMES[i]:24}{stats_max[i]:15.5}{stats_min[i]:15.5}{(stats_sum[i]/TEST_COUNT):15.5}")


if __name__ == '__main__':
    main()
#!/usr/bin/env python
#
# Simplest possible implementation:
# 1. Read in a question
# 2. Print the question and wait for input
# 3. Loop until out of questions
# 4. Print summaries

from __future__ import division
import os

valid_answers = ["Very true", "True", "Neutral", "Untrue", "Very untrue"]
groups = { 'PN': 'Past Negative', 'PP': 'Past Positive', 'PF': 'Present Fatalistic', 'PH': 'Present Hedonistic', 'FU': 'Future' }

def print_instructions():
    os.system('clear')
    print("ZTPI (short version) v0.3")
    print("\n")
    print("Answer each of the following questions with a number between 1 - 5:")
    for idx, answer in enumerate(valid_answers):
        print 5 - idx, " = ", answer
    print("(You can also answer \"b\" to go back one question or \"r\" to restart)")
    print("\n")

def read_questions(questions_file):
    f = open(questions_file, 'r')
    lines = f.read().split('\n')
    return lines[:-1]

def get_answers(questions):
    numq = len(questions)
    answers = numq*[0]
    i = 0
    while i < numq:
        answer = raw_input(questions[i][3:])
        if answer == "q":
            raise SystemExit
        elif answer == "r":
            i = 0
        elif answer == "b":
            if i > 0:
                i = i - 1
        elif answer in ["1", "2", "3", "4", "5"]:
            answers[i] = int(answer)
            i = i + 1
        else:
            print("Please enter a number between 1-5, b to go back, r to restart, or q to quit\n")
    return answers

def print_summary(questions, answers):
    print("Summary: ")
    for group in groups:
        score = 0
        total = 0
        for idx, question in enumerate(questions):
            if question[:2] == group:
                score += answers[idx]
                total += 1
        print "\t", groups[group], " = ", score / total

if __name__ == "__main__":
    questions = read_questions("questions.txt")
    while True:
        print_instructions()
        answers = get_answers(questions)
	done = False
    	while not done:
    	    print_summary(questions, answers)
    	    answer = raw_input("Type 'r' and press Enter to restart the test.")
    	    if answer == "r":
    	        done = True

from first.first import greeting

# write unit tests for the function greeting(name, language) in first/first.py
# include different test cases by writing different unit tests
# their names should reflect the test case, e.g. test_greeting_eng() if english is selected
# use assert to check that your output matches your expectation: assert greeting(name, language) == "expected string"
# when you have new tests ready, try to run pytest to see if they clear: pytest
# if you like, add other languages to your greeting() function and test for them
# add your changes: git add first/tests/first_test.py
# commit your changes using commit message conventions (https://inpred.github.io/24-03_bioinfo_ws/#19): git commit -m "test: <your commit message>"

import pytest

def test_greeting_default():
    assert greeting("Jaime", "Spanish") == "I don't speak your language!"

def test_greeting_English():
    assert greeting("Jaime", "English") == "Hello Jaime!"

def test_greeting_Norwegian()):
    assert greeting("Jaime", "Norwegian") == "Hei Jaime!"

def test_greeting_english()):
    assert greeting("Jaime", "english") == "Hello Jaime!"
import session10
from session10 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
	"Sequence",
	"strings",
	"lists",
	"tuples",
	"range",
	"__init__",
	"__eq__",
	"__gt__",
	"__repr__",
	"__init__",
	"__repr__",
	"__getitem__",
	"polygon",
	"isinstance"
   
]

def test_readme_exists():
	assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
	readme = open("README.md", "r")
	readme_words = readme.read().split()
	readme.close()
	assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
	READMELOOKSGOOD = True
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	for c in README_CONTENT_CHECK_FOR:
		if c not in content:
			READMELOOKSGOOD = False
			pass
	assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	assert content.count("#") >= 10

def test_indentations():
	''' Returns pass if used four spaces for each level of syntactically \
	significant indenting.'''
	lines = inspect.getsource(session10)
	spaces = re.findall('\n +.', lines)
	for space in spaces:
		assert len(space) % 4 == 2, "Your script contains misplaced indentations"
		assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
	functions = inspect.getmembers(session10, inspect.isfunction)
	for function in functions:
		assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


@pytest.mark.parametrize('side,radius,int_angle, edge_len,apothem,area,perim',[(5,12,'108.0','14.11','9.71','342.52','70.55'),\
	(8,12,'135.0', '9.18', '11.09', '407.22', '73.44'),\
	(4,6,'90.0','8.49','4.24','72.00','33.96')
	])
def test_who_faster(side,radius,int_angle, edge_len,apothem,area,perim):
	poly = Polygon(side, radius)
	assert poly.interior_anagle() == int_angle, 'interior angle mismatch'
	assert poly.edge_length() == edge_len, 'edge lenght mismatch'
	assert poly.apothem() == apothem, 'apothem mismatch'
	assert poly.area() == area, 'area mismatch'
	assert poly.perimiter() == perim, 'perimeter mismatch'






	
	


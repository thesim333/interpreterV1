"""
>>> from src.validator.age import Age
>>> a = Age('15'); a.validate()
'Valid'

>>> a = Age('14'); a.validate()
'Age must be be 14 < 80'

>>> a = Age('1'); a.validate()
'Age must be 2 numbers'

>>> from src.validator.dob import DOB
>>> a = DOB('09-08-1982'); a.validate()
'Valid'
>>> a.check_age_against_date(34)
'Valid'

>>> from src.validator.bmi import BMI
>>> a = BMI("Normal"); a.validate()
'Valid'

>>> a = BMI("normal"); a.validate()
'BMI not a valid option'

>>> from src.validator.emd_id import EmpID

>>> a = EmpID('A123'); a.validate()
'Valid'

>>> a = EmpID('a123'); a.validate()
'Employee ID must be of format "X000"'

>>> a = EmpID('A12'); a.validate()
'Employee ID must be of format "X000"'

>>> a = EmpID('A1234'); a.validate()
'Employee ID must be of format "X000"'

>>> a = EmpID('AAAA'); a.validate()
'Employee ID must be of format "X000"'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

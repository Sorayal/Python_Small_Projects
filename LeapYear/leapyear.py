#!/usr/bin/python3
# control structures

year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Dieses Jahr ist ein Schaltjahr")
        else:
            print("Dieses Jahr ist kein Schaltjahr")
    else:
        print("Dieses Jahr ist ein Schaltjahr")
else:
    print("Dieses Jahr ist kein Schaltjahr")

truth_table = """
--------------------------------------------------------------------
|  3 expression variables : n                                      |
|  2^n : 2 ^ 3 = 8 rows / possible results                         |
|                                                                  |
| year % 4 == 0 | year % 100 == 0 | year % 400 == 0 | is leap year |
--------------------------------------------------------------------
|       w       |        w        |        w        |       w      | <-
|       w       |        w        |        f        |       f      |
|       w       |        f        |        w        |       w      | <-
|       w       |        f        |        f        |       w      | <-
|       f       |        w        |        w        |       f      |
|       f       |        f        |        w        |       f      |
|       f       |        w        |        f        |       f      |
|       f       |        f        |        f        |       f      |
--------------------------------------------------------------------
"""

print(truth_table)

# Shorter modified version
isLeap = (year % 4 == 0 and not (
    year % 100 == 0)) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)
if isLeap:
    print("Dieses Jahr ist ein Schaltjahr")
else:
    print("Dieses Jahr ist kein Schaltjahr")

# even shorter version
isleap = year % 4 == 0 and not year % 100 == 0 or year % 400 == 0
if isLeap:
    print("Dieses Jahr ist ein Schaltjahr")
else:
    print("Dieses Jahr ist kein Schaltjahr")

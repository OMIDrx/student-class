# student-class
Simple Python Student class
# Student Class (Python)

A simple Python class to manage student grades.

## Features
- Calculate average grade
- Determine student status

## Status Rules
- Average >= 17 → Excellent
- 12 <= Average < 17 → Okay
- Average < 12 → Very Bad

## Example

```python
from student import Student

s1 = Student("Omid", [18, 15, 20])

print(s1.average())
print(s1.status())

17.67
Excellent

- Commit message:

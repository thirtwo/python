text = "Office workers, students, small/home business workers, and administrators would want to improve their productivity."
count = {}

for char in sorted(text.upper()):
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)
import pprint
pprint.pprint(count)

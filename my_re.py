import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# re.M是多行匹配，re.I是对大小写不敏感
if matchObj:
    print(matchObj.group(1))
    print(matchObj.group(2))
else:
    print("no match")

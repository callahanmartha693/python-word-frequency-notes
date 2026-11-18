import re
from collections import Counter

def solve(value):
    return dict(Counter(re.findall(r'[^\W_]+', value.casefold())))

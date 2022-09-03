import json

st = '"{"TT": {"LDR1": 51, "LDR2": 186, "LDR3": 91, "LDR4": 134, "T": 32.1, "A": 76.63, "P": 100418, "X": -2, "Y": -2}, "ADCS": {"X": 4, "Y": 10, "Z": 80, "A": 932}}"'
new = json.loads(st[1:-1])
print(new['TT'])
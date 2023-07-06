# sets do not allow repetition

s = set()

s.add(4)
s.add(5)
s.add(6)
s.add(5)
s.add(6)

s.remove(6)

print (f"set s contains {len(s)} elements")

print (s)
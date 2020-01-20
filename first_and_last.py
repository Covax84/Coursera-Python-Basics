s = input()
pos1 = s.find('f')
pos2 = len(s) - 1 - s[::-1].find('f') if s[::-1].find('f') != -1 else 0
if pos1 != -1:
    if pos2 and pos2 != pos1:
        print(pos1, pos2)
    else:
        print(pos1)

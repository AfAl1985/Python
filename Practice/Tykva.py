k = 0
for b1 in 'tykva':
    for b2 in 'tykva':
        for b3 in 'tykva':
            for b4 in 'tykva':
                for b5 in 'tykva':
                    for b6 in 'tykva':
                        res = b1+b2+b3+b4+b5+b6
                        if res [0] in 'tkv' and res [-1] in 'tkv':
                            if res.count('a') + res.count('y') == 2:
                                k += 1
                                print(res)

print(k)
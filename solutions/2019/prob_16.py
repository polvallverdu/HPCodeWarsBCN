def aminoacid(sequence):
    tabla = {'AA': 'Glycine', 'AT': 'Cysteine', 'AU': 'START', 'TA': 'END', 'TT': 'END', 'TU':
             'Arginine', 'UA': 'Serine', 'UT': 'DELETE', 'UU': 'Lysine'}
    aminolist = []
    seq = sequence
    exit = False
    coding = False
    while not exit:
        if len(seq) < 2:
            break
        codon = tabla[seq[:2]]
        if codon == 'START':
            coding = True
            seq = seq[2:]
        elif codon == 'END':
            if coding:
                exit = True
            else:
                seq = seq[1:]
            coding = False
        else:
            if coding:
                if codon == 'DELETE':
                    aminolist.pop()
                else:
                    aminolist.append(codon)
                seq = seq[2:]
            else:
                seq = seq[1:]
    if len(aminolist) == 0 or not exit:
        return 'NONE'
    else:
        return ','.join(aminolist)


sequence = input()
exit = aminoacid(sequence)
print(exit)

##str="ANILKO FRCY IDOWPBLV, YB SPBLSPNY CG FKDT NZ GTSM CG FRCY OPNDFKLULY. FRCY YBKFSFLV ZULY YPHTFECV, UBFR FRCY IDLN HRLULUOV TIRMRFSX KDNY NZ PTKCSC TICYFYCY CIMXLUOV FRLGKMLZ FRCY GTCYPE. YB RLDTNY DM RECYPY GTUHSH, CYOSGLPS RLNYSPLN ZUBFHTNHSH, KDNY CDLMDPNY TIFDFRFKURKO WRBYLY THPO FRCY YPKULY. LU FRCY TYCDLUPR, YB QKFRTSPS KHMNDA NZ FNOQBHST, LGDHBRKO QUIHIQNHCXYI KDNY HRKHLUOV REGLSBLY. FRCY ULQRER YBST OXXC KDNY OCFDLV, UBFR FRCY RDZY BACNCN QC REKHLY. RB ZULY NZ YPNFFTNI PEFNYP THPO FRCY IARESC KDNY MIRESC QC TYTSDSDZ SLTF, NZ FLKDEF CG STOXLNDCEB UBFR DKBKST KDNY FDFL GCSFLV"
str="VHVSSPQUCEMRVBVBBBVHVSURQGIBDUGRNICJQUCERVUAXSSR"
arr1 = []      ##contain frequency of singe letter
for i in range(26):
        substr = "" + chr(i + 65)  + ""     # X
        if str.count(substr) > 1:
            arr1.insert(0, ( str.count(substr), substr))

arr1.sort(reverse=True)
print("Frequency Of Single Character in Cypertext:\n",arr1)

arr2 = []       ##contain frequency of digraphs
for i in range(26):
    for j in range(26):
        substr = "" + chr(i + 65) + chr(j + 65) + ""     #XY
        if str.count(substr) > 1:
            arr2.insert(0, ( str.count(substr), substr))
arr2.sort(reverse=True)
print("\n\nFrequency Of digraphs in Cypertext:\n",arr2)

arr3 = []      ##contain frequency of trigraph
for i in range(26):
    for j in range(26):
        for k in range(26):
            substr = "" + chr(i + 65) + chr(j + 65) + chr(k + 65) + ""   #XYZ
            if str.count(substr) >1:
                arr3.insert(0, ( str.count(substr), substr ))
arr3.sort(reverse=True)
print("\n\nFrequency Of trigraph 3 letter  in Cypertext:\n",arr3)
arr4=[]      ##contain frequency of 4 length word
for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(26):
                substr = "" + chr(i + 65) + chr(j + 65) + chr(k + 65) +chr(l+65) + ""   #ABCD
                if str.count(substr) >1:
                    arr4.insert(0, ( str.count(substr), substr ))
arr4.sort(reverse=True)
print("\n\nFrequency Of 4 letter word in Cypertext:\n",arr4)

arr5=[]     ##contain frequency of 5 letter word 
for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(26):
                for m in range(26):
                    substr = "" + chr(i + 65) + chr(j + 65) + chr(k + 65) +chr(l+65)+chr(m+65)+ ""  #ABCDE
                    if str.count(substr) >1:
                       arr5.insert(0, ( str.count(substr), substr ))

arr5.sort(reverse=True)
print("\n\nFrequency Of 5 letter word in Cypertext:\n",arr5)



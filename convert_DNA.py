import math
from textwrap import wrap
def ternary(n):
    e = n // 3
    q = n % 3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)
def bin2DNAcode0(num):
    codes = {
        'A' : 'C',
        'C' : 'G',
        'G' : 'T',
        'T' : 'A'
    }
    return codes.get(num)
def bin2DNAcode1(num):
    codes = {
        'A' : 'G',
        'C' : 'T',
        'G' : 'A',
        'T' : 'C'
    }
    return codes.get(num)
def bin2DNAcode2(num):
    codes = {
        'A' : 'T',
        'C' : 'A',
        'G' : 'C',
        'T' : 'G'
    }
    return codes.get(num)
def bin2Code(num, DNAcode):
    codes = {
        '0' : bin2DNAcode0(DNAcode),
        '1' : bin2DNAcode1(DNAcode),
        '2' : bin2DNAcode2(DNAcode)
    }
    return codes.get(num)

def DNAEncode(binSeq, dna_length):
    n = 3
    x1 = ''
    for i in range(math.ceil(len(binSeq) / n)):
        temp = binSeq[n * (i + 1) - n:n * (i + 1)]
        b = int(temp, 2)
        x1 = x1 + ternary(b).zfill(2)
    y1 = ['A']
    for i in range(1, len(x1)):
        d1 = x1[i]
        d2 = y1[i - 1]
        y1.append(bin2Code(d1, d2))
    y1 = ''.join(y1)
    res = len(y1) % dna_length
    add1 = 'ATCG'
    add2 = 'ATCG'
    for i in range(math.ceil((dna_length - res) / 4)):
        add1 = add1 + add2
    y1 = y1 + add1[0: dna_length - res]
    encodeDNA = wrap(''.join(y1), dna_length) 
    return encodeDNA, res
import math
def DNAcode2BinA(num):
    codes = {
        'C': '0',
        'G': '1',
        'T': '2'
    }
    return codes.get(num)
def DNAcode2BinC(num):
    codes = {
        'G': '0',
        'T': '1',
        'A': '2'
    }
    return codes.get(num)
def DNAcode2BinG(num):
    codes = {
        'T': '0',
        'A': '1',
        'C': '2'
    }
    return codes.get(num)
def DNAcode2BinT(num):
    codes = {
        'A': '0',
        'C': '1',
        'G': '2'
    }
    return codes.get(num)
def code2Bin(num, DNAcode):
    codes = {
        'A' : DNAcode2BinA(DNAcode),
        'C' : DNAcode2BinC(DNAcode),
        'G' : DNAcode2BinG(DNAcode),
        'T' : DNAcode2BinT(DNAcode)
    }
    return codes.get(num)
def ter2Dec(n):
    res = 0
    for index, value  in enumerate(str(n)[::-1]):
        res += int(value) * 3**index
    return res
def DNADecode(DNA, y_start, dna_length, res):
    DNA = ''.join(DNA)
    DNASeq = DNA[0:len(DNA) - (dna_length - res)] 
    print(DNASeq)
    y2 = y_start
    for i in range(1, len(DNASeq)):
        d1 = DNASeq[i]
        d2 = DNASeq[i - 1]
        y2 = y2 + code2Bin(d2, d1)
    n = 2
    print(y2)
    binSeq = ''
    for i in range(math.ceil(len(y2) / n)):
        temp = y2[n * (i + 1) - n:n * (i + 1)]
        if i == math.ceil(len(y2) / n) - 1:
            b = bin(ter2Dec(temp))[2:]
        else:
            b = bin(ter2Dec(temp))[2:].zfill(3)
        binSeq = binSeq + b
    return binSeq
def code2Bin(num):
    codes = {
        'A' : '00',
        'T' : '01',
        'C' : '10',
        'G' : '11'
    }
    return codes.get(num)
def DNADecode(DNASeq, dna_length, res):
    DNASeq = ''.join(DNASeq)
    DNA = DNASeq[0:len(DNASeq) - (dna_length - res)] 
    print(DNA)
    y2 = '' 
    for i in range(0, len(DNA)):
        d1 = DNA[i]
        y2 = y2 + code2Bin(d1)
    return y2
import math
from textwrap import wrap
def bin2DNACode(num):
    codes = {
        '00' : 'A',
        '01' : 'T',
        '10' : 'C',
        '11' : 'G'
    }
    return codes.get(num)

def DNAEncode(binSeq, dna_length):
    y1 = ['']
    n = 2
    for i in range(math.ceil(len(binSeq) / n)):
        temp = binSeq[n * (i + 1) - n:n * (i + 1)]
        y1.append(bin2DNACode(temp))
    y1 = ''.join(y1)
    print(y1)
    res = len(y1) % dna_length
    add1 = 'ATCG'
    add2 = 'ATCG'
    for i in range(math.ceil((dna_length - res) / 4)):
        add1 = add1 + add2
    y1 = y1 + add1[0 : dna_length - res]
    encodeDNA = wrap(''.join(y1), dna_length) 
    return encodeDNA, res

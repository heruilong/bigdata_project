import os

def ATCG_count(genomeVal='Human', seqTypeVal='genomic'):
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt'
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    count = 0
    countRes = [0,0,0,0]
    with open(absPath, 'r') as f:
        for line in f:
            if ">" in line:
                continue
            else:
                c_a = line.count('A') + line.count('a')
                c_c = line.count('C') + line.count('c')
                c_g = line.count('G') + line.count('g')
                c_t = line.count('T') + line.count('t')
                countRes[0] = countRes[0] + c_a
                countRes[1] = countRes[1] + c_c
                countRes[2] = countRes[2] + c_g
                countRes[3] = countRes[3] + c_t
    print str(countRes)

if __name__ == "__main__":
    ATCG_count('Sea hare', 'genomic')

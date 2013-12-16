import sys
import os.path

def readLocal(rltvPath):
    absPath = os.path.join(os.path.dirname(__file__),rltvPath)
    f = open(absPath,'r')
    return f.read()

def test():
    print readLocal('../statistic/fasta_test.txt')

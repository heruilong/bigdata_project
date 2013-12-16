#!/usr/bin/env python
import sys
import time

# The program is to implement linear time algorithm for suffix array construction.
# The reference is DC3.
# Author: Xiang Niu, Yao Huang

def compare(a1, a2, b1, b2):
   return a1 < b1 or ( a1 == b1 and a2 <= b2)

def compare3(a1, a2, a3, b1, b2, b3):
   return (a1 < b1 or (a1 == b1 and compare(a2, a3, b2, b3)))

# Radix sort
def radix(a, b, r, n, K):
   c = [0 for i in xrange(K+1)]
   for i in xrange(n): c[r[a[i]]] += 1   
   for i in xrange(K + 1): 
      if i == 0: sum = 0
      t = c[i]; c[i] = sum; sum += t   
   for i in xrange(n):      
      b[c[r[a[i]]]] = a[i]
      c[r[a[i]]] += 1

def GetI(SA12t, n0):
   if SA12t < n0: return SA12t * 3 + 1  
   else: 
      return (SA12t - n0) * 3 + 2

# Get suffix array SA
def suffixArray(s, SA, n, K):
   n0, n1, n2 = (n + 2) / 3, (n + 1) / 3, n / 3
   n02 = n0 + n2
   
   s12 = getS12(n, n0, n1, n02)
   SA12 = radixRank(s12, s, n02,K)
   s12,SA12 = getS12Rank(n0, n02, s, s12, SA12)

   s0 = getS0(n0, n02, SA12)
   SA0 = getSA0(s0, n0, s, K)
   
   merge(n, n0, n1, n02, SA12, SA0, SA, s, s12)

# Get all the positions which the remaining value is not equal to 0.
# Return the array contains all proper positions.
def getS12(n, n0, n1, n02):
   s12 = []
   for i in xrange(n + (n0 - n1)):
      if i%3 != 0 : s12.append(i)        
   while(len(s12) < n02 + 3) : s12.append(0)
   return s12

# Get the sub ranks and sub positions from the range of B1 and B2.
# Return positions array and rank array. 
def getS12Rank(n0, n02, s, s12, SA12):
   name = 0
   c0, c1, c2 = -1, -1, -1
   for i in xrange(n02):
      if s[SA12[i]] != c0 or s[SA12[i] + 1] != c1 or s[SA12[i] + 2] != c2 :
         name += 1
         c0, c1, c2 = s[SA12[i]], s[SA12[i] + 1], s[SA12[i] + 2]
      if SA12[i] % 3 == 1: s12[SA12[i]/3]      = name
      else               : s12[SA12[i]/3 + n0] = name
      
   if name < n02 :
      suffixArray(s12, SA12, n02, name)
      for i in xrange(n02) : s12[SA12[i]] = i + 1
   else :
      for i in xrange(n02) : SA12[s12[i] - 1] = i
   return s12, SA12

# Get the corresponding rank for the triple strings.
# Compare from unit, tens, to hundreds.
# Return the ranking array.
def radixRank(s12, s, n02, K):
   SA12 = [0 for i in xrange(n02 + 3)]
   radix(s12 , SA12, s[2:], n02, K)
   radix(SA12, s12,  s[1:], n02, K)
   radix(s12 , SA12, s    , n02, K)
   return SA12

# Get the position array after sorting.
# Return an ordered array sorting alphbetically.
def getSA0(s0, n0, s, K):   
   SA0 = [0 for i in xrange(n0)]
   radix(s0, SA0, s, n0, K)
   return SA0

# Get all position that safisfies the remaining value is 0 after mod by 3.
def getS0(s, n02, SA12):
   s0 = [0 for i in xrange(s)]
   for i in  xrange(n02):
      if i == 0: j = 0 
      if (SA12[i] < s) :         
         s0[j] = 3 * SA12[i]
         j += 1
   return s0

# Merge two parts, SA12 and SA0 to SA
def merge(n, n0, n1, n02, SA12, SA0, SA, s, s12):
   k = 0
   while(k < n):
      if k == 0: p = 0; t = n0 - n1
      i = GetI(SA12[t], n0)
      j = SA0[p]
      if compare(s[i], s12[SA12[t] + n0], s[j], s12[j/3]) if SA12[t] < n0 else compare3(s[i],s[i+1],s12[SA12[t]-n0+1], s[j],s[j+1],s12[j/3+n0]):
         SA[k] = i; t += 1
         if t == n02:
            while(p < n0):
               k += 1
               SA[k] = SA0[p]
               p += 1    
      else    :
         SA[k] = j; p += 1
         if p == n0:
            while(t < n02):
               k += 1
               SA[k] = GetI(SA12[t],n0)
               t += 1               
      k += 1

# Change characters to unique integer
def dna2int(dna):
   if   dna == 'a' or dna == 'A': return 1
   elif dna == 'c' or dna == 'C': return 2
   elif dna == 'g' or dna == 'G': return 3
   elif dna == 't' or dna == 'T': return 4
   elif dna == 'n' or dna == 'N': return 5
   elif dna == '0'		: return 0   

# Append input with triple 0s that could make sure the last character 
# could have valid triple set.
def getInput(input):
   input = [ dna2int(t) for t in input]
   input.append(0)
   input.append(0)
   input.append(0)
   return input

def getSA(input): 
   n = len(input)
   input = getInput(input)
   SA = [0 for i in xrange(n)]
   K = 5
   t1 = time.time()
   suffixArray(input, SA, n, K)
   t2 = time.time()
   #print "dc3 time is: \t\t\t\t%s" % str(t2-t1)
   return SA

if __name__=="__main__":
   print getSA(sys.stdin.read().rstrip())

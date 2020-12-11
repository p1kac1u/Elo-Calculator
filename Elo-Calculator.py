#!/usr/bin/env python3

'''
MIT LICENSE

Copyright 2020 p1kac1u
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import math

#Input current ratings
r1 = int(input("Enter your current ratings: "))
r2 = int(input("Enter your opponent's current ratings: "))
k = int(input("Enter the k-factor: "))

#Input Score
s1 = int(input("Enter your score: "))
s2 = int(input("Enter your opponent's score: "))

#Calculate Expected Ratings
exp1 = 1 / (1 + 10 ** ((r2-r1) / 400))
exp2 = 1 / (1 + 10 ** ((r1-r2) / 400))

#Calculate New Ratings
nr1 = (r1 + (s1-exp1)*k)
nr2 = (r2 + (s2-exp2)*k)

#Print the new ratings with rounded
nr1 = math.floor(nr1)
nr2 = math.floor(nr2)
print(nr1)
print(nr2)

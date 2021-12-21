from z3 import *

bits_count = 32

x, y = BitVecs('x y', bits_count)

# min(x,y)
c = If(x < y, BitVecVal(-1, 32), BitVecVal(0, 32))
trick = y ^ ((x ^ y) & c)
simple_min = If(x < y, x, y)
prove(trick == simple_min)

# max(x,y)
c = If(x < y, BitVecVal(-1, 32), BitVecVal(0, 32))
trick = x ^ ((x ^ y) & c)
simple_min = If(x > y, x, y)
prove(trick == simple_min)

# opposite signs -> sign(x) != sign(y)
trick = (x ^ y) < 0
opposite = Or(And(x < 0, y >= 0), And(x >= 0, y < 0))
prove(trick == opposite)

# abs(x)
mask = x >> bits_count - 1
trick = (x + mask) ^ mask
simple_abs = If(x < 0, -1 * x, x)
prove(trick == simple_abs)

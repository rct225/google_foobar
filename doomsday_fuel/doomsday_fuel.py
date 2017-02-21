from fractions import Fraction, gcd

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

def answer(m):
   ct = 0
   ts = []
   p_m = []
   for r in m:
      if sum(r) != 0:
         p_r = [float(i)/sum(r) for i in r]
      else:
         ts.append(ct)
         p_r = len(r)*[0.0]
      p_m.append(p_r)
      ct += 1

   p = []
   out = [0.0]*len(m)
   
   if sum([row[0] for row in m]) != 0:
      for i in xrange(len(p_m)):
         p.append([row[i] for row in p_m])

         s = 0.0
      for t in ts:
         s += p[t][1]
            
      for t in ts:
         x = 1.0 / (1.0 + s)
         out[t]= p[t][1]*x
               
      for t in ts:
         if sum([row[t] for row in m]) != 0 and out[t] == 0.0:
            out[t] = 1 - sum(out)
   else:
      for i in xrange(len(p_m[0])):
         if i not in ts:
            p.append([p_m[0][i]*j for j in p_m[i]])

      if len(p) > 0:
         out = p[-1]
      else:
         out.append(1)
         return out

      if sum(out) < 1.0:
         for t in ts:
            if out[t] == 0:
               out[t] = 1.0 - sum(out)

   out = out[ts[0]::]

   out_f = [Fraction(o).limit_denominator() for o in out]# if o > 0.0]
   out_fd = [o.denominator for o in out_f]
    
   out_lcm = reduce(lcm,out_fd)
   out_answer = [o.numerator * out_lcm / o.denominator for o in out_f]
   out_answer.append(out_lcm)

   return out_answer


test1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
test2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print answer(test1)
print answer(test2)

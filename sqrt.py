def continuum(r,power):
  square = (r+power)**2
  return square

n = [3.1,.81]
threshold = 0.00001

def mySqrt(n):
  roots = []
  for num in n:
    for root in range(round(num+1)):
      if root**2 == num:
        #print(root)
        roots.append(root)
        break
        
      elif root**2 > num:
        power = 0.1
        r = root-1
        while abs(continuum(r,power) - num) > threshold:
          #print(r)
          power *= .1
          r+=power
          while continuum(r,power) - num < threshold:
            #print(r)
            r+=power
          if continuum(r,threshold)>num:
            #print(r)
            roots.append(r)
            break     
        break
  return roots

print(mySqrt(n))

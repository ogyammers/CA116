low = 0
high = len(a)

while low < high:
   mid = (low + high) // 2

   if a[mid] < q:
      low = mid + 1
   else:
      high = mid

p = low

#000403_01_08_hw03_ring.py
min = int(input ())
h = int(input ())
m = int(input ())
ringmin = min + h*60 + m
print (ringmin//60)
print (ringmin%60)
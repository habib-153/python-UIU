
# num = [1, 2, 3, 4, 4, 5]

# for n in num:
#     if (n == 4):
#         remove:(n)
#     else:
#         print(n)
# motor = ['honda', 'yamaha', ['kawasaki', 'bajaj'], 'sujuki', 'hero']
# print(sorted(motor, key=str))


# motor = ["honda", "yamaha", ["kawasaki", "bajaj"], "suzuki", "hero"]
# for i in range (len (motor)):
#   if isinstance (motor [i], list):
#     motor [i].sort ()
# motor.sort (key=lambda x: x [0] if isinstance (x, list) else x)
# print (motor)

motor = ["honda", "yamaha", ["kawasaki", "bajaj"], "suzuki", "hero"]
sorted_motor = [sorted (x, key=str) if isinstance (x, list) else x for x in motor]
sorted_motor = sorted (sorted_motor, key=str)
print(sorted_motor)
path = "6_Seminar\mimikriya_in.txt"
with open(path, 'r') as text:
    in_data = text.read()
data = in_data.split(' ')
print(data)
# transformation = lambda x: x
def transformation(x): return x


transformed_values = list(map(transformation, data))
# print(transformed_values)
if data == transformed_values:
    print('OK')
else:
    print('Not match')

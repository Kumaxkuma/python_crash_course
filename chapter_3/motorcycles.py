motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[1] = 'harley'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles[-2] = 'crotchrocket'
print(motorcycles)

motorcycles = []

motorcycles.append('ducati')
motorcycles.append('suzuki')
motorcycles.append('honda')

print(motorcycles)

motorcycles.insert(0, 'crotchrocket')
print(motorcycles)

motorcycles.insert(2, 'harley')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycles = []
print(popped_motorcycles)
popped_motorcycles.append(motorcycles.pop())
print(motorcycles)
print(popped_motorcycles)

motorcycles.pop(2)
print(motorcycles)

a_joke = motorcycles.pop(0)
print(f"The first motocycle I owned was a {a_joke.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

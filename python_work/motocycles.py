motocycles = ['honda' , 'yamaha',  'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)
motocycles.append('dayun')
print(motocycles)
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)
motocycles.insert(2,'dayun')
del motocycles[2]
print(motocycles)
motocycles = ['honda' , 'yamaha' , 'suzuki']
print(motocycles)
popped_motocycles  = motocycles.pop(0)
print(motocycles)
print (f"The Last I owned motocycle is {popped_motocycles.title()}.")
motocycles = ['honda' , 'suzuki' , 'yamaha' , 'ducati']
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive,I cannot buy it.")

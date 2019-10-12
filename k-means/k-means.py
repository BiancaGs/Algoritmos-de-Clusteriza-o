
file = open('../Instrucoes/datasets/c2ds1-2sp.txt', 'r')

lines = file.read().split('\n')

print(lines[1].split())

# for i in range(1, len(lines)):
#     print(lines[i])
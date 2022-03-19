# Conjuntos e subconjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9, 0}
print(type(conjunto))
conjuntoUniao = conjunto.union(conjunto2)
print(conjuntoUniao)
# instersect
conjuntoInterseccao = conjunto.intersection(conjunto2)
print(conjuntoInterseccao)
# diference

# diferença simétrica = tudo o que não tem nos dois conjuntos comparados
conjuntoDiffSimetrica = conjunto.symmetric_difference(conjunto2)
print(f'Conjunto Diferença Simétrica: {conjuntoDiffSimetrica}')

# Pertinência: métodos que retornam valores booleanos
conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}

#issubset
conjuntoSubset = conjuntoB.issubset(conjuntoA)
print(conjuntoSubset)

#issuperset
conjuntoSuperset = conjuntoB.issuperset(conjuntoA)
print(conjuntoSuperset)

#é possivel converter listas para conjuntos
lista = ['Cachorro', 'Cachorro', 'Gato', 'Calopsita', 'Jabuti']
conjuntoAnimais = set(lista)
print(conjuntoAnimais)

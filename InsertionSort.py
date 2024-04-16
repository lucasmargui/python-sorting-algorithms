def insercao(vet, tam):
    for i in range(1, tam):
        x = vet[i]
        j = i - 1
        while j >= 0 and x < vet[j]:
            vet[j + 1] = vet[j]
            j -= 1
        vet[j + 1] = x

# Example usage:
vetor = [3, 7, 1, 4, 6, 2, 5]
tam = len(vetor)

print("Before sorting:", vetor)
insercao(vetor, tam)
print("After sorting:", vetor)

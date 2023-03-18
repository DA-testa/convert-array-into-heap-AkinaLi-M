# Veronika Musijaka 221RDB124 13.gr


def build_heap(data):
    n = len(data)
    swaps = []
    # sākot no pēdējā mezgla, kas nav lapu, veic izsijāšanas darbības, lai izveidotu kaudzi
    for i in range(n // 2, -1, -1):
        swaps += sift_down(data, i, n)
    return swaps

def sift_down(data, i, n):
    swaps = []
    # atrast mezgla i mazākā bērna indeksu
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    # ja vecāks nav mazāks par savu mazāko bērnu, nomaina tos un veic bērnam izsijāšanas operāciju
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        swaps += sift_down(data, min_index, n)
    return swaps

def main():
    
    input_method = input("Please enter the input method (I or F): ")

    if "I" in input_method:
        n = int(input("Please enter a number of elements: "))
        data = list(map(int, input("Plese enter the elements: ").split()))

    if "F" in input_method:
        filename = input("Please enter the name of file: ")

        with open(f"tests/{filename}") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    assert len(data) == n

    
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

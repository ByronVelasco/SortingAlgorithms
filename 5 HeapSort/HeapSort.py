# %% [markdown]
# ## **Max-Heapify Algorithm**

# %%
def MaxHeapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = left + 1
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, n, largest)

# %% [markdown]
# ## **Heap Sort Algorithm**

# %%
def HeapSort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        MaxHeapify(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        MaxHeapify(A, i, 0)



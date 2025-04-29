# **HeapSort**

This module contains the file `HeapSort.ipynb`, which implements the Heap Sort algorithm using a Max Heap.

## **Heap Sort Algorithm**

Heap Sort is a comparison-based sorting technique based on a Binary Heap data structure. It works by:

1. Building a **Max Heap** from the input list.
2. Repeatedly swapping the first element (maximum) with the last unsorted element.
3. Reducing the heap size and restoring the Max Heap property using `MaxHeapify`.

This process ensures that the largest elements are moved to the end of the list in each iteration, resulting in a sorted array.

## **Functions Used**

### `MaxHeapify(A, n, i)`

Maintains the **Max Heap property** for a subtree rooted at index `i` in the list `A` of length `n`.

### `HeapSort(A)`

Performs Heap Sort by building a Max Heap and then sorting the list `A` in-place.

## **Visual Explanation of Heap Sort**

The image below illustrates how Heap Sort works: the input array is visualized as a binary tree, and the Max Heap property is maintained throughout the sorting process.

![Heap Sort Step-by-Step](../img/references/HeapSort.png)

*Image source: Cormen, Thomas H., et al. “Introduction to Algorithms.” 3rd ed., MIT Press, 2009.*

**Example:**
```python
A = [2, 4, 1, 7, 9]
HeapSort(A)
print(A)
# Output: [1, 2, 4, 7, 9]
```

## **Time Complexity**

- **Best case:** $O(n \lg n)$
- **Worst case:** $O(n \lg n)$
- **Average case:** $O(n \lg n)$

where $\lg n$ means $\log_2 n$

---

© 2025 Byron Velasco

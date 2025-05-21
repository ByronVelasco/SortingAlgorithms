# **Heap Sort**

Heap Sort is a comparison-based sorting technique based on a Binary Heap data structure. It works by:

1. Building a **Max Heap** from the input list.
2. Repeatedly swapping the first element (maximum) with the last unsorted element.
3. Reducing the heap size and restoring the Max Heap property using the Max Heap property.

This process ensures that the largest elements are moved to the end of the list in each iteration, resulting in a sorted array.

## **Visual Explanation of Heap Sort**

The image below illustrates how Heap Sort works: the input array is visualized as a binary tree, and the Max Heap property is maintained throughout the sorting process.

![Heap Sort Step-by-Step](../img/references/HeapSort.png)

*Image source: Cormen, Thomas H., et al. “Introduction to Algorithms.” 3rd ed., MIT Press, 2009.*

## **Key Functions**

### `max_heapify(A, n, i)`

Maintains the **Max Heap property** for a subtree rooted at index `i` in the list `A` of length `n`.

### `heap_sort(A)`

Sorts the list `A` in ascending order by first building a Max Heap and then repeatedly extracting the maximum element, modifying `A` in-place.

**Example:**
```python
A = [2, 4, 1, 7, 9]
heap_sort(A)
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
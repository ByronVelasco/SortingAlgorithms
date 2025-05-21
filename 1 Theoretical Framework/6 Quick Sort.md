# **Quick Sort**

Quick Sort is a highly efficient, divide-and-conquer sorting algorithm. It works by selecting a **pivot** element and partitioning the array such that:

- All elements less than or equal to the pivot are placed on its left.
- All elements greater than the pivot are placed on its right.

This process is recursively applied to the left and right subarrays until the entire list is sorted.

## **Visual Explanation of Quick Sort**

The image below shows how Quick Sort partitions the array around the pivot and gradually sorts it using recursive calls.

![Quick Sort Step-by-Step](../img/references/QuickSort.png)

*Image source: [Latte & Code – Algoritmos de ordenación: QuickSort en JavaScript](https://latteandcode.medium.com/algoritmos-de-ordenaci%C3%B3n-quicksort-en-javascript-f064db39e6ad)*

## **Key functions**

### `partition(A, p, r)`

- The argument `p` is the index of the first element of the subarray to be partitioned.
- Takes the **last element** `A[r]` as pivot.
- Reorganizes the list so that the pivot is in its **correct final position**.
- Returns the index of the pivot.

### `quick_sort(A, p=0, r=None)`

Recursively sorts the sublist of `A` from index `p` to `r` in-place by partitioning around a pivot element. By default, sorts the entire list.

**Example:**
```python
A = [2, 8, 7, 1, 3]
quick_sort(A)
print(A)
# Output: [1, 2, 3, 7, 8]
```

## **Time Complexity**

- **Best case:** $O(n \lg n)$
- **Worst case:** $O(n^2)$
- **Average case:** $O(n \lg n)$

  where $\lg n$ means $\log_2 n$.

---

© 2025 Byron Velasco
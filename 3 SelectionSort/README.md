# SelectionSort

This module contains the file `SelectionSort.ipynb`, which implements the Selection Sort algorithm.

## Selection Sort Algorithm

The Selection Sort algorithm divides the list into two parts — a sorted and an unsorted part. It repeatedly selects the smallest element from the unsorted part and moves it to the end of the sorted part.

- It starts with the first element and searches the entire list to find the smallest value.

- That smallest value is then swapped with the first element.

- This process is repeated for the remaining unsorted part of the list.

- Eventually, the entire list is sorted.

## Function: `SelectionSort(A)`

Sorts (ascending) a list `A`. Changes the entire list `A` in-place.

**Example:**
```python
A = [64, 25, 12, 22, 11]
SelectionSort(A)
print(A)
# Output: [11, 12, 22, 25, 64]
```

## Visual Explanation of Selection Sort

The image below illustrates how Selection Sort repeatedly selects the smallest element from the unsorted portion of the list and places it in its correct position by swapping it with the first unsorted element.

![Selection Sort Step-by-Step](../img/references/SelectionSort.png)

*Image source: [w3resource – Selection Sort Algorithm](https://www.w3resource.com/php-exercises/searching-and-sorting-algorithm/searching-and-sorting-algorithm-exercise-4.php)*

## Time Complexity

- **Best case:** $O(n^2)$
- **Worst case:** $O(n^2)$
- **Average case:** $O(n^2)$

---

© 2025 Byron Velasco

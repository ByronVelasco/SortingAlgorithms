# BubbleSort

This module contains the file `BubbleSort.ipynb`, which implements the Bubble Sort algorithm.

## Bubble Sort Algorithm

The Bubble Sort algorithm is named after the way bubbles rise to the top of a liquid — the largest values "bubble up" to the end of the list during each pass through the data.

- In each pass, adjacent bubbles (numbers) are compared.

- If a lower bubble is heavier (larger) than the one above it, they swap places, and the heavier one rises.

- This continues until the heaviest bubble reaches the top, i.e., the end of the list.

- The process repeats for the remaining bubbles until the entire list is sorted.

## Function: `BubbleSort(A)`

Sorts (ascending) a list `A`. Changes the entire list `A` in-place.

**Example:**
```python
A = [2, 6, 9, 5, 8]
BubbleSort(A)
print(A)
# Output: [2, 5, 6, 8, 9]
```

## Visual Explanation of Bubble Sort

The image below illustrates how Bubble Sort repeatedly compares and swaps adjacent elements, causing larger values to “bubble up” toward the end of the list.
Through multiple passes, unsorted values shift into their correct positions, gradually producing a fully sorted sequence.

![Merge Sort Visualization](../img/references/BubbleSort.png)

*Image source: [FavTutor – Bubble Sort in Python](https://favtutor.com/blogs/bubble-sort-python)* 

## Time Complexity

- **Best case:** $O(n^2)$
- **Worst case:** $O(n^2)$
- **Average case:** $O(n^2)$

---

© 2025 Byron Velasco
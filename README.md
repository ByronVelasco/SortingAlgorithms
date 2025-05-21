# **Complexity of Sorting Algorithms**

## **Summary**

This project presents an experimental study of the time complexity of fundamental sorting algorithms. Through systematic implementation, testing, and analysis, we empirically validated their theoretical performance and compared their execution times across various input scenarios. The goal is to bridge the gap between theoretical analysis and practical behavior using structured testing and visualization.

## **Objectives**

- Experimentally demonstrate the time complexity of common sorting algorithms.
- Compare the execution speed of each algorithm under different input conditions.

## **Conclusions**

Through comprehensive experimentation and analysis, we have compared the performance of several classic sorting algorithms—Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Heap Sort, and Quick Sort—across three different input scenarios: random, sorted, and reverse sorted lists.

Our results show that **Merge Sort and Heap Sort consistently maintained their performance and were the fastest algorithms in all three scenarios**, regardless of the initial order of the data. This robustness makes them highly reliable choices for practical applications.

However, in real-world situations, data is typically unordered, making **random lists the most common scenario**. In this context, **Quick Sort and Merge Sort emerged as the fastest algorithms on average**. Quick Sort, in particular, demonstrated superior average-case performance, making it a popular choice in many standard libraries and applications.

It is important to note, though, that **Quick Sort's performance can degrade significantly in its worst-case scenarios** (such as already sorted or reverse sorted lists). Addressing these worst cases requires algorithmic improvements, which will be explored in a future project.

In summary, while Merge Sort and Heap Sort offer consistent speed across all scenarios, Quick Sort stands out for its average-case efficiency on random data, provided its worst-case behavior is properly managed.

## **Project Structure**

The repository is organized into the following components:

- **`1 Theoretical Framework` Folder**:   
  This folder contains the theoretical framework and explanations for each sorting algorithm included in this project.

- **`2 Algorithm Design and Experimentation` Folder**:  
  This folder contains the implementation of algorithms `bubble_sort`, `insertion_sort`, `selection_sort`, `merge_sort`, `heap_sort` and `quick_sort` and their performance comparison with each other. It includes an experiment measuring and analyzing their execution times.

- **`img/` Folder**:  
  Stores the referenced diagrams (in the `references`/ subfolder) used to illustrate each algorithm, as well as the output images generated during experimentation.

- **`project_functions.py` Python Script**:   
  This Python script includes all the sorting algorithms developed specifically for this project.

- **`requirements.txt` Text File**:   
This file lists all the dependencies required to run the project.

## **Final Note**

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

## **Reference**

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

## **License**

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

---

© 2025 Byron Velasco
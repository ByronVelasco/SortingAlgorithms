# Complexity of Sorting Algorithms

## Summary

This project presents an experimental study of the time complexity of fundamental sorting algorithms. Through systematic implementation, testing, and analysis, we empirically validated their theoretical performance and compared their execution times across various input scenarios. The goal is to bridge the gap between theoretical analysis and practical behavior using structured testing and visualization.

## Objectives

- Experimentally demonstrate the time complexity of common sorting algorithms.
- Compare the execution speed of each algorithm under different input conditions.

## Conclusions

In this study, we experimentally validated the theoretical time complexities of various sorting algorithms. We also compared their performance across different input scenarios. Since data in real-world applications is typically unordered, the average-case performance is often the most relevant. Under these conditions, **QuickSort** and **MergeSort** consistently emerged as the fastest algorithms, achieving an average execution time of approximately **0.02 seconds** for lists containing **10,000 elements**.

On the other hand, **BubbleSort**, **InsertionSort**, and **SelectionSort** demonstrated significantly slower runtimes in all test cases, aligning with their known quadratic time complexity. **HeapSort**, while slightly slower than QuickSort and MergeSort, still maintained excellent average performance and is widely appreciated not only as a sorting algorithm but also as a foundational data structure for implementing efficient priority queues—an aspect we plan to explore further in future work.

## Project Structure

The repository is organized into the following components:

- **Individual Algorithm Folders**:  
  Each sorting algorithm (e.g., BubbleSort, InsertionSort, MergeSort, etc.) is placed in its own folder. Every folder contains the implementation and a detailed explanation in its corresponding `README.md`.

- **`Tests/` Folder**:  
  Contains test scripts that evaluate the correctness and behavior of each sorting algorithm.

- **`ListsMaker/` Folder**:  
  Contains functions that generate input lists:
  - Random lists
  - Ascending sorted lists
  - Descending sorted lists

- **`img/` Folder**:  
  Stores the cited diagrams used to explain each algorithm and the output images generated during experimentation.  
  Note: Some experimental plots may be missing from this folder, as saving images directly from the script resulted in overwriting files. However, all plots are also displayed inline within the script `ComplexityMachine.ipynb`.

- **`7 ComplexityMachine/` Folder**:  
  Contains the notebook `ComplexityMachine.ipynb`, which performs the experimental analysis of sorting algorithms and presents the conclusions.

## How to Run This Project

1. **Clone the repository**  
   Open a terminal and run:

   ```bash
   git clone https://github.com/ByronVelasco/Complexity-of-Sorting-Algorithms.git
   cd Complexity-of-Sorting-Algorithms

2. **Install the required libraries**
   
   Make sure you have Python installed (preferably 3.8+), then install the dependencies:
   
   ```bash
   pip install -r requirements.txt

3. **Open the main notebook**
   
   Use your preferred Python environment (like Jupyter, VS Code, or Google Colab) and open:

   ```
   7 ComplexityMachine/ComplexityMachine.ipynb

4. **Run** the cells to perform the experiments and generate the visualizations.

   The results will be displayed directly in the notebook, and the corresponding graphs will be saved in the `img/` folder.

## Final Note

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

## Reference

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

## License

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

© 2025 Byron Velasco
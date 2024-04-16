# Sorting Algorithms Time Complexity



### Bubble Sort:

Description: Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
Time Complexity:
Best Case: O(n) - when the list is already sorted.
Average Case: O(n^2).
Worst Case: O(n^2) - when the list is sorted in reverse order.
<br>
### Selection Sort:

Description: Selection Sort divides the input list into two parts: the sorted sublist and the unsorted sublist. It repeatedly finds the minimum element from the unsorted sublist and swaps it with the first element of the unsorted sublist.
Time Complexity:
Best Case: O(n^2).
Average Case: O(n^2).
Worst Case: O(n^2).
<br>
### Insertion Sort:

Description: Insertion Sort builds the final sorted array one item at a time. It iterates through the list, taking one element at a time and inserting it into its correct position in the already sorted part of the list.
Time Complexity:
Best Case: O(n) - when the list is already sorted.
Average Case: O(n^2).
Worst Case: O(n^2).
<br>
### Merge Sort:

Description: Merge Sort is a divide and conquer algorithm that divides the input array into two halves, sorts each half independently, and then merges them back together.
Time Complexity:
Best Case: O(n log n).
Average Case: O(n log n).
Worst Case: O(n log n).
<br>
### Quick Sort:

Description: Quick Sort also uses a divide and conquer approach. It picks an element as a pivot and partitions the given array around the pivot. It then recursively sorts the sub-arrays.
Time Complexity:
Best Case: O(n log n).
Average Case: O(n log n).
Worst Case: O(n^2) - when the pivot is consistently the smallest or largest element.
<br>
### Shell Sort:

Description: Shell Sort is an extension of insertion sort. It sorts the elements by comparing distant elements first and then progressively reducing the gap between elements to be compared.
Time Complexity:
Best Case: O(n log n).
Average Case: Depends on the gap sequence used.
Worst Case: O(n(log n)^2).

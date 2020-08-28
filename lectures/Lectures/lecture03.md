---
author:
- Mark Fontenot, PhD
subtitle: Data Structures
title: CS 2341:Fall 2020:Lecture 03
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---

## Reminders

- Homework 1 Due next Wednesday
    - 1 error (question 2) and 1 typo (question 3) were updated.  Check them out. 
    - **Any HW Questions???**
- Labs start next week. 

## Last Class

- Reviewed 
    - pointers
    - relationship between pointer offset notation (`*(arr + 1)`) and subscript notation (`arr[1]`).
    - pointers to pointers 
- Started learning about memory diagramming

## Today

- c-strings
- `new` and `delete` review
- Dangling Pointers & Memory Leaks
- What's a segmentation fault?
- Memory management in Classes: Rule of 3

## c-strings

## `new` and `delete`

- if `new`, then `delete`
- if `new[]`, then `delete[]`

- **Don't mix single version and array version**. 


## Dangling Pointers

- A **dangling pointer** is a pointer that points to memory that is no longer valid.  
    - the memory has been released through some other pointer

```{.cpp}
int* x = new int[5];
int* y = x;
delete[] y;
```



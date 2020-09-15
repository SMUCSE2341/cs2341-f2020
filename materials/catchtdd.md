---
author:
- Mark Fontenot, PhD
subtitle: Data Structures
title: CS 2341:Fall 2020:Catch & TDD
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---

# TDD

## What is it?

- write tests before 

## Example

# Catch2

## What is it? 

- "Catch2 is a multi-paradigm test framework for C++" (from GitHub page)
- Can be used as a **single header include**
  - you only need to add 1 file to your project to get access to the features of Catch2. 

# Phil Nash - Modern C++ with Catch2 on Youtube

## Example 1

- move catch.hpp into the project (single-header-include)

```cpp
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
```

- Can also run from terminal 
  - `./CatchTest4 -?`

## Example 2

- make a new file

```cpp
TEST_CASE() {
    REQUIRE(6*9 == 42);
}
```
- Clion catch2 runner in config options
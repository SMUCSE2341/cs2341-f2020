---
title: Valgrind 
has_children: false
parent: Lectures
nav_order: 2
---

# Valgrind on the Lyle Linux Servers

## Connecting to the Lyle Servers

### For Windows Folks

- Download [PuTTY](https://www.putty.org/) 
- Install PuTTY
- Execute PuTTY
- In the Connect dialog, use `genuse50.lyle.smu.edu` as the host name.  Make sure the `SSH` radio button is selected below the hostname field. 

### For Mac Folks

- Open a Terminal
- type `ssh <username>@genuse50.lyle.smu.edu` where `<username>` is replaced with whatever comes before the @ sign in your SMU Email address. 
- Use your regular SMU password (whatever you use for my.smu or webmail). 


## Clone the Repo of Interest

- Log into github and get the URI to the repo you want to test with Valgrind.
- Once logged in to the Lyle servers, clone that repo using `git clone <URI>` where `<URI>` is the repo link you get from github. 
- Use `cd` to change into the project directory. 
- Create a build folder for your project, run cmake, then make. 
  - `mkdir build`
  - `cd build`
  - `cmake3 ..`
  - `make`
- Once the project successfully builds, run Valgrind with the executable.  
  - Example: `valgrind ./my_project_executable` 
  - Of course, substitute the name of your executable for `my_project_executable`. 

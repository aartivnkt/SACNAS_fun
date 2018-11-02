Get ready for some SACNAS fun!

Goal:
    We added some simple code examples to introduce you to the structure of writing corporate-style software, together with
    some very basic unit testing. This exercise is in python. Coding in python is preferable, although R is fine too.

Exercise 1:
    In simple_example directory, there is a 1-line 1000G_example.csv input_file.
    Write a simple script that reads this input file into a dictionary, and append a 'mean_allele_frequency' dictionary key with
    the calculated mean allele frequency across populations as the value. Make sure the calculation of the mean_allele_frequency
    happens in a separate function.
    The goal of this exercise is to test important programming abilities (argument parsing, docstrings, following PEP8 standards,
    strong-typing the input args and so on).


    ** For teams that complete this exercise quickly, test the following additional exercises **:
    - Raise an error if the input file is not found
    - Raise a custom error if the allele frequency value is an incorrect datatype

Exercise 2:
    Unit test the bit of code that calculates mean_allele_frequency. Use python's inbuilt unittest module for this.

For students that write code in R, unit testing in R is also possible.

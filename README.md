Get ready for some SACNAS fun!

I added some very simple code examples that will introduce students to the structure of writing corporate-style software, together with
some very basic unit testing. This exercise is in python. Coding in python is preferable, although R is fine too.

Here is the structure of some examples I included, and the code that goes with it:

In simple_example directory, there is a 1-line 1000G_example.csv input_file.
The first exercise is to write a simple script that reads this input file into a dictionary, and creates a 'mean_allele_frequency'
field, with the calculated mean allele frequency. The goal of this exercise is to go over some basic code structure and style that
tests some important programming abilities (argument parsing, docstrings, following PEP8 standards, strong-typing the input args
and so on). I added a parse_1000G.py file that is a pythonic version of this exercise. Students will be required to write a
separate piece of code that calculates the mean_allele_frequency for the purpose of unit testing (see below).

Once the first exercise is completed, students will then unit test their bit of code that calculates mean_allele_frequency.

In tests/unit, I added a test_parse_1000G.py file that unit tests the 'cal_mean_allele_frequency' function in the parse_1000G.py code.
This is a very basic example, that hopefully introduces students to the idea of unit testing and its purpose.

For students that write code in R, unit testing in R is also possible.




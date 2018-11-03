#!/usr/bin/env RScript

if (!require("testthat")) { install.packages("testthat", dependencies = TRUE,repos = "http://cran.us.r-project.org") ; require("testthat") }

source("1000G_example.R")
test_file="1000G_example.test.csv"

test_that("cal_mean_allele_frequency",{
           expected= 0.612
           test_filename=read.csv(test_file)
           testing=cal_mean_allele_frequency(to_be_tested)
           expect_equal(testing, expected)
})

import os
import gc
import numpy
import pandas


import analysis

df = pandas.read_csv("test_data.csv")

a = analysis.Analysis() \
            .from_df(df) \
            .select_shape() \
            .select_mean("age") \
            .select_max("age") \
            .select_min("age") \
            .select_sum("age") \
            .run()

print(a)
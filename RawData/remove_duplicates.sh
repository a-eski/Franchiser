#!/bin/env bash

grep -Fvxf franchises_1.txt franchises_index_1.txt > franchises_index_1_filtered_1.txt
grep -Fvxf franchises_2.txt franchises_index_1_filtered_1.txt > franchises_index_1_filtered_2.txt
grep -Fvxf franchises_3.txt franchises_index_1_filtered_2.txt > franchises_index_1_filtered_3.txt
grep -Fvxf franchises_4.txt franchises_index_1_filtered_3.txt > franchises_index_1_filtered.txt
rm franchises_index_1_filtered_1.txt franchises_index_1_filtered_2.txt franchises_index_1_filtered_3.txt

grep -Fvxf franchises_1.txt franchises_index_2.txt > franchises_index_2_filtered_1.txt
grep -Fvxf franchises_2.txt franchises_index_2_filtered_1.txt > franchises_index_2_filtered_2.txt
grep -Fvxf franchises_3.txt franchises_index_2_filtered_2.txt > franchises_index_2_filtered_3.txt
grep -Fvxf franchises_4.txt franchises_index_2_filtered_3.txt > franchises_index_2_filtered.txt
rm franchises_index_2_filtered_1.txt franchises_index_2_filtered_2.txt franchises_index_2_filtered_3.txt

grep -Fvxf franchises_1.txt franchises_index_3.txt > franchises_index_3_filtered_1.txt
grep -Fvxf franchises_2.txt franchises_index_3_filtered_1.txt > franchises_index_3_filtered_2.txt
grep -Fvxf franchises_3.txt franchises_index_3_filtered_2.txt > franchises_index_3_filtered_3.txt
grep -Fvxf franchises_4.txt franchises_index_3_filtered_3.txt > franchises_index_3_filtered.txt
rm franchises_index_3_filtered_1.txt franchises_index_3_filtered_2.txt franchises_index_3_filtered_3.txt

grep -Fvxf franchises_1.txt franchises_index_4.txt > franchises_index_4_filtered_1.txt
grep -Fvxf franchises_2.txt franchises_index_4_filtered_1.txt > franchises_index_4_filtered_2.txt
grep -Fvxf franchises_3.txt franchises_index_4_filtered_2.txt > franchises_index_4_filtered_3.txt
grep -Fvxf franchises_4.txt franchises_index_4_filtered_3.txt > franchises_index_4_filtered.txt
rm franchises_index_4_filtered_1.txt franchises_index_4_filtered_2.txt franchises_index_4_filtered_3.txt

grep -Fvxf franchises_1.txt franchises_index_5.txt > franchises_index_5_filtered_1.txt
grep -Fvxf franchises_2.txt franchises_index_5_filtered_1.txt > franchises_index_5_filtered_2.txt
grep -Fvxf franchises_3.txt franchises_index_5_filtered_2.txt > franchises_index_5_filtered_3.txt
grep -Fvxf franchises_4.txt franchises_index_5_filtered_3.txt > franchises_index_5_filtered.txt
rm franchises_index_5_filtered_1.txt franchises_index_5_filtered_2.txt franchises_index_5_filtered_3.txt

grep -Fvxf franchises_1.txt franchises_index_6.txt > franchises_index_6_filtered_1.txt
grep -Fvxf franchises_2.txt franchises_index_6_filtered_1.txt > franchises_index_6_filtered_2.txt
grep -Fvxf franchises_3.txt franchises_index_6_filtered_2.txt > franchises_index_6_filtered_3.txt
grep -Fvxf franchises_4.txt franchises_index_6_filtered_3.txt > franchises_index_6_filtered.txt
rm franchises_index_6_filtered_1.txt franchises_index_6_filtered_2.txt franchises_index_6_filtered_3.txt

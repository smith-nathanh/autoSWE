#!/bin/bash

python ../src/query_arxiv.py \
--category cs.CL \
--title neural \
--author Smith \
--abstract learning \
--recent_days 7 \
--to_file example_query_results.csv \
--verbose

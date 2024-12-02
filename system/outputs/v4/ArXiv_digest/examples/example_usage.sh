#!/bin/bash

# Example usage of the Query ArXiv tool

python query_arxiv.py \
--category cs.CL \
--title neural \
--author Smith \
--abstract learning \
--recent_days 30 \
--to_file results.csv \
--verbose

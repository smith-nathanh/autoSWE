#!/bin/bash

# Example usage of the Query ArXiv tool
python query_arxiv.py \
--category cs.CL \
--author Smith \
--title neural \
--abstract learning \
--recent_days 30 \
--to_file examples/example_query_results.csv \
--verbose
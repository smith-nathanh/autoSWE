#!/bin/bash

python ../src/main.py \
  --learning_rate 0.01 \
  --num_epochs 10 \
  --batch_size 16 \
  --embedding_dim 300 \
  --kernel_sizes 3 4 5 \
  --max_length 50 \
  --save_every_n_epoch 2 \
  --train \
  --gpu \
  --output_dir '../outputs' \
  --train_log_per_k_batch 20 \
  --random_seed 20

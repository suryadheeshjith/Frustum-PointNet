#/bin/bash
python train/train.py --gpu 0 --log_dir train/log_v3 --num_point 1024 --max_epoch 51 --batch_size 32 --decay_step 800000 --decay_rate 0.5 --loss quantile

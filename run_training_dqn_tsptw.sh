#!/bin/bash

# Seed for the random generation: ensure that the validation set remains the same.
seed=1

# Characterics of the training instances
n_city=10

# Parameters for the training
batch_size=16 # max batch size for training/testing
hidden_layer=4 # number of hidden layer
latent_dim=128
learning_rate=0.0001
n_step=-1
max_softmax_beta=10

# Others
plot_training=1 # Boolean value: plot the training curve or not
mode=cpu

# Folder to save the trained model
network_arch=hidden_layer-$hidden_layer-latent_dim-$latent_dim/
result_root=trained_models/dqn/tsptw/n-city-$n_city/seed-$seed/$network_arch
save_dir=$result_root/batch_size-$batch_size-learning_rate-$learning_rate-n_step-$n_step-max_softmax_beta-$max_softmax_beta


if [ ! -e $save_dir ];
then
    mkdir -p $save_dir
fi

python main_training_dqn_tsptw.py \
    --seed $seed  \
    --n_city $n_city  \
    --batch_size $batch_size  \
    --hidden_layer $hidden_layer  \
    --latent_dim $latent_dim  \
    --max_softmax_beta $max_softmax_beta \
    --learning_rate $learning_rate \
    --save_dir $save_dir  \
    --plot_training $plot_training  \
    --mode $mode \
    --n_step $n_step \
    2>&1 | tee $save_dir/log-training.txt



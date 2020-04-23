
import sys
import os
import argparse

from src.problem.tsptw.learning.trainer_dqn import TrainerDQN

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def parse_arguments():
    parser = argparse.ArgumentParser()

    # Instances parameters
    parser.add_argument('--n_city', type=int, default=20)
    parser.add_argument('--mode', default='cpu', help='cpu/gpu')
    parser.add_argument('--seed', type=int, default=1)

    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--learning_rate', type=float, default=0.0001)
    parser.add_argument('--n_step', type=int, default=-1)
    parser.add_argument('--max_softmax_beta', type=int, default=10, help="max_softmax_beta")

    parser.add_argument('--hidden_layer', type=int, default=32)
    parser.add_argument('--latent_dim', type=int, default=128, help='dimension of latent layers')

    parser.add_argument('--L2_penalty', type=int, default=0)
    parser.add_argument('--dropout', type=int, default=0)

    # Argument for Trainer
    parser.add_argument('--n_episode', type=int, default=1000000)
    parser.add_argument('--save_dir', type=str, default='./result-default')
    parser.add_argument('--plot_training', type=int, default=1)


    return parser.parse_args()


if __name__ == '__main__':

    args = parse_arguments()

    print("***********************************************************")
    print("[INFO] TRAINING ON RANDOM INSTANCES: TSPTW")
    print("[INFO] n_cities: %d" % args.n_city)
    print("***********************************************************")
    print("[INFO] TRAINING PARAMETERS")
    print("[INFO] algorithm: DQN")
    print("[INFO] batch_size: %d" % args.batch_size)
    print("[INFO] learning_rate: %f" % args.learning_rate)
    print("[INFO] hidden_layer: %d" % args.hidden_layer)
    print("[INFO] latent_dim: %d" % args.latent_dim)
    print("[INFO] softmax_beta: %d" % args.max_softmax_beta)
    print("[INFO] n_step: %d" % args.n_step)
    print("***********************************************************")
    sys.stdout.flush()

    trainer = TrainerDQN(args)
    trainer.run_training()

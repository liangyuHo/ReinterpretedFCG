import argparse


def parameter_parser():
    parser = argparse.ArgumentParser(description="Run Graph2Vec.")

    parser.add_argument('--input-path',
                        nargs='?',
                        default='./bin/006b4ca023bf1f3139b1e8d30ee09f2abc6079657b77ea401a9a3c0ed1af42c2',
                        help='input binary file.')

    parser.add_argument('--model',
                        nargs='?',
                        default='mlp',
                        help='Select the model(rf, knn, svm, mlp).')
    
    parser.add_argument("--output-path",
                        nargs="?",
                        default="./feature/feature.csv",
	                help="Embeddings path.")
    parser.add_argument("--dimensions",
                        type=int,
                        default=128,
	                help="Number of dimensions. Default is 128.")

    parser.add_argument("--workers",
                        type=int,
                        default=4,
	                help="Number of workers. Default is 4.")

    parser.add_argument("--epochs",
                        type=int,
                        default=50,
	                help="Number of epochs. Default is 10.")

    parser.add_argument("--min-count",
                        type=int,
                        default=0,
	                help="Minimal structural feature count. Default is 5.")

    parser.add_argument("--wl-iterations",
                        type=int,
                        default=2,
	                help="Number of Weisfeiler-Lehman iterations. Default is 2.")

    parser.add_argument("--learning-rate",
                        type=float,
                        default=0.025,
	                help="Initial learning rate. Default is 0.025.")

    parser.add_argument("--down-sampling",
                        type=float,
                        default=0.0001,
	                help="Down sampling rate of features. Default is 0.0001.")

    parser.add_argument("--judge",
                    type=int,
                    default=0,
                help="Rename?")


    return parser.parse_args()

"""Parameter parser to set the model hyperparameters."""

import argparse
import os

def parameter_parser():
    """
    A method to parse up command line parameters.
    By default it gives an embedding of the partial NCI1 graph dataset.
    The default hyperparameters give a good quality representation without grid search.
    Representations are sorted by ID.
    """
    parser = argparse.ArgumentParser(description="Run Graph2Vec.")

    parser.add_argument("--input-path","-i",
                        nargs="?",
                        default="./dataset/",
	                help="Input folder with jsons.")

    parser.add_argument("--output-path","-o",
                        nargs="?",
                        default="./features/nci1.csv",
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
                        default=1,
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

    parser.add_argument('--model','-m',
                        nargs='?',
                        default='SVM',
                        help='Select the model(KNN,LR,MLP,RF,SVM).')
    parser.add_argument('-c', '--classify', action='store_true',
                        help='apply the family classifier')
    return parser.parse_args()



def write_output(input_path,output_path,result,labels):
    '''
    param.
        input_path: path to the input binary file
        output_path: path to the csv file
        result: a list(float), probability of each class, e.g. [0.92, 0.08]
        labels: a list(str), each class, e.g. ['Benignware', 'Malware']
    description.
        write a csv file for saving the result of prediction
            e.g.
                Filename, Benign, Malware
                34eff01a, 0.98, 0.02
                f01a34ef, 0.17, 0.83
                ff001aff, -1
            or e.g.
                Filename, Benign, Mirai, Unknown, Android
                34eff01a, 0.01, 0.02, 0.95, 0.02
                f01a34ef, 0.73, 0, 0.22, 0.05
                ff001aff, -1
    '''

    if '.csv' not in output_path:
        output_path += '.csv'

    # init the columns of this table if it is a new csv file
    if not os.path.exists(output_path):
        with open(output_path,'w') as f:
            line = 'Filename, '
            line += ', '.join(labels)
            line += '\n'
            f.write(line)

    # write the result 
    with open(output_path,'a+') as f:
        line = os.path.basename(input_path) + ', '
        line += ','.join(list(str(i) for i in result))
        line += '\n'
        f.write(line)

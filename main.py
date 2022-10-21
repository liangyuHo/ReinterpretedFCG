import r2pipe, os, sys, time, csv
from param_parser import parameter_parser
import AnalysisUserDefined
import CreateRenameGraph
import pandas as pd
import numpy as np

def bin2Fcg(fname):
    r2 = r2pipe.open(fname)
    try:
        r2.cmd('aaaa')
    except Exception:
        print('time out')
        pid = os.popen("ps aux | grep " + fname+ " | grep -v grep | awk '{print $2}'")
        for i in pid:
            os.popen("kill -9 " + i.strip('\n'))
            continue
        return
    G = r2.cmd('agCd')
    return G




def main(args):
    # convert binary file to fcg
    fcg_Dot = bin2Fcg(args.input_path)
    
    # use radare2 to analysis the binary file
    # to detect is there any user_defined_function in the binary file?
    # we store the result in DetectionUserDefined/ as numpy file
    AnalysisUserDefined.radare2_analysis(args.input_path)
    
    # we find is there any dupes file(function)
    cmd = 'fdupes -r ./DetectionUserDefined/ > ./fdupes.txt'
    os.system(cmd)
    
    # we relabel the dupes file(function)'s name
    # and we build the new fcg graph
    CreateRenameGraph.Re_create(fcg_Dot)
    
    # we use graph2vec+.py to convert the fcg to vector
    # store the vector  as csv file
    cmd = 'python graph2vec+.py --input-path ./ --output-path ./test.csv'

    os.system(cmd)

    # read test.csv and turn the vector to numpy
    feature = []
    try:
        data = pd.read_csv('./test.csv',header=None)
    except:
        with open('redefine_fcg.dot','w') as f:
            f.write(fcg_Dot)
        cmd = 'python graph2vec.py --input-path ./ --output-path ./test.csv'
        os.system(cmd)

        data = pd.read_csv('./test.csv',header=None)


    print(data.shape[0])
    for i in range(data.shape[0]):
        tmp = data.iloc[i,1:132].values.tolist()
        feature.append(tmp)
    feature = np.array(feature)
    print(feature)
    np.save('./feature/feature',feature)

    # delete the redundant file
    cmd = 'rm -rf test.csv redefine_fcg.dot fdupes.txt ./DetectionUserDefined/ '
    os.system(cmd)

if __name__=='__main__':
    args = parameter_parser()
    main(args)

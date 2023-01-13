import r2pipe, os, sys, time, csv
from utils import parameter_parser
from utils import write_output
#import AnalysisUserDefined
#import CreateRenameGraph
import pandas as pd
import numpy as np
import subprocess
import pickle,sklearn


def main(args):

    ### extract feature ###
    subprocess.call(['mkdir ./Redefine/ ./cfg_output/ ./DetectionUserDefined/'],shell=True)
    exec(open("./CG_extract.py").read(),{'args':args})
    exec(open("./AnalysisUserDefined.py").read())
    subprocess.call(['fdupes -r ./DetectionUserDefined/ > ./fdupes.txt'],shell=True)
    subprocess.call(['python CreateRenameGraph.py'],shell=True)
    exec(open("./graph2vec+.py").read(),{'args':args})
    feature=[]
    data = pd.read_csv('./test.csv',header=None)
    for i in range(data.shape[0]):
        tmp = data.iloc[i,1:132].values.tolist()
        feature.append(tmp)
    
    ### convert feature to numpy ###
    feature = np.array(feature)
    np.save('./feature/feature',feature)
    
    ### delete the relative file ###
    subprocess.call(['rm -rf ./Redefine/ fdupes.txt ./DetectionUserDefined/  tmp.csv test.csv ./cfg_output/'],shell=True)
    
    ### select model and classifier ###
    model_type = args.model
    if args.classify:
        model = pickle.load(open('./model/Model_save/'+model_type+'_classifier.pkl','rb'))
        
    else:
        model = pickle.load(open('./model/Model_save/'+model_type+'.pkl','rb'))
    feature = np.load('./feature/feature.npy')

    ### create label ###
    labels = ['BenignWare','Malware']
    if args.classify:
        labels = ['Android' ,'Bashlite' ,'BenignWare', 'Dofloo', 'Hajime', 'Mirai', 'Tsunami', 'Unknown', 'Xorddos', 'Pnscan']

    ### predict the answer ###
    result = model.predict_proba(feature)
    
    ### write the csv ###
    write_output(args.input_path, args.output_path, result, labels)

    
args = parameter_parser()
main(args)



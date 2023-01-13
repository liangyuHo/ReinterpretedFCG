import networkx as nx
import json
import r2pipe, os, sys, time, csv
import numpy as np
import signal
from networkx.readwrite import json_graph
import os
import shutil
#import Filelist
import warnings
import csv
from utils import parameter_parser


def radare(fname,target,name):
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(30)
    r2 = r2pipe.open(fname)
    start = time.time()
    try:
        r2.cmd('aaaa')
    except Exception:
        print('time out ')
        pid = os.popen("ps aux | grep " + fname+ " | grep -v grep | awk '{print $2}'")
        for i in pid:
            os.popen("kill -9 " + i.strip('\n'))
            continue
        return
    cmd_of_save_dot='agCd >>'+target+'graph.dot'
    #cmd_of_save_dot='agCd >'+name+'.dot'
    r2.cmd(cmd_of_save_dot)
    end = time.time()
    return end-start
    
    #return call_graph_list

def signal_handler(signum, frame):
    raise Exception("Timed out!")


def main(args):
    sys.setrecursionlimit(100000000) 
    feature_vec = {}  
    filePath=''
    count = 0
         
    #print('Extracting CFG from', args.input_path)
    print('Extracting CFG from', filePath)
    f = args.input_path
             
            #if f in list:
            #    continue
                
    if count % 10000 == 0:
        print('extract %d files' % count)
    try:
        #file_dir = f[:2]
        call_graph_list = []
        fname = os.path.join(args.input_path)
        path = fname
                #path = fname.replace('/mnt/database0/', './call_graph_list/')
        
                       
        if not os.path.isfile(path + '.json'):
                    
            print(count, f)
            signal.signal(signal.SIGALRM, signal_handler)
            signal.alarm(60)
            
                      
            try:
                target='./cfg_output/'
                print(f)
                passtime = radare(f,target,f)
                
            except Exception:
                print("Timed out!ii")
                pid = os.popen("ps aux | grep " + fname+ " | grep -v grep | awk '{print $2}'")
                for i in pid:
                    os.popen("kill -9 " + i.strip('\n'))
                    continue
                print('success kill')
                        
                        
    except:
        print(f, 'error')
    
    
main(args)
if __name__=='__main__':
    args = parameter_parser()
    main(args)

# ReinterpretedFCG
## usage

* Use main.py extract the input file to feature
* And we store the feature(feature.npy) in ./feature/
```
  python main.py --input-path [FILE_PATH]
```

* And then use ./model/detector.py to detect the file
```
  python ./model/detector.py 
```
* benign:0  
* malware:1

## Description
* we use radare2 to extract fcg
* AnalysisUserDefined.py : extract opcode sequence of 'fcn.' (user-defined function)
* CreateRenameGraph.py : to build the relabel dict and to build a new fcg

## Feature Extraction
* we reverse the binary file to function call graph by r2pipe

## Requirements
* python3
* radare2
* sklearn
* pickle
* networkx


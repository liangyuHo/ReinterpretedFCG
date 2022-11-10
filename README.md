# ReinterpretedFCG

## usage
* Use main.py to extract the binary file to feature
* And we store the feature in ./feature/feature.npy

```
python main.py --input-path [FILE_PATH]
``` 
* For example
```
python main.py --input-path ./binary/040007e80925af67093e2245bab6a1030086417bd7e0cd6013f9cd2e4f979393
```

* And then we use ./model/detector.py to detect the feature
```
cd model/
python detector.py
```

* benign:0
* malware:1

## Description
* we use radare2 to extract fcg
* AnalysisUserDefined.py extract opcode sequence of 'fcn.'
* CreateRenameGraph.py : to build the relabel dict and to nuild a new fcg

# ReinterpretedFCG

## usage
* Use main.py to extract the binary file to feature
* And we store the feature in ./feature/feature.npy

```
python main.py -i [FILE_PATH] -o [output csv] -m [model (SVM、LR、KNN、RF、MLP)] -c(classifier or not)
``` 
* For example
```
### for detector
python main.py -i ./binary/040007e80925af67093e2245bab6a1030086417bd7e0cd6013f9cd2e4f979393 -o detector_result.csv -m RF

### for classifier
python main.py -i ./binary/040007e80925af67093e2245bab6a1030086417bd7e0cd6013f9cd2e4f979393 -o detector_result.csv -m RF -c
```
* label for detector
    * [benign,malware]
* label for classifier
    * [Android,Bashlite,BenignWare,Dofloo,Hajime,Mirai,Tsunami,Unknown,Xorddos,Pnscan]
## Description
* we use radare2 to extract fcg
* AnalysisUserDefined.py extract opcode sequence of 'fcn.'
* CreateRenameGraph.py : to build the relabel dict and to nuild a new fcg

# Accuracy
## malware detection

| Model | Accuracy |
| ----- | -------- |
| SVM   | 98.91    |
| RF    | 100      |
| KNN   | 97.78    |
| LR    | 95.88    |
| MLP   | 98.92    |

## family classification
| Model | Accuracy |
| ----- | -------- |
| SVM   | 96.53    |
| RF    | 98.56    |
| KNN   | 94.12    |
| LR    | 97.79    |
| MLP   | 86.94    |    

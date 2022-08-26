# Classification
Pasos del aprendizaje de máquina:
    1. alimentarlo
    2. Probarlo
## Introduction

### Teaching to read digits
(Process of classification)
1. Show a sample of written digits, one at a time (_Training Set_)
2. Shuffle the images and evaluate
3. Repet until the student gets most of them right
4. Try with other set (_Test set_)


**Class**: abstraction of elements of the same type

## Binary Classification
- Assign each example to a class
    1. It's the number one
    2. It is not the number one

#### Evaluation the (binary) classifier
- True positive
- False positive
- True negative
- False negative

|True label| One | Not a one|Accuracy|Error rate|
|-|-|-|-|-|
|One| 1,1 |1|2/3|1/3|
|Nor a one|7|6,5,5,2,4,9|1/7|6/7|

- Overall accuracy: 8/10
- Error rate: 2/10

We define in a binary classifier:  
- **Sensitivity**: $TP/TP+FN$, es el indicador para determinar la habilidad de el estudiante de reconocer la clase
- **Specificity**: $TN/TN+FP$, es el indicador para determinar la habilidad de el estudiante para reconocer que algo no es la clase  

## Multi-class classifier

En lugar de una tabla de verdad, tenemos una matriz de confunsión de clase (Class-Confusion Matrix)

### Trainign and testing
- Collect all the available examples and split them into :
    - Training set
    - Test set for evaluation
- 

### Cross-validation
- Iteratively
    - generate a new random split, or fold, of the training set and test set
    - teach with the training set
    - evaluate with the test set and record accuracy for current fold
- average accuracy over all the folds

### Leave one cut cross validation

A particular case of cross-validation with size as follows:
- Data set: N
- Training set in each fold: N-1
- Test set in each fold: 1

### k-Fold Cross-Validation
A particular case of cross-validation with size as follows:
- Data set: N
    - Split into k equal pieces at fixed places
    - $|N/K|N/K|...|N/K|$
    - Training set in each fold: $N-N/K$
    - Test set in each fold: $N/K$

Estos métodos sirven para entrenar y verificar mi modelo de manera iterativa con un solo conjunto de datos, de manera que sobre

## Classifiers
    - Input: data item
        - set of features in vector $X$
    - Output: label
        - $Y$
            - Binary
            - Multi-class

### Supervised training
    - Input: Training set: data itemas ($X$,$Y$)
    - Testing
        - Input: Test set: data itemas ($X$)
        - Evaluate perfomance on $Y$
### Classifier's goals
- Class-Confussion MAtriz
- Accuracy
- Error rate
- Specificity
- Sensitivity

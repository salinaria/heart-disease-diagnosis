# Heart Disease Diagnosis
The aim of this project is to diagnose heart disease based on a `fuzzy expert system`.
## Inputs
1. **Blood Pressure**
2. **Blood Sugar**
3. **Cholesterol**
4. **Heart Rate**
5. **ECG**
6. **Old Peak**
7. **Age**
- The `fuzzy` sets of these values are available [Here](https://github.com/salinaria/heart-disease-diagnosis/blob/main/fuzzy%20sets).

### Crisp Inputs
1. **Chest Pain**
1: Typical Angina, 2: Atypical Angina, 3: Non-Anginal Pain, 4: Asymptomatic

2. **Sex**
0: Male, 1: Female

3. **Exercise**
0: This person is not allowed to have sport activities. 1: This person is allowed to have sport activities
4. **Thallium**
3: Normal 6: Medium 7: High

## Steps
This project includes four steps:
1. [Fuzzification](https://github.com/salinaria/heart-disease-diagnosis/blob/main/fuzzification.py): Based on Inputs and Fuzzy Sets
2. [Inference](https://github.com/salinaria/heart-disease-diagnosis/blob/main/inference.py): Based on the [Rules](https://github.com/salinaria/heart-disease-diagnosis/blob/main/rules.fcl)
3. [Defuzzification](https://github.com/salinaria/heart-disease-diagnosis/blob/main/defuzzification.py): Based on [Diagram of Output Values](https://github.com/salinaria/heart-disease-diagnosis/blob/main/fuzzy%20sets/sickness.JPG) and This Formula of the Center of the Mass (`CoG`):

$$x^*=(\sum_{i=1}^{n} μ_C^― (x_i).x_i)/(\sum_{i=1}^{n} μ_C^― (x_i))$$

4. [Final Result](https://github.com/salinaria/heart-disease-diagnosis/blob/main/final_result.py)

## How to Run
### Install Requirements
    $ pip install -r requirements.txt
### Run
    $ python -m flask run
## An Example of Input and Result
![image](https://user-images.githubusercontent.com/72709191/196000393-6a60aad1-5ee6-4dc6-a423-c7b443770dfd.png)
![image](https://user-images.githubusercontent.com/72709191/196000274-0abac9f5-3517-4b63-a897-5c3019289170.png)

## Report
My report in Farsi is available [Here](https://github.com/salinaria/heart-disease-diagnosis/blob/main/CI_project2.pdf).


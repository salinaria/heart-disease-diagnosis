from inference import submit_rules, extract_rules
from fuzzification import INPUTS, OUTPUTS


def run(METRIC):
    for i in METRIC.keys():
        METRIC[i] = float(METRIC[i])
    inp = INPUTS
    out = OUTPUTS
    rules = extract_rules()
    submit_rules(rules, METRIC, inp, out)
    OUT = out['health']
    OUT.prepare_defuzzyfication()
    list_defuzzyfication = OUT.list_defuzzyfication
    numinator = 0
    denominator = 0
    for i in range(len(list_defuzzyfication)):
        numinator += list_defuzzyfication[i][0] * list_defuzzyfication[i][1]
        denominator += list_defuzzyfication[i][1]

    return numinator / denominator

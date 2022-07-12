def extract_rules():

    rules = []
    f = open('rules.fcl', 'r')
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace('(', '')
        lines[i] = lines[i].replace(')', '')
        lines[i] = lines[i].replace('THEN', '')
        lines[i] = lines[i].replace('IF', '')
        lines[i] = lines[i].replace(';', '')
        lines[i] = lines[i].replace('maximum_', '')
        lines[i] = lines[i].replace('cholesterol', 'cholestrol')
        lines[i] = lines[i].replace('thallium', 'thallium_scan')
        lines[i] = lines[i].replace('ECG', 'ecg')
        lines[i] = lines[i].split()[2:]
    if lines[-1] == '':
        del lines[-1]

    for i in range(len(lines)):

        # Simple rules
        if len(lines[i]) == 6:
            C, S = lines[i][0], lines[i][2]
            COUT, SOUT = lines[i][3], lines[i][5]
            rules.append({'rule': 'simple', 'cond': C, 'stat': S,
                         'cond_out': COUT, 'stat_out': SOUT})

        # AND or OR rules
        if len(lines[i]) == 10:
            if lines[i][3] == 'OR':
                C1, S1 = lines[i][0], lines[i][2]
                C2, S2 = lines[i][4], lines[i][6]
                COUT, SOUT = lines[i][7], lines[i][9]
                rules.append({'rule': 'or', 'cond1': C1, 'stat1': S1, 'cond2': C2,
                             'stat2': S2, 'cond_out': COUT, 'stat_out': SOUT})

            if lines[i][3] == 'AND':
                C1, S1 = lines[i][0], lines[i][2]
                C2, S2 = lines[i][4], lines[i][6]
                COUT, SOUT = lines[i][7], lines[i][9]
                rules.append({'rule': 'and', 'cond1': C1, 'stat1': S1,
                             'cond2': C2, 'stat2': S2, 'cond_out': COUT, 'stat_out': SOUT})

    return rules


def submit_rules(rules, METRIC, INPUTS, OUTPUTS):
    for rule in rules:

        if rule['rule'] == 'simple':
            OUTPUTS[rule['cond_out']].set_output_value(
                rule['stat_out'], INPUTS[rule['cond']].get_membership(METRIC[rule['cond']], rule['stat']))

        if rule['rule'] == 'or':
            maxi = max(INPUTS[rule['cond1']].get_membership(METRIC[rule['cond1']], rule['stat1']),
                       INPUTS[rule['cond2']].get_membership(METRIC[rule['cond2']], rule['stat2']))
            OUTPUTS[rule['cond_out']].set_output_value(rule['stat_out'], maxi)

        if rule['rule'] == 'and':
            mini = min(INPUTS[rule['cond1']].get_membership(METRIC[rule['cond1']], rule['stat1']),
                       INPUTS[rule['cond2']].get_membership(METRIC[rule['cond2']], rule['stat2']))
            OUTPUTS[rule['cond_out']].set_output_value(rule['stat_out'], mini)

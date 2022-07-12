class FUZZYFY:
    def __init__(self, name, dic, output=False, step=0.01):
        self.name = name
        self.fuzzy_sets = dic
        if output:
            self.mini = 0
            self.maxi = 4

            self.output = {}
            self.step = step
            self.list_defuzzyfication = []

            for i in self.fuzzy_sets.keys():
                self.output[i] = 0

    def set_output_value(self, fuzzy_set, value):
        self.output[fuzzy_set] = max(value,self.output[fuzzy_set])
        print(fuzzy_set, value)

    def prepare_defuzzyfication(self):
        i = self.mini
        while i <= self.maxi:
            self.list_defuzzyfication.append((i, self.get_max_fuzzy(self.output, i)))
            print(i, self.get_max_fuzzy(self.output, i))
            i = i + self.step
    
    def cut_fuzzy(self, x, value, fuzzy_set):
        return min(self.get_membership(x, fuzzy_set), value)
    
    def get_max_fuzzy(self, output, x):
        f_set = list(self.fuzzy_sets.keys())
        maxi = self.cut_fuzzy(x, output[f_set[0]], f_set[0])
        for i in f_set:
            maxi = max(maxi, self.cut_fuzzy(x, output[i], i))
        return maxi
    
    def get_membership(self, x, fuzzy_set):

        fuzzy_points = self.fuzzy_sets[fuzzy_set]
        
        # Computing membership for triangles
        if len(fuzzy_points) == 3:
            if x <= fuzzy_points[0][0]:
                return 0
            elif fuzzy_points[0][0] < x <= fuzzy_points[1][0]:
                return (x - fuzzy_points[0][0]) / (fuzzy_points[1][0] - fuzzy_points[0][0])
            elif fuzzy_points[1][0] < x <= fuzzy_points[2][0]:
                return (fuzzy_points[2][0] - x) / (fuzzy_points[2][0] - fuzzy_points[1][0])
            else:
                return 0

        # Computing membership for trapezoids and crisps
        elif len(fuzzy_points) == 2:
            if x <= fuzzy_points[0][0]:
                return fuzzy_points[0][1]
            elif x >= fuzzy_points[1][0]:
                return fuzzy_points[1][1]
            else:
                if fuzzy_points[0][1] == 0:
                    return (x - fuzzy_points[0][0]) / (fuzzy_points[1][0] - fuzzy_points[0][0])
                else:
                    return 1 - (x - fuzzy_points[0][0]) / (fuzzy_points[1][0] - fuzzy_points[0][0])


chest_pain = FUZZYFY('chest_pain', {
    "typical_anginal": [(0.999, 0), (1, 1), (1.001, 0)],
    "atypical_anginal": [(1.999, 0), (2, 1), (2.001, 0)],
    "non_aginal_pain": [(2.999, 0), (3, 1), (3.001, 0)],
    "asymptomatic": [(3.999, 0), (4, 1), (4.001, 0)],
})

blood_pressure = FUZZYFY('blood_pressure', {
    "low": [(111, 1), (134, 0)],
    "medium": [(127, 0), (139, 1), (153, 0)],
    "high": [(142, 0), (157, 1), (172, 0)],
    "very_high": [(154, 0), (171, 1)],
})

cholestrol = FUZZYFY('cholesterol', {
    "low": [(151, 1), (197, 0)],
    "medium": [(188, 0), (215, 1), (250, 0)],
    "high": [(217, 0), (263, 1), (307, 0)],
    "very_high": [(281, 0), (347, 1)]
})

blood_sugar = FUZZYFY('blood_sugar', {
    "true": [(105, 0), (120, 1)],
    "false": [(105, 1), (120, 0)]
})

ecg = FUZZYFY('ecg', {
    "normal": [(0, 1), (0.4, 0)],
    "abnormal": [(0.2, 0), (1, 1), (1.8, 0)],
    "hypertrophy": [(1.4, 0), (1.9, 1)]
})

heart_rate = FUZZYFY('heart_rate', {
    "low": [(100, 1), (141, 0)],
    "medium": [(111, 0), (152, 1), (194, 0)],
    "high": [(152, 0), (210, 1)]
})
exercise = FUZZYFY('exercise', {
    "true": [(0.999, 0), (1, 1), (1.001, 0)],
    "false": [(-0.001, 0), (0, 1), (0.001, 0)],
})
old_peak = FUZZYFY('old_peak', {
    "low": [(1, 1), (2, 0)],
    "risk": [(1.5, 0), (2.8, 1), (4.2, 0)],
    "terrible": [(2.5, 0), (4, 1)]
})

thallium_scan = FUZZYFY('thallium_scan', {
    'normal': [(2.999, 0), (3, 1), (3.001, 0)],
    'medium': [(5.999, 0), (6, 1), (6.001, 0)],
    'high': [(6.999, 0), (7, 1), (7.001, 0)],
})

sex = FUZZYFY('sex', {
    "female": [(0.999, 0), (1, 1), (1.001, 0)],
    "male": [(-0.001, 0), (0, 1), (0.001, 0)]
})

age = FUZZYFY('age', {
    "young": [(29, 1), (38, 0)],
    "mild": [(33, 0), (38, 1), (45, 0)],
    "old": [(40, 0), (48, 1), (58, 0)],
    "very_old": [(52, 0), (60, 1)]
})

health = FUZZYFY("health", {
    "healthy": [(0.25, 1), (1, 0)],
    "sick_1": [(0, 0), (1, 1), (2, 0)],
    "sick_2": [(1, 0), (2, 1), (3, 0)],
    "sick_3": [(2, 0), (3, 1), (4, 0)],
    "sick_4": [(3, 0), (3.75, 1)]
}, output=True)


INPUTS = {
    'chest_pain': chest_pain,
    'blood_pressure': blood_pressure,
    'cholestrol': cholestrol,
    'blood_sugar': blood_sugar,
    'ecg': ecg,
    'heart_rate': heart_rate,
    'exercise': exercise,
    'old_peak': old_peak,
    'thallium_scan': thallium_scan,
    'sex': sex,
    'age': age,
}

OUTPUTS = {
    'health': health
}

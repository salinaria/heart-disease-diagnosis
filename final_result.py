from defuzzification import run


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        a = run(input_dict)
        print(a)
        res = ''
        if a < 1.78:
            res += 'Healthy & '
        if 1 <= a < 2.51:
            res += 'sick1 & '
        if 1.78 <= a < 3.25:
            res += 'sick2 & '
        if 1.5 <= a < 4.5:
            res += 'sick3 & '
        if 3.25 < a:
            res += 'sick4 '
        if res[-2] == '&':
            res = res[:-2]
        res = res + ': ' + str(a)

        return res

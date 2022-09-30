def botton_up(kb):
    C = []

    if 'assumables' in kb:
        for a in kb['assumables']:
            if ask(a):
                C.append(a)

    new_consequence = True

    while new_consequence:
        new_consequence = False 

        for head in kb['rules']:
            if head not in C: # Very innefient
                for body in kb['rules'][head]:
                    if not set(body).difference(set(C)): # Very innefient
                        C.append(head)
                        new_consequence = True

    return C

def abduction(kb, obs):

    if not obs:
        return []

    conseqLogica = botton_up(kb)
    observationRules = []

    for o in obs:
        observationRules += kb["rules"][o]
    
    expl = []

    for regra in observationRules:
        isExplanation = True
        ruleAssumables = []
        for ass in regra:
            ruleAssumables.append(ass)

            if not (ass in conseqLogica or ass in kb["assumables"]):
                isExplanation = False
                ruleAssumables = []
                break

        if isExplanation and not (regra in expl):
            expl += [regra]

    return expl

def ask(askable):
    ans = input(f'Is {askable} true?')
    return True if ans.lower() in ['sim','s','yes','y'] else False


if __name__ == "__main__":
    
    kb = {'rules':{'a':[['b','c']],
                   'b':[['d'],['c']],
                   'd':[['h']],
                   'g':[['a','b','c']],
                   'f':[['h','b']]},
            'assumables':['c','e']}

    obs = ['a', 'b', 'd']

    print(f"Explicacao de {obs} - {abduction(kb, obs)}")
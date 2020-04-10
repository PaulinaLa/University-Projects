import json
from z3 import *


def ingredients_list(ingredients, params):
    result = {}
    for i in ingredients:
        foo = {}
        for p in params:
            foo[p] = i[p]
        result[i['nazwa']] = foo
    return result

def vars(meals, ing_list):
    var_index = 0
    result = {}
    for m in meals:
        foo = {}
        for key in ing_list:
            foo[key] = Int(str(var_index))
            var_index += 1
        result[m] = foo
    return result


def assertions(result, ing_list, fvars, goal, conflicts):

    food = fvars.values()
    for meal in food:
        mfig = list(meal.values())
        sum = 0
        for m in mfig:
            sum += m
        result.add(sum > 0)
        for var in mfig:
            result.add(var >= 0)

    for factor in goal:
        amount = set()
        for ing in ing_list:
            foo = set()
            sum = 0
            for meal in fvars:
                foo.add(ToReal(fvars[meal][ing]) * ing_list[ing][factor])
            for elem in foo:
                sum += elem
            amount.add(sum)
        Totsum = 0
        for elem in amount:
            Totsum += elem
        result.add(Totsum >= goal[factor]['min'])
        result.add(Totsum <= goal[factor]['max'])

    for mess in conflicts:
        fst = mess['nazwa1']
        snd = mess['nazwa2']
        for vars in food:
            result.add(Or(
                And(vars[fst] > 0, vars[snd] == 0),
                And(vars[fst] == 0, vars[snd] > 0),
                And(vars[fst] == 0, vars[snd] == 0)))


def main():
    file_name = input()
    with open(file_name, 'r', encoding= 'utf-8') as f:
        dicts = json.load(f)
    meals = ['śniadanie', 'lunch', 'obiad', 'podwieczorek', 'kolacja']
    params = dicts['parametry']
    ingredients = dicts['składniki']
    conflicts = dicts['konflikty']
    goal = dicts['cel']
    food = ingredients_list(ingredients,params)
    fvars = vars(meals, food)
    result = Solver()
    assertions(result, food, fvars, goal, conflicts)

    if result.check() == sat:
        menu = result.model()
        for meal in fvars:
            diet = []
            for ing in fvars[meal]:
                amount = menu.evaluate(fvars[meal][ing]).as_long()
                diet += [ing] * amount
            print(meal + ': ', end='')
            print(', '.join(diet))
    else:
        print('Nie można wygenerować diety.')

main()


def parser():
    line_number = 0
    ingr_count = 0
    empty_line = 0
    cook_book = {}
    with open('recept.txt', 'r') as f:
        for i, line in enumerate(f):
            if i==line_number:
                dish = line
                ingredients = []
            elif i==line_number+1:
                ingr_count = int(line)
                line_number = i + ingr_count + 2
                empty_line = i + ingr_count
            elif i<=empty_line:
                result = line.replace('\n', '').split(' | ')
                ingr = {'ingridient_name': result[0], 'quantity': int(result[1]), 'measure': result[2]}
                ingredients.append(ingr)
                if i==empty_line:
                    cook_book[dish.replace('\n', '')] = ingredients
    print(cook_book)
parser()

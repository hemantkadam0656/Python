def main():
    list = []
    result = []
    dict_values = {}

    for i in range(int(input())):
        name = input()
        score = float(input())
        list.append((name,score))
        dict_values[name] = score
    
    marks = sorted(set([i for i in dict_values.values()]))

    second_lowest = marks[1]

    for x,y in dict_values.items():
        if y == second_lowest:
              result.append(x)   
        else:
            continue

    for z in sorted(result):
        print(z)

  
if __name__ == '__main__':
    main()
    

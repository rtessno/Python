#### average.py

def main():
    mylist = [70,80,90]
    show_scores(mylist)

def show_scores(scorelist):
    count = 0    ### counter
    total = 0    ### accumulator
    for score in scorelist:
        total += score
        count += 1
    average = total / count
    print('Average:',format(average,'.2f'))



main()

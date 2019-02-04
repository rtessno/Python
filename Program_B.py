#Robert Tessnow-Ramirez
#October 12, 2016 ©
#Program B
# The Pseudocode
#   Start the Program
#    In main, create an empty list
#    Open the file named scores.txt
#    use a while loop that can detect the end of file to read the scores and add them
#    to the list
#    close file.
#    call the showscores function with the list of scores as sole argument
#    inside the showscores function"
#        process the list of scores
#        print out the average score accurate to two decimal places
#   End Program

def main():                                 #start program
    
    scores = []                             #create a empty list
    scores_file = open("scores.txt",'r')    #read scores.txt file
    line = scores_file.readline()           #test for an empty string
    while line != '':                       #as long as an empty sting is not returned, continue processing
        score = float(line)
        line = scores_file.readline()       #continue processing
        
        scores.append(score)                 #add data to scores list
    scores_file.close()                     ### close file
    showscores(scores)                      #calls showscores function passing the list as sole argument

def showscores(scores):                     #define showscores catching scores list as sole argument
    number_of_scores = 0                    #accumulate the total number of scores in file
    total_of_scores = 0                     #accumulate total of all scores added together
    average = 0                             #divide total number of scores by total added together to get average
    for i in scores:                        #processes the list
        number_of_scores += 1               #accumulate each score in file
        total_of_scores += i                #adds all scores together
    average = total_of_scores / number_of_scores #calculates average
    print('The average of all scores is ', "%.2f" % average) #prints average of all scores
   
main()# end program

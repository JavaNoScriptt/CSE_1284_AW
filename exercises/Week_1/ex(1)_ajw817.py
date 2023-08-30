# compute average of a certian amount of test scores
#
# This program computes an average score for 3 quizzes.



# get the three

print( "\nEnter your three(3) quiz scores\n" )

score1,score2,score3 = int(input( "score 1: " )), int(input( "score 2: " )),int(input( "score 3: " )) 

print('\n')


# compute the average score

avg = (score1 + score2 + score3)/3

# display the average score and the inputed values

print( f"The net average of {score1},{score2},{score3} is: {avg:.2f}")
print()




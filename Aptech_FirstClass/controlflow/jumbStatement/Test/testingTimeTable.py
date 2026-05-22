# write a python program to print 1 -12 out and display the values example just like the time table of  and 2-12 and 3-12 and so on so 
# know input add just to display the time table of 1-12 in a straight line 

# -------------------- stupid methiod ----------------------
# time2 = "1 = 2, 2 = 4, 3 = 6, 4 = 8, 5 = 10, 6 = 12, 7 = 14, 8 = 16, 9 = 18, 10 = 20, 11 = 22, 12 = 24"
# time3 = "1 = 3, 2 = 6, 3 = 9, 4 = 12, 5 = 15, 6 = 18, 7 = 21, 8 = 24, 9 = 27, 10 = 30, 11 = 33, 12 = 36"
# time4 = "1 = 4, 2 = 8, 3 = 12, 4 = 16, 5 = 20, 6 = 24, 7 = 28, 8 = 32, 9 = 36, 10 = 40, 11 = 44, 12 = 48"
# time5 = "1 = 5, 2 = 10, 3 = 15, 4 = 20, 5 = 25, 6 = 30, 7 = 35, 8 = 40, 9 = 45, 10 = 50, 11 = 55, 12 = 60"
# time6 = "1 = 6, 2 = 12, 3 = 18, 4 = 24, 5 = 30, 6 = 36, 7 = 42, 8 = 48, 9 = 54, 10 = 60, 11 = 66, 12 = 72"
# time7 = "1 = 7, 2 = 14, 3 = 21, 4 = 28, 5 = 35, 6 = 42, 7 = 49, 8 = 56, 9 = 63, 10 = 70, 11 = 77, 12 = 84"
# time8 = "1 = 8, 2 = 16, 3 = 24, 4 = 32, 5 = 40, 6 = 48, 7 = 56, 8 = 64, 9 = 72, 10 = 80, 11 = 88, 12 = 96"
# time9 = "1 = 9, 2 = 18, 3 = 27, 4 = 36, 5 = 45, 6 = 54, 7 = 63, 8 = 72, 9 = 81, 10 = 90, 11 = 99, 12 = 108"
# time10 = "1 = 10, 2 = 20, 3 = 30, 4 = 40, 5 = 50, 6 = 60, 7 = 70, 8 = 80, 9 = 90, 10 = 100, 11 = 110, 12 = 120"
# time11 = "1 = 11, 2 = 22, 3 = 33, 4 = 44, 5 = 55, 6 = 66, 7 = 77, 8 = 88, 9 = 99, 10 = 110, 11 = 121, 12 = 132"
# time12 = "1 = 12, 2 = 24, 3 = 36, 4 = 48, 5 = 60, 6 = 72, 7 = 84, 8 = 96, 9 = 108, 10 = 120, 11 = 132, 12 = 144"

# # display the time table of 1-12 in a straight line
# print(time2, time3, time4, time5, time6, time7, time8, time9, time10, time11, time12)
# # print(time2 )

# -------------------- smart method ----------------------
print("                                               Multiplication Table                    \n")
for i in range(1,12):
    for j in range(1,12):
    
        # use nested loop to display the time table of 1-12 in a straight line
        print(f"{i} x {j} = {i*j}", end="\t") # \t horizontal tab (each end of the horizontal)
    # print() # to move to the next line after each row is printed
    
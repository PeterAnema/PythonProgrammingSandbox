
#for j in range(1,11):
#    for i in range(1,11):
#        print("%5d" % (j*i), end="")
#    print("")

# of -----------------------------------------------------------

##tafels = []
##for j in range(1,11):
##    tafel = []
##    for i in range(1,11):
##        tafel.append(j*i)
##    tafels.append(tafel)
##
##for j in range(10):
##    for i in range(10):
##        print("%5d" % tafels[i][j], end='')
##    print("")

# of -----------------------------------------------------------

##tafels = []
##for j in range(1,11):
##	tafels.append([j*i for i in range(1,11)])
##
##for tafel in tafels:
##    print("".join(["%5d" % n for n in tafel]))

# of -----------------------------------------------------------

#tafels = [[j*i for i in range(1,11)] for j in range(1,11)]
#
#for tafel in tafels:
#    print("".join(["%5d" % n for n in tafel]))

# of -----------------------------------------------------------

print("\n".join("".join(["%5d" % n for n in tafel]) for tafel in [[j*i for i in range(1,11)] for j in range(1,11)]))

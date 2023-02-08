stop = 4
i = 0
for cell in td:
    print("<td>%s</td>\n" % cell)
    if i == stop: 
        print ("</tr><tr>\n")
        stop == i + 5
    i += 1

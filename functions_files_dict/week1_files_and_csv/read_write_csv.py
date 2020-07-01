olympians = [
    ("John Aalberg", 31, "Cross Country Skiing"),
    ("Minna M", 30, "Sailing"),
    ("Win Valdemar", 54, "Art Comp"),
    ("Wakako", 34, "Testing")
]

outfile = open("reduce.csv", "w")
outfile.write("Name,Age,Sport")
for o in olympians:
    row_string = "{},{},{}".format(o[0],o[1],o[2])
    outfile.write(row_string)
    outfile.write("\n")
outfile.close()
import os
import csv
print(os.path.join("Users", "bob", "st.txt"))
#
st = open("st.txt", "w")
st.write("Test string")
st.close()

#
with open("st.txt", "w") as f:
    f.write("test string number 2")
#
with open("st.txt", "r") as f:
    print(f.read())
#CSV
with open("st2.csv", "w") as f:
    w = csv.writer(f,
                   delimiter = ",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])
#
with open("st2.csv", "r") as f:
    r = csv.reader(f, delimiter = ",")
    for row in r:
        print(",".join(row))

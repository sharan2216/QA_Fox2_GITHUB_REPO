def meth():
    with open("C:\\Users\\shashi\\Desktop\\abc.txt") as f:
        lines=f.readlines()
        for line in lines:
            if line.startswith("my"):
                print(line)
                print("--------------")
            if not (line.startswith("my")):
                print(line)

meth()



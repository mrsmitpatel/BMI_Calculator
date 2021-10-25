def main():
    z = int(input("Enter Weight"))
    y = float(input("Enter height"))
    x = (z / y ** 2)
    if x < 18.5:
        print("Underweight")
    elif x >= 18 and x < 25:
        print("Normal")
    elif x >= 25 and x < 30:
        print("Overweight")
    elif x >= 30:
        print("Obesity")

main()




def check_temp(min_value):
    error = "Please enter a number that is more than {}".format(min_value)

    try:
        reponse = float(input("Choose a number: "))

        if reponse < min_value:
            print(error)
        else:
            return reponse

    except ValueError:
        print(error)

# *** Main routine ***

while True:
    to_check = check_temp(-273)
    print("Success")
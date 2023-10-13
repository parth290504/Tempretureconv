def convert():
    print(
        "Hello there, welcome to tempreture converter, which converts tempreture between degree celcius and fahrenheit")
    x = (input(
        "\nWhich measurement of tempreture you would like to provide, \n press 1 for fahrenheit \n press 2 for degree celcius  "))
    y = float(input("enter the value: "))
    if x == "1":
        deg_ans = (y - 32) * (5 / 9)
        print("so you wanted to convert tempreture from fahrenheit to degree celcius \n ")
        print("Your value when converted into degree gives:", deg_ans)
    elif x == "2":
        fans = y * (9 / 5) + 32
        print("since you wanted to convert Degree Celcius into Farehenite \n")
        print("Your value when converted into fahrenheit gives : ", fans)
    else:
        print("Invalid choice")

    print("Thankyou for using this simple tempreture converter")

    z=int(input("\nDo you wish to convert tempretures once again?\n Press 1 if yes\n Press 2 if no\n"))
    if z==1:
      convert()

    elif z==2:
        print("Thank you for using this simple tempreture converter")



    else:
        print("kindly select a valid choice")


convert()
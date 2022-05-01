import math
import time
print("This is a Sphere Volume Calculator:\n Insert the lenght of the Sphere's Radius.")
print("if you want to turn off the calculator type the number '0'")

def cal_sphere_vol():

        x = (4 / 3)
        y = math.pi
        calculator = True

        while calculator:
            user = float(input(">>> Sphere Radius:"))
            print(user)

            try:

                if user != 0:
                    print(type(user))
                    radius = user ** 3
                    calculation = radius * (x * y)
                    print("The Volume of your Sphere is {}".format(calculation))
                    time.sleep(1)
                    print("What is your next Sphere's Radius?")
                else:
                    print("Your are turning off the calculator...")
                    time.sleep(0.5)
                    print("3")
                    time.sleep(0.5)
                    print("2")
                    time.sleep(0.5)
                    print("1...")
                    time.sleep(0.5)
                    print("Booom!!!!!!!!!!!!!!")
                    time.sleep(1)
                    print("Goodbye!")
                    break
            except ValueError:
                print("It must be a number digit!!")


function_try = cal_sphere_vol()
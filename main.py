def main():

    celsius = int(input('Enter the temp in C: '))
    fahrenheit = (9/5)*celsius + 32


    print(f"{celsius} in celcius is {fahrenheit} in fahrenheit")



    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()

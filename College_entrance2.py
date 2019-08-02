# Checks to make sure user inputs a float, loops till number is inputed
def check_float():
    try:
        value = float(input(" : "))
        return value
    except ValueError:
        print("Please type in a number")
        return check_float()

# Checks to make sure user inputed a y or n, loops till properly inputed
def check_yn():
    yn = input(" : ")
    yn = yn.lower()
    if yn not in ["y", "yes", "n", "no"]:
        print("Invalid response, please type y or n")
        return check_yn()
    elif yn == "y" or yn == "yes":
        return True
    elif yn == "n" or yn == "no":
        return False

# Checks to see if age is in desired range, if in range returns age, if out of range returns False
def get_age(min, max):
    print("How old are you?")
    age = check_float()
    if age < min or age > max:
        return False
    else:
        return age

# Checks to see if gpa is in desired range, if in range returns gpa, if out of range returns False
def get_gpa(min):
    print("What is your GPA?")
    gpa = check_float()
    if gpa < 0 or gpa > 5:
        print("Invalid range, GPA range 0-5")
        return get_gpa(2.5)
    elif gpa >= min:
        return gpa
    elif gpa < min:
        return False

# Checks to see if sat is in desired range, if in range returns sat, if out of range returns False
def get_sat(min):
    print("What is your SAT Score?")
    sat = check_float()
    if sat < 0 or sat > 2400:
        print("Invalid range, SAT range 0-2400")
        return get_sat(1700)
    elif sat >= min: 
        return sat
    elif sat < min:
        return False

# Checks to see if parents whent to our college, if they did returns True, if not returns False
def get_parent():
    print("Did your parents attened our college?")
    par = check_yn()
    return par

# Converts given vairable into 0-3 higher the better
def convert123(var, bestL, bestH, goodL, goodH):
    var = int(var)
    if var == False:
        value = 0
        return value
    elif var in range(bestL, bestH):
        value = 3
        return value
    elif var in range(goodL, goodH):
        value = 2
        return value
    else:
        value = 1
        return value

# Converts parent True/ False into 2 or 0 respectivly
def convert_parent(par):
    if par == True:
        value = 2
        return value
    elif par == False:
        value = 0
        return value

age = get_age(16, 60)
gpa = get_gpa(2.5)
sat = get_sat(1700)
par = get_parent()

print(f"age: {age} | gpa: {gpa} | SAT: {sat} | Parrent: {par}")

age1 = convert123(age, 16, 30, 30, 40)
gpa1 = convert123(gpa, 4, 6, 3, 5)
sat1 = convert123(sat, 2000, 2401, 1800, 2000)
par1 = convert_parent(par)

print(f"age: {age1} | gpa: {gpa1} | SAT: {sat1} | Parrent: {par1}")

total = age1 + gpa1 + sat1 + par1

if total >= 6:
    print("Welcome to our college")
else:
    print("Sorry, you were not accepted to our college")
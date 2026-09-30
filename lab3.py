a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
equation = f"{a}x^2"
if b< 0:
    equation += f" - {abs(b)}x"
else:
    equation += f" + {b}"
if c < 0:
    equation += f" - {abs(c)}"
else:
    equation += f" + {c}"
print("Your equation is: \n     " + equation)

discrim = (b**2) - 4 * a * c

if discrim > 0:
    root1 = (-b + (discrim ** 0.5))/(2 * a)
    root2 = (-b - (discrim ** 0.5))/(2 * a)
    print(f"Your roots are: \n x = {root1}\n x={root2}")

if discrim == 0:
    root1 = -b/(2*a)
    print(f"Your root is: {root1}")

if discrim < 0:
    real1 = -b/(2*a)
    imag1 = (abs(discrim) ** 0.5)/(2*a)
    print(f"Your roots are: \n x = {real1} + {imag1}i\n x = {real1} - {imag1}i")
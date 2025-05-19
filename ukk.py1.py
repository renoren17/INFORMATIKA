a = 10
b = 0
op = "/"

if op == "+":
    hasil = a + b
elif op == "-":
    hasil = a - b
elif op == "*":
    hasil = a * b
elif op == "/" and b != 0:
    hasil = a / b
else:
    print("Operator tidak dikenal.")


if 'hasil' in locals():
    print("Hasil =", hasil)

"""An example of function definition."""


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else:
        return b

x: int = 6
y: int = 5 + 2
z: int = my_max(x,y)
print(z)

print(chr(129313))
print("110 is on a \U0001F6A2")
print("Hello\nworld\n!!!")

age: int = 21
msg: str = f"You are {age}!"
print(msg)
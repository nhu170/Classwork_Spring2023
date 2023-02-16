def calc(a):
    if type(a) is str:
        raise TypeError("Cannot input string")
    ans = a**2
    return a


def main():
    x = "2"
    try:
        ans = calc(x)
    except TypeError:
        new_x = int(x)
        ans = calc(new_x)
    print(ans)


if __name__ == "__main__":
    main()

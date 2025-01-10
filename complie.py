import dis


async def main():
    x = 1
    y = 2
    await add(x, y)


async def add(x, y):
    return x + y


if __name__ == "__main__":
    dis.dis(main)
    main()

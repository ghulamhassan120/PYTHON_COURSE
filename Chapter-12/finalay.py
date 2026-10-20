
def main():

    try:
        a=int(input("Hey "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("OK")

main()
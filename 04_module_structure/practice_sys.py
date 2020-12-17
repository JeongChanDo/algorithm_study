import sys

def main():
    #python path environment variable
    print(sys.path)
    for arg in sys.argv[1:]:
        print(arg)


if __name__ == "__main__":
    main()
import sys
import time
import string

from extender import *

# ----------------------------------------------
if __name__ == '__main__':
    start_time = time.time()
    container = Container()
    outputFileName = "output.txt"
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Incorrect command line! You must write: python main "
              "<inputFileName> [<outputFileName>]")
        sys.exit(1)
    if sys.argv[1] == "-f":
        if len(sys.argv) == 4:
            inputFileName = sys.argv[2]
            outputFileName = sys.argv[3]
        elif len(sys.argv) == 3:
            inputFileName = sys.argv[2]
            outputFileName = "output.txt"
        else:
            print("incorrect command line!\n"
                  "  Waited:\n"
                  "     python main.py -f infile outfile\n"
                  "  Or:\n"
                  "     python main.py -n number outfile\n")
            exit()

        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        figNum = ReadStrArray(container, strArray)

    elif sys.argv[1] == "-n":
        count = -1
        if len(sys.argv) == 4:
            try:
                count = int(sys.argv[2])
            except Exception:
                print("Incorrect number of figures")
                sys.exit()
            outputFileName = sys.argv[3]
        elif len(sys.argv) == 3:
            try:
                count = int(sys.argv[2])
            except Exception:
                print("Incorrect number of figures")
                sys.exit()
            outputFileName = "output.txt"
        else:
            print("incorrect command line!\n"
                  "  Waited:\n"
                  "     python main.py -f infile outfile\n"
                  "  Or:\n"
                  "     python main.py -n number outfile\n")
            exit()
        if (count < 1) or (count > 10000):
            print("Incorrect number of figures")
            sys.exit()
        container.InRnd(count)
    else:
        print("incorrect command line!\n"
              "  Waited:\n"
              "     python main.py -f infile outfile\n"
              "  Or:\n"
              "     python main.py -n number outfile\n")
        exit()

    print('==> Start')

    ofile = open(outputFileName, 'w')
    print('Before sorted:')
    ofile.write("Before sorted:\n")
    container.Print()
    container.Write(ofile)

    container.merge_sort(0, len(container.store))

    print('\nAfter sorted:')
    ofile.write("\nAfter sorted:\n")
    container.Print()
    container.Write(ofile)
    ofile.close()

    print('==> Finish')

    print("--- %s seconds ---" % (time.time() - start_time))

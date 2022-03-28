def swapFileData():
    sample1 = input('Enter the name of 1st file:')
    sample2 = input('Enter the name of 1st file:')

    with open(sample1, 'r') as a:
        data_a = a.read()

    with open(sample2, 'r') as a:
        data_a = a.read()

    with open(sample1, 'w') as a:
        a.write(data_b)

    with open(sample2, 'w') as a:
        a.write(data_b)

    countingWordsFromFile()

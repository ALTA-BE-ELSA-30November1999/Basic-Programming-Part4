def mean_median(array_input):
    mean = 1.0
    median = 1
    Length = len(array_input)
    if Length > 0 :
        for i in range (Length):
            mean = sum(array_input)/Length

        for j in range (len(array_input)) :
            Nilai1 = array_input[int(Length/2)]

            if Length % 2 == 0 :
                Nilai2 = array_input[int(Length/2)-1]
            else :
                Nilai2 = array_input[int(Length/2)]

            median = (Nilai1+Nilai2)/2
    else :
        return
    return (mean, median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)
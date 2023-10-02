def play_with_asterisk(n):
    pattern = " "
    List = []
    for i in range (n):
        for j in range (n-1) :
            List.append(" ")
        n -= 1
        for j in range (i + 1) :
            List.append("* ")
        List.append('\n')
    Hasil = "".join(map(str, List))


    return Hasil


if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """

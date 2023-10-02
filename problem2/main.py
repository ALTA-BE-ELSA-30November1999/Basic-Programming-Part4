def draw_xyz(N):
        Start_nilai = 0
        pattern = []
        for i in range (1, N+1):
                for j in range (1, N+1) :
                        Start_nilai += 1
                        # print(Start_nilai, end=' ')  
                        # print(Start_nilai,i,j)
                        if Start_nilai % 3 == 0 :
                                pattern.append("X ")
                        elif Start_nilai % 2 == 0 :
                                pattern.append("Z ")
                        elif Start_nilai % 2 == 1 :
                                pattern.append("Y ") 
                pattern.append("\n")
        Hasil = "".join(map(str, pattern))

        return Hasil
    
if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """
def pyramid_game(pyramid,size:int,source_i:int=1,target_i:int=3):
    """рекурсивный алгоритм игры ханойские башни (классические 3 оси)"""
    pyramid_size=len(pyramid[source_i-1])
    assert type(pyramid) is list and pyramid_size>0 and size>0
    if size==1:
         top_element=pyramid[source_i-1].pop()
         pyramid[target_i-1].append(top_element)
    else:
         tmp_i=6-source_i-target_i
         pyramid_game(pyramid,size-1,source_i,tmp_i)
         base_element=pyramid[source_i-1].pop()
         pyramid[target_i-1].append(base_element)
         pyramid_game(pyramid,size-1,tmp_i,target_i)

def pyramid_game_tests():

    print("test#1", end="")
    p=[[1],[],[]]
    pyramid_game(pyramid=p,size=len(p[0]))
    print("ok" if p==[[],[],[1]] else "fail")

    print("test#2", end="")
    p=[[1],[],[]]
    pyramid_game(pyramid=p,size=len(p[0]),source_i=1,target_i=2)
    print("ok" if p==[[],[1],[]] else "fail")

    print("test#3", end="")
    p=[[2,1],[],[]]
    pyramid_game(pyramid=p,size=len(p[0]))
    print("ok" if p==[[],[],[2,1]] else "fail")

    print("test#4", end="")
    p=[[],[10,9,8,7,6,5,4,3,2,1],[]]
    pyramid_game(pyramid=p,size=10,source_i=2,target_i=1)
    print("ok" if p==[[10,9,8,7,6,5,4,3,2,1],[],[]] else "fail")

if __name__ == "__main__":
    pyramid_game_tests()

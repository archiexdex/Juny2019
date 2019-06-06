def f1(s):
    return s[::-1]
    

def f2(s):
    return " ".join(map(f1 ,s.split(" ")))
    

if __name__ == "__main__": 
    s1 = "junyiacademy"
    print(f1(s1))
    s2 = "flipped class room is important"
    print(f2(s2))

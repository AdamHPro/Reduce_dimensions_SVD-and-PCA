def qui_est_grand(a, b) :
    if a<b :
        print(b + "est strictement plus grand que" + a)
    elif a>b :
        print(a + "est strictement plus grand que" + b)
    else :
        print( a + "=" + b)
    print("Et la différence est :"+abs(a-b))
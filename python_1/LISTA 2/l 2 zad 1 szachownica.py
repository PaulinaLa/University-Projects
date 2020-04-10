def wiersz1(k,n):
    return((" "*k+"#"*k)*n+"\n")

def wiersz2(k,n):
    return(("#"*k+" "*k)*n+"\n")
def szachownica(k,n):
    print((wiersz1(k,n)*k + wiersz2(k,n)*k)*n)

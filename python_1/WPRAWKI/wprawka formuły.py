from forms import *

def fv(f):
    if isVar(f):
        return set(getVar(f))
    if isNeg(f) :
        return fv(getNeg(f))
    if isDisj(f):
        return fv(getDisjL(f)) | fv(getDisjR(f))
    if isConj(f):
        return fv(getConjL(f)) | fv(getConjR(f))


print(fv(disj(var("x"),conj(neg(var("y")),var("z")))))


def val(f, S): #dostaję wartości w słowniku
    if isVar(f):
        return S[getVar(f)]
    if isNeg(f) :
        return  not val(getNeg(f),S)
    if isDisj(f):
        return val(getDisjL(f),S) or val(getDisjR(f),S)
    if isConj(f):
         return val(getConjL(f),S) and val(getConjR(f),S)
 

S= { "x":True, "y":False, "z":True}
print(val(disj(var("x"),conj(neg(var("y")),var("z"))),S))       
def F(f):
    if isVar(f):
        return neg(f)
    if isConj(f):
        return disj(F(getConjL(f)), F(getConjR(f)))
    if isDisj(f):
        return conj(F(getDisjL(f)),F(getDisjR(f)))
    if isNeg(f):
        return to_nnf(getNeg(f))
    
def to_nnf(f):
    if isVar(f):
        return f
    if isConj(f):
        return conj(to_nnf(getConjL(f)),to_nnf(getConjR(f)))
    if isDisj(f):
        return disj(to_nnf(getDisjL(f)),to_nnf(getDisjR(f)))
    if isNeg(f):
        return F(getNeg(f))

    """
        g = getNeg(f)
        if isVar(g):
            return f
        if isNeg(g):
            return to_nnf(getNeg(g))
        if isConj(g):
            return disj(F(getConjL(g)), F(getConjR(g)))
        if isDisj(g):
            return conj(F(getDisjL(g)), F(getDisjR(g)))
    """
print(to_nnf(disj(var("x"),conj(neg(var("y")),var("z")))))






    
  

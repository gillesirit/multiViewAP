# a is always a vector + its label
def atomic_analogy(a, b, c, d):  # return True/False 
    return (a == b and c == d) or (a == c and b == d)  # gggg ghgh gghh

def solve_atomic_analogy(a,b,c):
    if a==b:
        return c
    if a==c:
        return b
    return 100  # no solution

def vector_analogy(a, b, c, d, mask):  # we watch only the relevant features - return True/False
    res = True
    l = len(mask)
    for i in range(l):
        if mask[i] == 1:
            res = res and atomic_analogy(a[i], b[i], c[i], d[i])
    return res

def transitivity(a, b, c, d,e,f, mask):  # return True if transitivity, False otherwise focusing on mask
    return vector_analogy(a, b, c, d, mask) and vector_analogy(c, d, e, f , mask) and vector_analogy(a,b, e, f, mask)

def solve_vector_equation(a,b,c,mask):   # return vector solution if any, focusing on mask - a,b,c, mask have same length
    l=len(a)
    sol=[1000]*l
    for i in range(l):
        if mask[i] == 1:  # we focus on this feature
            sol[i]=solve_atomic_analogy(a[i],b[i],c[i])
    return sol
#################################### 

def mask_intersection(mask1,mask2): # create a new mask with and operator
    l=len(mask1)
    mask=[0]*l
    for i in range(l):
        if mask1[i]==1 and mask2[i]==1:
            mask[i]=1
    return mask

def central_permutation(a, b, c, d, m): # assume a:b::c:d on m
    return vector_analogy(a, c, b, d, m)
    

def get_full_analogy_count(set_of_pairs,mask):  # mask is the list of relevant indices like [0,0,1,0,1,1, etc...]
    #count_analogy=0
    #count_central_permutation=0
    list_of_analogy_on_mask=[]
    for a, b in set_of_pairs:
        for c, d in set_of_pairs:
            if (a==c).all():
                continue
            else:
                if vector_analogy(a, b, c, d, mask):
                    #count_analogy+=1
                    list_of_analogy_on_mask.append((a,b,c,d))
    return list_of_analogy_on_mask

def check_transitivity(list1,list2, mask):
    count=0
    candidate=0
    for (a,b,c,d) in list1:
        for (c1,d1,e,f) in list2:
            if (a==c1).all():  # we do not use (a,b) with (a,b)
                continue
            else:
                if (c==c1).all() and (d==d1).all():
                    candidate+=1
                    if transitivity(a, b, c, d,e,f, mask):
                        count+=1
    return candidate,count

    
def matching_profile_on_mask(u,v,focus): # true iff u[i]==v[i] when focus[i]=1
    res = True
    for i in range(len(focus)):
        if focus[i]==1:
            res =res and u[i]==v[i]
    return res

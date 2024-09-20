#Case Scenario 1
 
#t=no.of test cases
#n=array size
#p=local maxima
#q=local minima

def permutation():
    testcases=[]
    T=int(input("Enter the no. of test cases:                 "))
    for i in range(0,T):
        N,P,Q = input("Enter Array Size, Local Maxima,Local Minima :").split()
        test_case_data=[N,P,Q]
        testcases.append(test_case_data)
    
    for i, testcase in enumerate(testcases):
        N,P,Q=testcase
        
        n=int(N)
        p=int(P)
        q=int(Q)
        
        total_extrema=n-2
        
        if p + q > total_extrema:
            print("No")
        else:
            max_possible_maximas=(n-1)//2
            max_possible_minimas=(n-1)//2
            
            if p<=max_possible_maximas and q<=max_possible_minimas:
                print("Yes")
            else:
                print("No")
            
permutation()


# Elliptic Curve: y^2 = x^3 + A*x + B mod M
M = 218925954923455975113808255640357734801
A = 117784136680056914958014732219575150968
B = 115857097425776487375223208492285700589

G = (1, 12925268147578859956582415706419653103)
P = d1*G = (83120571548610219336387422119327889747, 142472226619953807903704206304442544019)
Q = d2*G = (132577002137522699788630037342938299835, 42276980267889888363445760641870330604)
K = d1*d2*G = d2*P = d1*Q

'''
Using Sage

sage: M = 218925954923455975113808255640357734801
sage: A = 117784136680056914958014732219575150968
sage: B = 115857097425776487375223208492285700589

sage: F = FiniteField(M)
sage: E = EllipticCurve(F,[A,B])
=> ArithmeticError: invariants (0, 0, 0, 117784136680056914958014732219575150968, 115857097425776487375223208492285700589) define a singular curve

#LETS OPEN UP THE EQUATION:
    y^2 + a_1*x*y +a_3*y = x^3 + a_2*x^2 + a_4*x + a_6
    a_1=0
    a_2=0
    a_3=0
    a_4=117784136680056914958014732219575150968
    a_6=115857097425776487375223208492285700589
    => ArithmeticError: invariants (0, 0, 0, 117784136680056914958014732219575150968, 115857097425776487375223208492285700589) define a singular curve
   
    #Looks like the curve is singular and Sagemath seems to be not happy working with these. Let's double check this and compute the discriminant following the formulae from http://mathworld.wolfram.com/EllipticDiscriminant.html
    b2 = a1^2 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3^2 + 4*a6
    b8 = a1^2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3^2 - a4^2
    Di = -b2^2*b8 - 8*b4^3 - 27*b6^2 + 9*b2*b4*b6
    Di % M
    => 0

    =>Discriminant=0

    #Lets calculate singularity:
    df/dx = 3*x^2 + 2*a_2*x + a_4 
    df/dy = 2y

    ##det = b^2-4ac
    det = GF(M)(4*a2^2 - 4*3*a4)
    =>119072044303508846300481002847602331991
    ##sol1=-b+sqrt(det)/2a
    ##sol2=-b-sqrt(det)/2a
    sol1 = GF(M)(-2a2 + sqrt(det))/2*3)
    

    =============>   +-3477412715407459121010679931851697672           <<<<<<<<<<=====================================

#We use the negative since it makes the equation easier


    sage: P.<x>=GF(p)[]
    sage: p
    218925954923455975113808255640357734801
    sage: f = x^3 + A*x + B
    sage: f_ = f.subs(x= x+xx)
    sage: f_
    x^3 + 208493716777233597750776215844802641785*x^2

    sage: G =(1, 12925268147578859956582415706419653103)
    sage: P =(83120571548610219336387422119327889747, 14247222
    ....: 6619953807903704206304442544019)
    sage: Q = (132577002137522699788630037342938299835, 422769
    ....: 80267889888363445760641870330604)
    sage: G_ = (GF(p)(G[0] - xx), GF(p)(G[1]))
    sage: P_ = (GF(p)(P[0] - xx), GF(p)(P[1]))
    sage: Q_ = (GF(p)(Q[0] - xx), GF(p)(Q[1]))
     
    sage: mapG = G_[0]*(G_[1]^-1)
    sage: mapP = P_[0]*(P_[1]^-1)
    sage: mapQ = Q_[0]*(Q_[1]^-1)
     
    sage: d1 = mapP*(mapG^-1)
    sage: d1
    51116768009652380563192358908292320535
    sage: d2 = mapQ*(mapG^-1)
    sage: d2
    166568400495699451586585094040868252006

#or with the possitive sign solution:
    114571619017273227328554287033022265700
    115148625482407323993738716583786078643


    discrete log(G->P)=60
    discrete log(G->Q)=65

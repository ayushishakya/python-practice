from numpy import *
from numpy.linalg import inv

def kf_predict(X, P, A, Q, B, U):
    X = dot(A, X) + dot(B, U)
    P = dot(A, dot(P, A.T)) + Q
    return (X, P)

def kf_update(X, P, Y, H, R):
    IM = dot(H, X)
    IS = R + dot(H, dot(P, H.T))
    K = dot(P, dot(H.T, inv(IS)))
    X = X + dot(K, (Y-IM))
    P = P - dot(K, dot(IS, K.T))
    LH = gauss_pdf(Y, IM, IS)
    return (X, P, K, IM, IS, LH)

def gauss_pdf(X, M, S):
    if M.shape()[1] == 1 :
        DX = X -tile(M, X.shape()[1])
        E = 0.5 * sum(DX * ( dot(inv(S), DX)) , axis = 0 )
        E = E + 0.5 * M.shape()[0] * log(2*pi) + 0.5 *log(det(S))
        P = exp(-E)
    elif X.shape()[1] == 1 :
        DX = tile(X, M.shape()[1]) - M
        E = 0.5 * sum(DX * ( dot(inv(S), DX)) , axis = 0 )
        E = E + 0.5 * M.shape()[0] * log(2*pi) + 0.5 *log(det(S))
        P = exp(-E)
    else :
        DX = X - M
        E = 0.5 * dot(DX.T, dot(inv(S), DX))
        E = E + 0.5 * M.shape()[0] * log(2*pi) + 0.5 *log(det(S))
        P = exp(-E)
    return (P[0], E[0])

#time step of mobile environment
dt = 0.1

#initialization of state matrices
Y =
H = array ([[1, 0, 0, 0], [0, 1, 0, 0]])
R = eye(Y.shape()[0])

#number of iterations
N_iter = 50

#applyting Kalman Filter
for i in arange(0, N_iter) :
    (X, P) = kf_predict(X, P, A, Q, B, U)
    (X, P, K, IM, IS, LH) = kf_update(X, P, Y, H, R)
    Y =

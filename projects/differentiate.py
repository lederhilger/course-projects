import numpy as np

def differentiate(u, dt):
    u_len = len(u)
    d = np.zeros(u_len)
    for i in range(1, u_len - 1):
        d[i] = (u[i+1] - u[i-1])/(2*dt)
    frwrd = (u[1] - u[0])/dt; bckwrd = (u[u_len - 1] - u[u_len - 2])/dt
    d[0] = frwrd; d[-1] = bckwrd
    return d

def differentiate_vector(u, dt):
    u_len = len(u)
    d = np.zeros(u_len)
    d[1:u_len-1] = (u[2:u_len] - u[0:u_len-2])/(2*dt)
    frwrd = (u[1] - u[0])/dt; bckwrd = (u[u_len - 1] - u[u_len - 2])/dt
    d[0] = frwrd; d[-1] = bckwrd
    return d

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()

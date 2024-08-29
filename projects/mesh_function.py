from numpy import exp, array, allclose, zeros_like

def mesh_function(f, t):
    mesh_function = zeros_like(t, dtype = float)
    for i in range(len(t)):
        mesh_function[i] = f(t[i])
    return mesh_function

def func(t):
    if t >= 0 and t <= 3:
        return exp(-t)
    elif t > 3 and t <= 4:
        return exp(-3*t)
    else:
        print("Domain not vlaid."); quit()

def test_mesh_function():
    t = array([1, 2, 3, 4])
    f = array([exp(-1), exp(-2), exp(-3), exp(-12)])
    fun = mesh_function(func, t)
    assert allclose(fun, f)

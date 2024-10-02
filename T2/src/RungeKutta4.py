import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    """The dot product of the of the operator and the state minus the dot product of the state and the operator, this rest multiplied by the imagiinary constant i=-1.0j. 
        Specifically the operator and the state have to be np.arrays with th same size. 


    
    Args:
        oper (Numpy array): First argument (linear operator).
        state (Numpy array): Second argument (initial state).


    Returns:
        (Numpy array): Returns the imaginary constant i multiplied by the dot product of the operator by the state minus the dot product of the state by the operator.


    Examples:
        Defining oOper as the linear operator and yInit the initial state of the system.  
        ```python
        oOper=np.array([[0, 1], [1, 0]])
        yInit = np.array([[1, 0], [0, 0]])
        dyn_generator(oOper, yInit)
        [[0.-0.j 0.+1.j]
        [0.-1.j 0.-0.j]]
        ```

    """
    return (np.dot(oper,state)-np.dot(state,oper))*(-1.0j)

def rk4(func, oper, state, h):
    """Four values each label by kn, n being every natural number from 1 to four. Specifically
        
        -If k=1 it`s defined by a value h multiplied by function evaluated in a operator and the state
        -If k=2 or k=3 it`s defined by a value h multiplied by function evaluated in a operator and the sum of the state plus k(n-1) divited by two       
        -If k=4 it`s defined by a value h multiplied by function evaluated in a operator and the state plus k3



    Parameters
    ----------
    
    Args:
        func (Fuction) Firts Argument (Function in charge of proportioning a matrix that it`s going to be use for the respective k`s) 
        oper (Numpy array): First argument (linear operator).
        state (Numpy array): Second argument (initial state).
        h (structure, object or primitive datatype):  Fourth Argument (The temporal step)

    Returns:
        (Numpy array): Returns the state plus 1/6 multiplied by "k1" plus two multiplied by "k2" plus two multiplied by "k4" plus "k4"

    Examples:

            rk4(dyn_generator, oOper, yInit, h)
            #Defining func=dyn_generator, oOper=np.array([[0, 1], [1, 0]]), yInit = np.array([[1, 0], [0, 0]]) and h=np.linspace(0,10,1000)[1] - np.linspace(0,10,1000)[0]
            [[9.99899803e-01+0.j         0.00000000e+00+0.01000934j]
            [0.00000000e+00-0.01000934j 1.00196954e-04+0.j        ]]
            """
    k1 = h*func(oper,state)
    k2 = h*func(oper,state+(k1/2))
    k3 = h*func(oper,state+(k2/2))
    k4 = h*func(oper,state+k3)
    return state + (1/6)*(k1+(2*k2)+(2*k3)+k4)

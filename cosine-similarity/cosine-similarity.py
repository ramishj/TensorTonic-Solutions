import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    
    if(np.linalg.norm(np.array(a))==0 or np.linalg.norm(np.array(b))==0):
        return float(0)
    return float (float(np.array(a)@np.array(b))/(float(np.linalg.norm(np.array(a))*np.linalg.norm(np.array(b)))))
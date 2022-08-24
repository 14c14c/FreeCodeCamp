import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError('List must contain nine numbers.')
  #raise error when list of less than 9 element is passed.
    
  mat = np.matrix([list[:3], list[3:6], list[6:9]])
  calculations = {}
  #set up matrix in numpy and dictionary
  
  calculations['mean'] = [mat.mean(axis=0).tolist()[0], mat.mean(axis=1).flatten().tolist()[0], mat.mean()]
  calculations['variance'] = [mat.var(axis=0).tolist()[0], mat.var(axis=1).flatten().tolist()[0], mat.var()]
  calculations['standard deviation'] = [mat.std(axis=0).tolist()[0], mat.std(axis=1).flatten().tolist()[0], mat.std()]
  calculations['max'] = [mat.max(axis=0).tolist()[0], mat.max(axis=1).flatten().tolist()[0], mat.max()]
  calculations['min'] = [mat.min(axis=0).tolist()[0], mat.min(axis=1).flatten().tolist()[0], mat.min()]
  calculations['sum'] = [mat.sum(axis=0).tolist()[0], mat.sum(axis=1).flatten().tolist()[0], mat.sum()]
  #actual calculations. flatten() method is needed for axis=1.
  
  return calculations

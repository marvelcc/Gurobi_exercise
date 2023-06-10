import gurobipy as gp
from gurobipy import GRB


# Base data
customers = ['i1', 'i2', 'i3', 'i4', 'i5']
facilities = ['j1', 'j2', 'j3']

demand = {'i1': 80, 'i2': 270, 'i3': 250, 'i4': 160, 'i5': 180}
activation_cost = {'j1': 1000, 'j2': 1000, 'j3': 1000}
capacity = {'j1': 500, 'j2': 500, 'j3': 500}
transport_cost = {('i1', 'j1'), 4
                  ('i1', 'j2'), 6
                  ('i1', 'j3'), 9
                  ('i2', 'j1'), 5
                  ('i2', 'j2'), 4
                  ('i2', 'j3'), 7
                  ('i3', 'j1'), 6
                  ('i3', 'j2'), 3
                  ('i3', 'j3'), 4
                  ('i4', 'j1'), 8
                  ('i4', 'j2'), 5
                  ('i4', 'j3'), 3
                  ('i5', 'j1'), 10
                  ('i5', 'j2'), 8
                  ('i5', 'j3'), 4}

# Create model
m = gp.Model('FLP')


# Create variables
m.addVars(vtype=)


import cvxpy
import numpy
from cvxpy import log

#function which return the index of the max value in a matrix

def maxM(matrix):
  max=matrix[0][0]
  maxM=0
  for k in range(len(matrix)):
      for i in range(len(matrix[0])):
        if(matrix[k][i]>max):
           max=matrix[k][i]
           maxI=i
  return maxM
       
    

# input some n people and m res 
rows = int(input("enter the number of rows:"))  #read num of rows
cows = int(input("enter the number of columns:")) #read num of columns
matrix1 = [] 
print("enter the values") 
for i in range(rows):         
    a =[] 
    for j in range(cows):      
         a.append(int(input())) 
    matrix1.append(a) 
  
# show the matrix
print(matrix1)

#list of variables - x1,x2....xn (n=num of people/rows)
arr=[]
for i in range(len(matrix1)):
    val=cvxpy.Variable()
    arr.append(val)

#convert to array structure
matrix=numpy.array(matrix1)
arrVal=numpy.array(arr)

val = [] 
maxM=maxM(matrix)
for n in range(len(matrix)):
        temp=0
        for m in range(len(matrix[0])):
            if(m==maxM):         #multiply the varaiables at the resource with the highest value
               temp += arrVal[n]*matrix[n][m]
            else:
               temp += matrix[n][m] #the other resources
        val.append(log(temp)) #adding every row as a log function

#sum of the logs
obj=numpy.array(val) 
objective=0
for i in range(len(obj)):
 objective=objective+obj[i]    #sum up all the logs to collective objective

FinalObjective=cvxpy.Maximize(objective)  

constrains = []
temp_cons = 0 #summary of the values must be 1
for i in arrVal:
   constrains.append(0<=i)
   constrains.append(i<=1)
   temp_cons += i

constrains.append(temp_cons == 1)    
prob = cvxpy.Problem(FinalObjective,constrains)
prob.solve()

#show the result
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
       if (j==maxM):
         print("Agent#{} gets {} of resource# {}".format(i,arrVal[i].value*matrix[i][j],j))
       else:
         print("Agent#{} gets {} of resource# {}".format(i,matrix[i][j],j))







##Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
print("Total for salesArray: ", salesArray.sum())
print()

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
print("Min: ", salesArray.min())
print("Max: ", salesArray.max())
print()

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")
print("Sales greater than 100: ")
print()
sales_greater_100 = salesArray[salesArray >= 100]
print(sales_greater_100)
print()

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
print("Total for each register: ")
print()
print(salesArray.sum(axis = 1))
print()

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")
feeArray = salesArray*.02
print("Fee Array: ")
print()
print(feeArray)
print()
print("Total: ", feeArray.sum())
print()

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")
print("The after fees Array: ")
print()
after_fees_array = salesArray - feeArray
print(after_fees_array)
print()

## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")
print("2nd and 4th Registers:")
print()
print(salesArray[[1, 3]])
print()

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
print("Added 5th register: ")
print()
newRegister = np.array([[17.89,13.59,107.89,176.88,56.78]])
print(salesArray)
print()
salesArray = np.concatenate((salesArray, newRegister), axis=0)
print(salesArray)
print()

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")
sales
print()


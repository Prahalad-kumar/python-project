"""#write a program to store seven fruits in a list entered by the user.

#Create a empty list to store fruit name

fruits=[]

#using for loop to taking input seven type

for i in range(7):
    fruit=input(f" Enter fruit {i+1}:")

    #adding fruit in list

    fruits.append(fruit)

#print the fruits list

print("Enter fruits list ",fruits)"""

#write a program to accept marks for 6 studens and display them in a sorted.

# creating a empty list to store mark

marks=[]

# using to for loop to taking input five time

"""for i in range(6):
    mark=float(input(f"Enter the mark of student no {i+1}:"))
    # Ensure the mark is between 0 and 100
    if mark < 0 or mark > 100:
        print("Please enter a mark between 0 and 100.")
    else:
        marks.append(mark)

# store the mark in marks list.

   # marks.append(mark)

# sorting the marks list.

marks.sort()

#showing the result

print(marks)"""


# Function to accept marks for 6 students and display them sorted
def accept_and_sort_marks():
    # Initialize an empty list to store the marks
    marks = []

    # Loop to accept marks for 6 students
    for i in range(6):
        while True:
            try:
                # Prompt user to enter the mark for the student
                mark = float(input(f"Enter the mark for student {i + 1}: "))
                # Ensure the mark is between 0 and 100
                if mark < 0 or mark > 100:
                    print("Please enter a mark between 0 and 100.")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Sort the marks in ascending order
    marks.sort()

    # Display the sorted marks
    print("\nSorted marks:")
    for i, mark in enumerate(marks, start=1):
        print(f"Student {i}: {mark}")


# Call the function
accept_and_sort_marks()

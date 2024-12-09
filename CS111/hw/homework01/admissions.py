# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True

####################################################
# https://youtu.be/lIFE7h3m40U?si=2VSwF5PG33WxMXE2 #
####################################################
	
# define your functions here
def convert_row_type(lis):
    return [float(i) for i in lis]

def calculate_score(lis):
    return ((lis[0] / 160) * 0.3) + ((lis[1] * 2) * 0.4) + (lis[2] * 0.1) + (lis[3] * 0.2)
def is_outlier(student):
    return student[2] == 0 or (student[1] * 2) - (student[0] / 160) > 2
def calculate_score_improved(student):
    score = calculate_score(student)

    return is_outlier(student) or score >= 6
def grade_outlier(grades):
    lowest = 999999
    secondLowest = 999999

    # Faster than sorting the list first!!! :))))
    for grade in grades:
        if grade < lowest:
            secondLowest = lowest
            lowest = grade
        elif grade < secondLowest:
            secondLowest = grade
    
    return (secondLowest - lowest) > 20
def grade_improvement(grades):
    prev = -999999
    for grade in grades:
        if not (prev <= grade):
            return False
        prev = grade
    return True

def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")    
    
    
    print("Processing " + filename + "...")

    headers = input_file.readline()


    students = input_file.readlines()

    outputLines = []
    outputLinesChosen = []
    outliers = []
    chosenImproved = []
    outputCalculatedLinesImproved = []
    compositeChosen = []

    for student in students:
        student_list = student.split(',')
        name = student_list.pop(0)
        typed_student = convert_row_type(student_list)

        if not check_row_types(typed_student):
            print("AHHHHHHHHH")
        
        first = typed_student[0:4]
        second = typed_student[4:8]

        score = calculate_score(first)

        outputLines.append(f"{name},{score:.2f}")
        if score >= 6:
            outputLinesChosen.append(name)
        if is_outlier(typed_student):
            outliers.append(name)
        if (score >= 6) or (is_outlier(typed_student) and score >= 5):
            chosenImproved.append(name)
        
        if calculate_score_improved(typed_student):
            outputCalculatedLinesImproved.append(f'{name},{first[0]},{first[1]},{first[2]},{first[3]}')
        if score >= 6 or (score >= 5 and (is_outlier(typed_student) or grade_outlier(second) or grade_improvement(second))):
            compositeChosen.append(name)

    # Why's there an `\n` at the end >:(

    with open('student_scores.csv', 'w') as file:
        file.write('\n'.join(outputLines) + '\n')
    with open('chosen_students.csv', 'w') as file:
        file.write('\n'.join(outputLinesChosen) + '\n')
    with open('outliers.csv', 'w') as file:
        file.write('\n'.join(outliers) + '\n')
    with open('chosen_improved.csv', 'w') as file:
        file.write('\n'.join(chosenImproved) + '\n')
    with open('better_improved.csv', 'w') as file:
        file.write('\n'.join(outputCalculatedLinesImproved) + '\n')
    with open('composite_chosen.csv', 'w') as file:
        file.write('\n'.join(compositeChosen) + '\n')
        

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()

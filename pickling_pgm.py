import pickle

student={"name":"Joseph","age":34,6:9}

with open("student_detail.pkl","wb") as file:
    pickle.dump(student,file)

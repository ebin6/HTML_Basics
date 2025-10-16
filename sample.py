import pickle
with open("accounts.pkl","rb") as file:
    print(pickle.load(file))
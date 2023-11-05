import pickle

# Normal dictionary
hackers = {"neut":1, "geohot": 100, "neo":1000}

for key, value  in hackers.items():
    print(key, value)

# Now we will create a serializaed version of this dictionary BINARY FORMAT

serializaed_hackers = pickle.dumps(hackers)
print(serializaed_hackers)

# Now we will deserialize the dictionary and load it

hackers_v2 = pickle.loads(serializaed_hackers)
print(hackers_v2)

# Can be printed like the first one
for key, value in hackers_v2.items():
    print(key, value)

# We save as "wb" because the contents are bytes
with open("hackers.pickle", "wb") as handle:
    pickle.dump(hackers, handle)

# Now we load the bytes and print it as a normal dictionary

with open("hackers.pickle", "rb")as handle:
    pickle.load(handle)
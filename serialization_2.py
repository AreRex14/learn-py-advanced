# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
import pickle

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
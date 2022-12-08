from tensorflow import keras
import matplotlib.pyplot as plt
class MyFashion():
    def __init__(self):
        pass

    def exec(self):
        (train_input,train_target), (train_input,train_target) = keras.datasets.fashion_mnist.load_data()
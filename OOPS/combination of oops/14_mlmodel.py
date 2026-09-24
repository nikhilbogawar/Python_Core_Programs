# 14.
# Design:
# • Abstract class Model with train(), predict()
# • Implement LinearRegressionModel and DecisionTreeModel(just print or
# write a logic, focus on calling and concept)
# • A Pipeline class that:
# o Accepts any model
# o Uses composition to chain transformations
# o Overloads __call__() to run predictions
# • Encapsulates internal steps
from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def train(self, data):
        pass
    @abstractmethod
    def predict(self, input_data):
        pass
class LinearRegressionModel(Model):
    def train(self, data):
        print("Training Linear Regression on data")
    def predict(self, input_data):
        print("Predicting with Linear Regression")
        return 42
class DecisionTreeModel(Model):
    def train(self, data):
        print("Training Decision Tree on data")
    def predict(self, input_data):
        print("Predicting with Decision Tree")
        return "Class A"
class Pipeline:
    def __init__(self, model):
        self.model = model
        self.__steps = []
    def add_step(self, step):
        self.__steps.append(step)
    def __call__(self, input_data):
        print("Pipeline running...")
        for step in self.__steps:
            print("Step:", step)
        return self.model.predict(input_data)
pipe = Pipeline(LinearRegressionModel())
pipe.add_step("Normalization")
pipe.add_step("Feature Selection")
result = pipe("Sample Input")
print("Result:", result)

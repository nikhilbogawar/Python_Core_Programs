# 17. Create an abstract class MLModel with:
# • train(data)
# • predict(x)
# • evaluate(test_set)
# Implement models:
# • LinearRegressionModel- some different logic
# • DecisionTreeModel – some logic
# Show how a generic training loop works for any model without caring about details.

from abc import ABC, abstractmethod
class MLModel(ABC):
    @abstractmethod
    def train(self,data):
        pass
    @abstractmethod
    def predict(self,x):
        pass
    @abstractmethod
    def evaluate(self,test_set):
        pass
class LinearRegressionModel(MLModel):
    def train(self,data):
        print("Training Linear Regression")
    def predict(self,x):
        return 2*x + 1
    def evaluate(self,test_set):
        print("Evaluating Linear Regression")
class DecisionTreeModel(MLModel):
    def train(self,data):
        print("Training Decision Tree")
    def predict(self,x):
        if x>5:
            return "Class A"
        else:
            return "Class B"
    def evaluate(self,test_set):
        print("Evaluating Decision Tree")
models=[LinearRegressionModel(),DecisionTreeModel()]
for m in models:
    m.train("data")
    print("Prediction:", m.predict(3))
    m.evaluate("test")

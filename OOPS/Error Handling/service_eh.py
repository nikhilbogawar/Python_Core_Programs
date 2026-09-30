# • Create a class Service with a method that calls another method which raises an exception.
# Catch and handle the exception in the Service class.
class Service:
    def start(self):
        try:
            self.do_work()
        except Exception as e:
            print("Error handled:", e)
    def do_work(self):
        raise Exception("Something went wrong")
s = Service()
s.start()
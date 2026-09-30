# • Create a class Transaction with a method process() that
# uses try, except, and finally blocks to ensure a cleanup message is always printed.
class Transaction:
    def process(self):
        try:
            print("Processing transaction")
            raise Exception("Transaction failed")
        except Exception as e:
            print("Error:", e)
        finally:
            print("Cleanup completed")
t = Transaction()
t.process()
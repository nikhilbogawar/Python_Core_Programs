# Create three completely unrelated classes: PDFReport, ExcelSheet, and EmailMessage. Each has a method send().
# Write a function dispatch(item) that calls send() using duck typing.
# Prove that no inheritance is needed.
class PDFReport:
    def send(self):
        return "PDF Report sent"

class ExcelSheet:
    def send(self):
        return "Excel Sheet sent"

class EmailMessage:
    def send(self):
        return "Email Message sent"

def dispatch(item):
    print(item.send())

dispatch(PDFReport())
dispatch(ExcelSheet())
dispatch(EmailMessage())

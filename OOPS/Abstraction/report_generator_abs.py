# 15. Design a class ReportGenerator (abstract) with:
# • load_data()
# • process()
# • export()
# Implement:
# • PDFReport
# • ExcelReport
# Demonstrate how abstraction enforces a multi-step structure.

from abc import ABC, abstractmethod
class ReportGenerator(ABC):
    @abstractmethod
    def load_data(self):
        pass
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def export(self):
        pass
class PDFReport(ReportGenerator):
    def load_data(self):
        print("Loading PDF data")
    def process(self):
        print("Processing PDF data")
    def export(self):
        print("Exporting PDF")
class ExcelReport(ReportGenerator):
    def load_data(self):
        print("Loading Excel data")
    def process(self):
        print("Processing Excel data")
    def export(self):
        print("Exporting Excel")
r=[PDFReport(), ExcelReport()]
for i in r:
    i.load_data()
    i.process()
    i.export()

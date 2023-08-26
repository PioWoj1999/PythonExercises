
import abc

"""
Python example on defining interfaces. 
URL: https://realpython.com/python-interface/
"""

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    # abstract methods needs to be over ride by subclasses
    @abc.abstractmethod 
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError

class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print(f"Loading from path {path}, file: {file_name} ...")
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

def main(): 
    pdf_parser = PdfParserNew()
    pdf_parser.load_data_source(path="C:\System32", file_name="file.pdf")

    # check if class is a virtual subclass of interface - unit test case
    print(issubclass(PdfParserNew, FormalParserInterface))
    
    # error - class doesnt overrides the interface method that was required
    # email_parser = EmlParserNew()

if __name__ == "__main__":
    main()
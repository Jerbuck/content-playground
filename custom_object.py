import sys

username = None
password = None
base_url = None
objects = []

class CustomObject(object):
    """Data class for custom object."""

    def __init__(self):
        self.username = None
        self.password = None
        self.base_url = None
        self.objects = []

    def print(self):
        """Print the contents of the custom object."""
        print(f"\n--> Username: {self.username}")
        print(f"--> Password: {self.base_url}")
        print(f"--> Base URL: {self.base_url}")
        print(f"--> Objects: {self.objects}\n")

    def load(self, data):
        """Load the custom object from a dictionary."""
        try:
            self.username = data["username"]
            self.password = data["password"]
            self.base_url = data["base-url"]
            self.objects = data['objects']
            if (self.username == None) or \
                (self.password == None) or \
                (self.base_url == None) or \
                (self.objects == []):
                sys.Exit()
        except:
            print(f"\nERROR: Unable to parse data into custom object.")
            sys.exit()


if __name__ == '__main__':
    custom_object = CustomObject()
    custom_object.print()
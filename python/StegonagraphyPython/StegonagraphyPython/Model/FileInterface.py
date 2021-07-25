# /usr/env/python3.7

"""
FileInterface

Project goal:
Hide a file within a photo of the same size or less
Currently under Development
"""
me = '[FileInterface]'


class FileInterface:
    """
    Constructor for FileInterface
    """

    def __init__(self, fileName):
        self.fileName = fileName
        self.fd = None

    '''
    OpenFile
    Opens a file and turns into a File Descriptor
    '''

    def OpenFile(self, fileName=None):
        if fileName != None:
            self.fileName = fileName
            fd = open(fileName, 'r')
            self.fd = fd
            return fd
        else:
            return None

    '''
    FileToLines
    Turns a file into Lines
    '''

    def FileToLines(self) -> list[str]:
        if self.fileName is not None:
            fd = self.OpenFile(self.fileName)
            self.fd = fd
            array = []
            array = fd.readlines()
            return array
        else:
            return None

    '''
    FileToBytes
    Turns a file into a byte array
    '''

    def FileToBytes(self) -> bytes:
        array = []
        try:
            fd = open(self.fileName, 'rb')
        except OSError as err:
            if err > 0:
                print(me + 'ERROR> Error will robinson, Error')

        data = fd.read()
        fd.close()
        return data

    '''
    CloseFile
    closes a file descriptor
    '''

    def CloseFile(self) -> None:
        if self.fd > 0:
            self.fd.close()


'''
Below is example usage
'''
if __name__ == '__main__':
    pass

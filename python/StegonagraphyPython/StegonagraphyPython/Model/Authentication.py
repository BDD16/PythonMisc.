class ZeroKnowledgeServer:
    """
    ZeroKnowledgeServer is the Server for the exchange of tokens, then the actual algorithm of verification
    """

    pass


class ZeroKnowledgeClient:
    """
    ZeroKnowledgeClient Where the username and password will be passed into the client to then calculate the appropriate
    calculated values.
    """

    def __init__(self):
        pass

    pass


class Authentication(ZeroKnowledgeServer, ZeroKnowledgeClient):
    """
    Authentication class to have properties of both Server and Client.
    """

    def __init__(self):
        pass

    pass


class SecurePassword(str):
    """
    SecurePassword just contains a string with the ability to semi-securely delete from the RAM
    """

    def __init__(self, pwd_to_secure: str):
        super(SecurePassword, self)
        self.pwd = pwd_to_secure.encode()
        self.pwd = bytearray(self.pwd)
        del pwd_to_secure

    def delete(self) -> bool:
        result = False
        try:

            for i in range(0, len(self.pwd)):
                self.pwd[i] = ord("\x00")
            del self.pwd
            result = True

        except Exception as e:
            print(e)
            result = False

        return result


if __name__ == '__main__':
    x = SecurePassword('isthissecure')
    x.delete()

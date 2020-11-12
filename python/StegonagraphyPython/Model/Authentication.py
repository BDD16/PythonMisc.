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


class SecurePassword:
    """
    SecurePassword just contains a string with the ability to semi-securely delete from the RAM
    """
    def __init__(self, pwd_to_secure: str):
        self.pwd = pwd_to_secure

    def delete(self) -> bool:
        result = False
        try:
            for i in range(len(self.pwd)):
                self.pwd[i] = "\x00".encode()

            del self.pwd
            result = True

        except Exception as e:
            print(e)
            result = False

        return result

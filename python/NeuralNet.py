import numpy as np
import CryptoTools as crypt
import struct

'''
Completed: NO


This files and the files after it should be a neural net framework for
guessing learning an arbitrary amount of things to train image recognition all
the way to emulate a sha256 emulator

Note: come to find out the sha256 emulator is just snake oil...the error for this
type of learning is just too high due to the mathematically unpredictable setup of
sha256....I think.
'''

class NeuralNet():
    def __init__(self):
        self.x = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])#training example of parameters
        self.y = np.array([[0,1,1,0]]).T #training answers
        self.syn = 2*np.random.random((4000,31)) -1 #synaps0
        self.syn1 = 2*np.random.random((4000,4)) -1 #synapse1
        self.syn0 = None
        self.passwords = []
        self.hashofPasswords = []

    def GeneratePasswords(self, amount, bytelength):
        j = 0
        while j < amount:
            self.passwords.append(crypt.CryptoTools().RandomNumber(bytelength))
            j = j + 1
        j = 0
        while j < amount:
            self.passwords[j].strip()
            j = j + 1

    def HashPasswords(self):
        if len(self.passwords) > 0:
            i = 0
            while i < len(self.passwords):
                self.hashofPasswords.append(crypt.CryptoTools().Sha256(self.passwords[i]))
                i = i + 1


    def updateXFromHashes(self):
        self.x = []
        for j in xrange(len(self.hashofPasswords)):
            hash = self.hashofPasswords[j]
            hash = bytearray(hash)
            e0 = int(hash[0])
            e1 = int(hash[1])
            e2 = int(hash[2])
            e3 = int(hash[3])
            e4 = int(hash[4])
            e5 = int(hash[5])
            e6 = int(hash[6])
            e7 = int(hash[7])
            e8 = int(hash[8])
            e9 = int(hash[9])
            e10 = int(hash[10])
            e11 = int(hash[11])
            e12 = int(hash[12])
            e13 = int(hash[13])
            e14 = int(hash[14])
            e15 = int(hash[15])
            e16 = int(hash[16])
            e17 = int(hash[17])
            e18 = int(hash[18])
            e19 = int(hash[19])
            e20 = int(hash[20])
            e21 = int(hash[21])
            e22 = int(hash[22])
            e23 = int(hash[23])
            e24 = int(hash[24])
            e25 = int(hash[25])
            e26 = int(hash[26])
            e27 = int(hash[27])
            e28 = int(hash[28])
            e29 = int(hash[29])
            e30 = int(hash[30])
            e31 = int(hash[31])
            bigarray = np.array([e0, e1, e2, e3,e4,e5,e6,e7,e8,e9,e10,\
                                    e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,\
                                    e21,e22,e23,e24,e25,e26,e27,e28,e29,e30, e31], dtype=np.float128)
            self.x.append(bigarray)
        self.x = np.array(self.x, dtype=np.float128)
        #self.x = np.array(self.x, dtype=np.float128)


    def updateYFromPasswords(self):
        self.y = []
        for j in xrange(len(self.passwords)):
            pwd = self.passwords[j]
            one = struct.unpack('f',pwd[:4])
            two = struct.unpack('f',pwd[4:8])
            three = struct.unpack('f',pwd[8:])
            big = np.array([one, two, three], dtype=np.float)
            self.y.append(big)
        self.y = np.array(self.y).T


    def nonlin(self, x, deriv=False):
        if deriv == True:
            return (x * (1-x))
        else:
            return 1/(1+np.exp(-x.astype(float)))

    def Train(self,AmtOfPwds):
        self.syn0 = (255)*np.random.random((32,AmtOfPwds))
        self.syn1 = (255)*np.random.random((AmtOfPwds,3))
        #self.x = self.x[:]
        for j in xrange(100000):
            l0 = self.x
            l1 = self.nonlin(np.dot(l0,self.syn0))
            l2 = self.nonlin(np.dot(l1, self.syn1))
            #error amount we missed by actual value
            l2_error = self.y.T[:,:,0] - l2
            if j %100 == 0:
                print "iteration is: " + str(j)
                print "Error is: " + str(np.mean(np.absolute(l2_error)))

            l2_delta = np.dot(l2_error,self.nonlin(l2,deriv=True).T)
            l1_error = l2_delta.dot(self.syn1)
            l1_delta = np.dot(l1_error, self.nonlin(l1,deriv=True)[:3,:])


            self.syn1 = self.syn1 + l1.T.dot(l2_delta)[:,:3]

            self.syn0 = self.syn0 + l0.T.dot(l1_delta)
        print l2


if __name__ == '__main__':
    net = NeuralNet()
    net.GeneratePasswords(100,12)
    net.HashPasswords()
    net.updateXFromHashes()
    net.updateYFromPasswords()
    net.Train(100)
    print 'Completed but wow is that a saturated neuron'


    print net.syn

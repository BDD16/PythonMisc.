'''
CATI STIG defintions for Apple OSX 10.12 Sierra
Release: 3 Benchmark Date: 27 Apr 2018
'''

'''
imports to be used throught CATI
'''
import subprocess
import os
import sys
import shlex

#some constants
me = '[CAT-I]'

class CATI:

    def __init__(self):
        #initialize the class as neccessary
        #may need to make sure can run as a sudo
        #for now just do nothing
        self.initialized = True;

    '''
    STIG: AOSX-12-000050
    It is detrimental for operating systems to provide, or install by default,
    functionality exceeding requirements or mission objectives. These unnecessary
    capabilities or services are often overlooked and therefore may remain unsecured.
    They increase the risk to the platform by providing additional attack vectors.
    '''
    def AOSX_12_000050(self):
        result = False
        verification = '"com.apple.rshd" => true'
        cmd = '/usr/bin/sudo /bin/launchctl print-disabled system | /usr/bin/grep com.apple.rshd'
        fix = '/usr/bin/sudo /bin/launchctl disable system/com.apple.rshd'
        outputcheck = subprocess.check_output(shlex.split(cmd))

        print "output check>" + str(outputcheck)

        if not (verification in outputcheck):
            os.system(fix)
            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd != verification:
                print me + 'ERROR>unable to verify system check for AOSX_12_000050'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX_12_000050'
        else:
            print me + 'INFO>Verified AOSX_12_000050 is Satisfied'

        return result
    '''
    STIG: AOSX-12-000035
    Any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system.

    '''
    def AOSX_12_000035(self):
        result = False
        verification = '"com.openssh.sshd" => false'
        cmd = '/usr/bin/sudo /bin/launchctl print-disabled system | /usr/bin/grep com.openssh.sshd'
        fix = '/usr/bin/sudo /bin/launchctl enable system/com.openssh.sshd'
        outputcheck = subprocess.check_output(shlex.split(cmd))

        if not (verification in outputcheck):
            os.system(fix)
            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd != verification:
                print me + 'ERROR>unable to verify system check for AOSX_12_000035'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX_12_000035'
        else:
            print me + 'INFO>Verified AOSX_12_000035 is Satisfied'

        return result


    '''
    STIG: AOSX_12_000430
    Any changes to the hardware, software, and/or firmware components of the
    information system and/or application can potentially have significant effects
    on the overall security of the system.

    '''
    def AOSX_12_000430(self):
        result = False
        verification = ''
        cmd = ''
        fix = ''
        outputcheck = subprocess.check_output(shlex.split(cmd))

        if not (verification in outputcheck):
            os.system(fix)
            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd != verification:
                print me + 'ERROR>unable to verify system check for AOSX-12-000430'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX-12-000430'
        else:
            print me + 'INFO>Verified AOSX_12_000035 is Satisfied'

        return result


    '''
    STIG: AOSX-12-000605
    The "telnet" service must be disabled as it sends all data in a clear-text form
    that can be easily intercepted and read. The data needs to be protected at all
    times during transmission, and encryption is the standard method for protecting
    data in transit.
    '''
    def AOSX_12_000605(self):
        result = False
        verification = '"com.apple.telnetd" => true'
        cmd = '/usr/bin/sudo /bin/launchctl print-disabled system | /usr/bin/grep com.apple.telnetd'
        fix = '/usr/bin/sudo /bin/launchctl disable system/com.apple.telnetd'
        outputcheck = subprocess.check_output(shlex.split(cmd))

        if not (verification in outputcheck):
            os.system(fix)
            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd != verification:
                print me + 'ERROR>unable to verify system check for AOSX-12-000605'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX-12-000605'
        else:
            print me + 'INFO>Verified AOSX_12_000035 is Satisfied'

        return result

    '''
    STIG: AOSX-12-000606
    The "ftp" service must be disabled as it sends all data in a clear-text form
    that can be easily intercepted and read. The data needs to be protected at all
    times during transmission, and encryption is the standard method for protecting
    data in transit.
    '''
    def AOSX_12_000606(self):
        result = False
        verification = '"com.apple.ftpd" => true'
        cmd = '/usr/bin/sudo /bin/launchctl print-disabled system | /usr/bin/grep com.apple.ftpd'
        fix = '/usr/bin/sudo /bin/launchctl disable system/com.apple.ftpd'
        outputcheck = subprocess.check_output(shlex.split(cmd))

        if not (verification in outputcheck):
            os.system(fix)
            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd != verification:
                print me + 'ERROR>unable to verify system check for AOSX-12-000606'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX-12-000606'
        else:
            print me + 'INFO>Verified AOSX-12-000606 is Satisfied'

        return result

    '''
    STIG: AOSX-12-000995
    The "sudo" command must be configured to prompt for the administrator user's
    password at least once in each newly opened Terminal window or remote logon
    session, as this prevents a malicious user from taking advantage of an unlocked
    computer or an abandoned logon session to bypass the normal password prompt requirement.
    '''
    def AOSX_12_000995(self):
        result = False
        verification = 'tty_tickets'
        cmd = '/usr/bin/sudo /usr/bin/grep tty_tickets /etc/sudoers'
        fix = ''
        try:
            outputcheck = subprocess.check_output(shlex.split(cmd))
        except OSError as err:
            #didn't find anything
            outputcheck = None

        print str(outputcheck)
        if (outputcheck == None):
            #os.system(fix)
            fd = open('/etc/sudoers', 'a')
            fd.write('Defaults tty_tickets')
            fd.close()

            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd == verification:
                print me + 'ERROR>unable to verify system check for AOSX-12-000995'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX-12-000995'
        else:
            print me + 'INFO>Verified AOSX-12-000995 is Satisfied'

        return result

    '''
    STIG: AOSX-12-001465
    The OS X system must use a anti-virus program.

    '''
    def AOSX_12_001465(self):
        result = False
        verification = ''
        cmd = ''
        fix = ''
        outputcheck = subprocess.check_output(shlex.split(cmd))

        if not (verification in outputcheck):
            os.system(fix)
            #confirm everything was fixed
            confirmation = subprocess.check_output(shlex.split(cmd))
            if cmd != verification:
                print me + 'ERROR>unable to verify system check for AOSX-12-001465'
            else:
                result = True
                print me + 'INFO> verified and fixed system check for AOSX-12-001465'
        else:
            print me + 'INFO>Verified AOSX-12-001465 is Satisfied'

        return result

###-----------------------------------------------------------------------------
#
#CATI RUN ALL
#
###-----------------------------------------------------------------------------

    def CATI_RUNALL(self):
        self.AOSX_12_000050()
        self.AOSX_12_000035()
        #self.AOSX_12_000430()
        self.AOSX_12_000605()
        self.AOSX_12_000606()
        #self.AOSX_12_000995()
        self.AOSX_12_001465()

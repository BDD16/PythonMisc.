'''
CATII STIG defintions for Apple OSX 10.12 Sierra
Release: 3 Benchmark Date: 27 Apr 2018
'''

'''
imports to be used throught CATI
'''
import subprocess
import os
import sys

#some constants
me = '[CAT-II]'

'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_000050():
    verification = ''
    cmd = '/usr/sbin/system_profiler SPConfigurationProfileDataType | /usr/bin/grep "wvous-bl-corner = 0;"'
    cmd2 = '/usr/sbin/system_profiler SPConfigurationProfileDataType | /usr/bin/grep "wvous-tl-corner = 0;"'
    cmd3 = '/usr/sbin/system_profiler SPConfigurationProfileDataType | /usr/bin/grep "wvous-br-corner = 0;"'
    cmd4 = '/usr/sbin/system_profiler SPConfigurationProfileDataType | /usr/bin/grep "wvous-tr-corner = 0;"'
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck == verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX_12_000050'
        else:
            print me + 'INFO> verified and fixed system check for AOSX_12_000050'
    else:
        print me + 'INFO>Verified AOSX_12_000050 is Satisfied'

'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_000035():
    verification = ''
    cmd = ''
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck != verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX_12_000035'
        else:
            print me + 'INFO> verified and fixed system check for AOSX_12_000035'
    else:
        print me + 'INFO>Verified AOSX_12_000035 is Satisfied'


'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_000430():
    verification = ''
    cmd = ''
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck != verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX-12-000430'
        else:
            print me + 'INFO> verified and fixed system check for AOSX-12-000430'
    else:
        print me + 'INFO>Verified AOSX_12_000035 is Satisfied'


'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_000605():
    verification = ''
    cmd = ''
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck != verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX-12-000605'
        else:
            print me + 'INFO> verified and fixed system check for AOSX-12-000605'
    else:
        print me + 'INFO>Verified AOSX_12_000035 is Satisfied'


'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_000606():
    verification = ''
    cmd = ''
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck != verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX-12-000606'
        else:
            print me + 'INFO> verified and fixed system check for AOSX-12-000606'
    else:
        print me + 'INFO>Verified AOSX-12-000606 is Satisfied'


'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_000995():
    verification = ''
    cmd = ''
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck != verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX-12-000995'
        else:
            print me + 'INFO> verified and fixed system check for AOSX-12-000995'
    else:
        print me + 'INFO>Verified AOSX-12-000995 is Satisfied'


'''
STIG:
NOT IMPLEMENTED
'''
def AOSX_12_001465():
    verification = ''
    cmd = ''
    fix = ''
    outputcheck = subprocess.check_output(cmd, shell=True)

    if(outputcheck != verification):
        os.system(fix)
        #confirm everything was fixed
        confirmation = subprocess.checkoutput(cmd, shell=True)
        if cmd != verification:
            print me + 'ERROR>unable to verify system check for AOSX-12-001465'
        else:
            print me + 'INFO> verified and fixed system check for AOSX-12-001465'
    else:
        print me + 'INFO>Verified AOSX-12-001465 is Satisfied'

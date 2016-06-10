from cmd2 import Cmd, make_option, options
import subprocess
from  modules import *

prog = "python"

remote_script   =    " ./modules/remote.py"
source_script   =    " ./modules/source-scan.py"
trust_script    =    " ./modules/trust-scan.py"
crypto_script   =    " ./modules/crypto-checks.py"



#import cmd

class main(Cmd):
    """\n\n LAMMA : The Crypto-Auditing Framework\n\n"""

    prompt = 'prompt: '
    intro = """\n\n 
                                                       
                         __    _____ _____ _____ _____ 
                        |  |  |  _  |     |     |  _  |
                        |  |__|     | | | | | | |     |
                        |_____|__|__|_|_|_|_|_|_|__|__|
                                                      
                                    (BETA)


                Vulnerability Assessment and Auditing Framework 
                      for all the Crypto Implementations.


                           (An Open Source Project)

                                      by

                                SECURITY MONX
 
    \n\n"""

    prompt = 'LAMMA : '

    Cmd.colors = True

    Cmd.doc_header = """Welcome to LAMMA : \n
Primary Commands
----------------------------------------------

remote  -   module to test a remote server
crypto  -   module to test the quality of basic cryptographic schemes
source  -   module to find use of weak and deprecated cipher schemes in source code
trust   -   module to detect - insecure storage of private keys, un-trusted certificates


All commands supported by LAMMA Shell
---------------------------------------------
"""
    Cmd.misc_header = ""
    Cmd.undoc_header = """\n\nWant \'help\' or 'exit' LAMMA?
---------------------------------------------
"""

    def do_remote(self, line):
        """  Scans the remote host and reports the SSL/TLS configuration profile & applicable vulnerabilities\n
        """
        subprocess.call(prog + remote_script +" " + line, shell="false")


    def do_trust(self, line):
        """  Scans a given trust/key stores for -  untrusted certs, insecure private keys,\n
        """
        subprocess.call(prog + trust_script + " " + line, shell="false")


    def do_crypto(self, line):
        """  Generate keys, hashes, random number under various schemes for a given counts\n
        """
        subprocess.call(prog + crypto_script +" " + line, shell="false")



    def do_source(self, line):
        """  Scans the source code for known weak or backdoored functions\n
        """
        subprocess.call(prog + source_script +" " + line, shell="false")






pass    # Class Main Close


if __name__ == '__main__':
    main().cmdloop()


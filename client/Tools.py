import errno
import getopt
import os
import sys
import CommonVariables

def commandLineSetup():
    # récupération de la ligne de commande
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "f:d:",
                                   ["function",
                                    "database"])
    except:
        print("Error in command line")

    for opt, arg in opts:
        if opt in ['-f', '--function']:
            CommonVariables.Command_line['-f'] = arg

        if opt in ['-d', '--database']:
            CommonVariables.Command_line['-d'] = arg


def setupLOCALDATA():
    # verifier si le dossier LOCALdata existe
    try:
        os.makedirs(CommonVariables.ROOT_DIR + "/LOCALdata/")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
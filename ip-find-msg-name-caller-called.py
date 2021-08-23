from pathlib import Path
import re
import os
import time
import io
import csv
import codecs
import sys

opennewcopy = open('vm1.csv', mode='r')
readnewcopy = opennewcopy.read()

newresultdoc = open('Caller Filename Mailbox.txt', mode='w+')
phind = (re.findall('.+\n.+\n.+\n.+Put message.+', readnewcopy))
jointogether = '\n\n'.join(phind)
print(jointogether, file=newresultdoc)
newresultdoc.close()
opennewcopy.close()
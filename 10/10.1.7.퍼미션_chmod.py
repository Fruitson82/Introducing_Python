import os
import stat

os.chmod('oops.txt', stat.S_IRUSR)

import re
 
def valid(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{8,20}$"
    pat = re.compile(reg)               
    mat = re.search(pat, password)

    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

a=('Amiraliasd1')
valid(a) 
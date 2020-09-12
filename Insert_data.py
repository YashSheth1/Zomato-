import subprocess


"""
Example of running a sqlplus script from Python.
Works with Python 3 and 2.
"""

def run_sqlplus(sqlplus_script):

    """
    Run a sql command or group of commands against
    a database using sqlplus.
    """

    p = subprocess.Popen(['sqlplus','/nolog'],stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr) = p.communicate(sqlplus_script.encode('utf-8'))
    stdout_lines = stdout.decode('utf-8').split("\n")

    return stdout_lines
def insert(restaurant_name,locality,city,url):
    #name="address"
    # sqlplus_script="""
    # connect scott/tiger@orcl 
    # select """+name+""" from customer_deloitte; 
    # exit"""
    loc=locality.split(',')[0]+""""""
    print loc
    url=url.split('?')[0]+""""""
    sqlplus_script="""
    connect scott/tiger@orcl 
    insert into restaurants values (\'"""+city+"""\',\'"""+restaurant_name+"""\',\'"""+locality+"""\',\'"""+url+"""\');
    exit"""
    print sqlplus_script
    sqlplus_output = run_sqlplus(sqlplus_script)

    for line in sqlplus_output:
        print(line)


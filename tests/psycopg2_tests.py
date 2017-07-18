import psycopg2
import subprocess

connection = psycopg2.connect(
    database="test",
    user="sid",
    password="Blue8690",
    host="localhost",
    port="5432"
)

print connection.closed # 0

# restart the db externally
subprocess.check_call("sudo /etc/init.d/postgresql restart", shell=True)

# this query will fail because the db is no longer connected
try:
    cur = connection.cursor()
    cur.execute('SELECT 1')
except psycopg2.OperationalError:
    pass

print connection.closed # 2

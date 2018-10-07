from database import *
from webrequests import get_request

url_array = [
	"http://www.sqlitetutorial.net/sqlite-python/creating-database/",
	"https://stackoverflow.com/questions/2023893/python-3-get-http-page",
	"http://www.sqlitetutorial.net/sqlite-python/create-tables/"
]


def run():

	db_file = r'E:\\Coding\\Python\\Requests\\database\\test.db'

	conn = db_connect(db_file)

	sql_create_test_table = """
	
	CREATE TABLE TestTable (
	id integer PRIMARY KEY AUTOINCREMENT,
	excerpt varchar
	);
	
	"""

	if conn is not None:
		# create test table
		create_table(conn, sql_create_test_table)
		for url in url_array:
			request = get_request(url)
			request_str = (str(request)[:10],)
			insert_into_db(conn, request_str)
	else:
		print("Error! cannot create the database connection.")


if __name__ == '__main__':
	run()

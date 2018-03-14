import psycopg2
DBNAME = "news"

#three most popular articles of all time
query1 = "select title,view from article_view limit 3"

#most popular authors of all time
query2 = "select * from authors_view"

#days on which more than 1% of requests lead to errors
query3 = "select * from percenterror_view where Percent_Error >= 1"

query1_result = {}
query2_result = {}
query3_result = {}

query1_result['title'] = "The most popular three articles of all time are:\n"
query2_result['title'] = "The most popular article authors of all time are:\n"
query3_result['title'] = "The days on which more than 1% of requests lead to errors are:\n"


def get_result(query):
    """
    return result of the query
    """
    db = psycog2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def print_result(query_result):
    """
    prints the result of the query
    """
    print(query_result['title'])
    for result in query_result['results']:
        print(str(result[0])+'\t'+str(result[1]+'views'))
    print('\n')

def print_errorquery_result(query_result):
    """
    prints the result of the error query
    """
    print(query_result['title'])
    for result in query_result['results']:
        print(str(result[0])+'\t'+str(result[1]+'%'))
    print('\n')

#store results
query1_result['results'] = get_result(query1)
query2_result['results'] = get_result(query2)
query3_result['results'] = get_result(query3)

#print results
print_result(query1_result)
print_result(query2_result)
print_errorquery_result(query3_result)

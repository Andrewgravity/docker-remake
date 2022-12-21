

class Combiner:

    def __init__(self) -> None:
        pass

    def parse_data(self) -> str:
        global cursor
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json_data

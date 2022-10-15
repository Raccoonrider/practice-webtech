def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    query = environ['QUERY_STRING']
    print(query)
    body = "\n".join(x for x in query.strip('?').split("&"))
    start_response(status, headers)
    return [body]
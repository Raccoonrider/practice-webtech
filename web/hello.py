def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    query = environ['QUERY_STRING']
    print(query)
    body = "\n".join(query.strip('?').split("&"))
    start_response(status, headers)
    return body.encode('utf-8')
def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    print (environ.QUERY_STRING)
    body = ""
    start_response(status, headers)
    return [body]
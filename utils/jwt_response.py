def jwt_response_payload_handler(token, user=None, request=None):
    print(user)
    print(request)
    return {
        'token': token
    }

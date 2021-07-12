from replaceWordsInString.lambda_function import *

def api_gateway_event(strInput):
    return {
        "strToReplace": strInput
    }

def test_with_none_event():
    resp = lambda_handler(None, None)
    assert resp == {'statusCode': 400, 'body': 'Input string not provided.'}

def test_with_blank_string():
    event = api_gateway_event("")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 400, 'body': 'Input string not provided.'}

def test_non_existing_replacement_words():
    event = api_gateway_event("Hello Python")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'Hello Python'}

def test_google_replacement_words_in_string():
    event = api_gateway_event("We really like the new security features of Google Cloud")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'We really like the new security features of Google© Cloud'}

def test_oracle_replacement_words_in_string():
    event = api_gateway_event("We really like the new security features of Oracle Cloud")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'We really like the new security features of Oracle© Cloud'}

def test_microsoft_replacement_words_in_string():
    event = api_gateway_event("We really like the new security features of Microsoft Cloud")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'We really like the new security features of Microsoft© Cloud'}

def test_amazon_replacement_words_in_string():
    event = api_gateway_event("We really like the new security features of Amazon Cloud")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'We really like the new security features of Amazon© Cloud'}

def test_deloitte_replacement_words_in_string():
    event = api_gateway_event("We really like the new security features of Deloitte Cloud")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'We really like the new security features of Deloitte© Cloud'}

def test_google_in_lowercase_replacement_words_in_string():
    event = api_gateway_event("We really like the new security features of google Cloud")
    resp = lambda_handler(event, None)
    assert resp == {'statusCode': 200, 'body': 'We really like the new security features of google Cloud'}
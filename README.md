# replace_words
An API that will use a string as input and find and replace for certain words and outputs the result. 

For example: replace Google for Google©. 
Example input: 	“We really like the new security features of Google Cloud”. 
Expected output: 	“We really like the new security features of Google© Cloud”.

Following words will be replaced.
Oracle -> Oracle©
Google -> Google©
Microsoft -> Microsoft©
Amazon -> Amazon©
Deloitte -> Deloitte©

# Sample Request
curl --location --request POST 'https://35auuip4ug.execute-api.us-east-2.amazonaws.com/prod' \
--header 'Content-Type: application/json' \
--data-raw '{
  "strToReplace": "We really like the new security features of Amazon Cloud"
}'

# Sample Response
{
    "statusCode": 200,
    "body": "We really like the new security features of Amazon© Cloud"
}
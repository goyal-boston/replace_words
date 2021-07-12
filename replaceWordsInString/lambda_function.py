
def lambda_handler(event, context):
    """
    Find and replace following words and outputs the result.
    Oracle -> Oracle©
    Google -> Google©
    Microsoft -> Microsoft©
    Amazon -> Amazon©
    Deloitte -> Deloitte©

    Example input: 	“We really like the new security features of Google Cloud”. 
    Expected output: 	“We really like the new security features of Google© Cloud”.
    """
    # Return 400 if event is none or strToReplace is blank
    if not event or not event['strToReplace']:
        return {
            'statusCode': 400,
            'body': "Input string not provided."
        }

    # Input String
    replacementString = event['strToReplace']

    # Dictionary of words with replacement words
    wordsToReplaceDict = {'Oracle': 'Oracle©', 'Google': 'Google©', 'Microsoft': 'Microsoft©', 'Amazon': 'Amazon©', 'Deloitte': 'Deloitte©'}
    
    # Iterate over all key-value pairs in dictionary 
    for key, value in wordsToReplaceDict.items():
        # Replace words in string
        replacementString = replacementString.replace(key, value)
    
    return {
        'statusCode': 200,
        'body': replacementString
    }

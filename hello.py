def lambda_handler(event, context):

    print("Konichiwa AWS!, This is my first time creating Jenkins and shell Pipeline")
    print("event = {}".format(event))
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda using shell scripting!',
        
    }
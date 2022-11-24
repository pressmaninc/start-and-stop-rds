import boto3

region = 'xxxxxxxxxxx'

instance = 'xxxxxxx'
def lambda_handler(event, context):
    rds = boto3.client('rds', region_name=region)
    rds.start_db_instance(DBInstanceIdentifier=instance)
    print('started instance: ' + instance)
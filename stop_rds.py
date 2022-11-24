import boto3

region = 'xxxxxxxxxxx'

instance = 'xxxxxxx'
def lambda_handler(event, context):
    rds = boto3.client('rds', region_name=region)
    rds.stop_db_instance(DBInstanceIdentifier=instance)
    print('stoped instance: ' + instance)
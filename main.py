from readDataFromCSV import get_data
from stocksTemplate import send_stocks_credentials_mail

delegationData, numOfDelegates, numOfDelegations = get_data('delegation_test_data.csv')

print(f'{numOfDelegations} delegations in file.')
print(f'{numOfDelegates} delegates in file.')

for delegateIndex in range(numOfDelegates):
    print('====================================================================')
    print(f"Del Num: {delegationData['Del Num'][delegateIndex]}")
    print(f"Name: {delegationData['Name'][delegateIndex]}")
    print(f"Email: {delegationData['Email'][delegateIndex]}")
    print(f"School: {delegationData['School'][delegateIndex]}")
    print(f"Grade: {delegationData['Grade'][delegateIndex]}")
    print(f"Password: {delegationData['Password'][delegateIndex]}")
    print('====================================================================')
    send_stocks_credentials_mail(
        delNum=delegationData['Del Num'][delegateIndex],
        name=delegationData['Name'][delegateIndex],
        email=delegationData['Email'][delegateIndex],
        password=delegationData['Password'][delegateIndex],
    )
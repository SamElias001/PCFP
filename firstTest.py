expense_tracker_list = {}
totalamount = 0
id = 0
while True:
    id += 1
    
    description = input("Enter a description: ").upper()

    if description == '1':
        break

    amount = int(input("Enter an amount: "))

    totalamount += amount

    note = open('expense_tracker.txt')
    if note is not open:
        
    note.write(f"ID: {id}, Description: {description}, Amount: {amount}\n, Total Amount: {totalamount}\n")
    note.close()

    print(note.readlines())
    '''expense_tracker_list[id]=[{ 'Description': description, 'Amount': amount}]'''

'''for key, value in expense_tracker_list.items():
    print(f"ID: {key}, Description: {value[0]['Description']}, Amount: {value[0]['Amount']}")'''




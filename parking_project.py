#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = [i for i in range(1, total_tickets + 1)]
        self.parking_spaces = [i for i in range(1, total_parking_spaces + 1)]
        self.current_ticket = {}

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket[ticket_number] = {'paid': False, 'parking_space': parking_space}
            print(f"Ticket {ticket_number} issued. Parking space {parking_space} is assigned.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.current_ticket:
            amount = input("Enter the payment amount: ")
            if amount:
                self.current_ticket[ticket_number]['paid'] = True
                print("Your ticket has been paid. You have 15 minutes to leave.")
            else:
                print("Payment amount cannot be empty.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.current_ticket:
            if self.current_ticket[ticket_number]['paid']:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.current_ticket[ticket_number]['parking_space'])
                self.tickets.append(ticket_number)
                del self.current_ticket[ticket_number]
            else:
                print("Please pay for your parking first.")
        else:
            print("Invalid ticket number.")


parking_garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

while True:
    print("\n1. Take Ticket\n2. Pay for Parking\n3. Leave Garage\n4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        parking_garage.takeTicket()
    elif choice == '2':
        parking_garage.payForParking()
    elif choice == '3':
        parking_garage.leaveGarage()
    elif choice == '4':
        print("Thank you for using our parking garage. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:





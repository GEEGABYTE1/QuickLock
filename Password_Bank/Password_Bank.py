from os import system

class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link

    def update_value(self, new_value):
        self.value = new_value

class LinkedList:
    
    accounts = []
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_node(self, new_value):
        new_node = Node(new_value)
        self.accounts.append(new_node.get_value()[0])
        new_node.set_link(self.head_node)
        self.head_node = new_node

     



class Password:
    users = {}
    count = 0
    current_users_logged_in = 0
    def intro(self):
        print('Welcome to QuickLock; your personal password database!')
        print('Type n if you need to create an account')
        print('Type s if you already have an account ')
        
        
        init = False

        while init == False:
            print("There are currently {num} user(s) logged into the database! ".format(num=self.current_users_logged_in))
            print("--------------------------------------------------------------------------------------------------")
            print('You may now type in a command: ')

            prompt = input()

            if prompt == "n":
                password = input('Please type in a password: ')
                encrypted_pass = password.encode()
                self.real_pass =  encrypted_pass[:int(len(encrypted_pass) / 2)] 
                print('Your encryped password is now: {} '.format(self.real_pass))
                self.current_users_logged_in += 1
                clear = lambda: system('clear')
                clear()
                
                
                self.users[self.real_pass] = LinkedList()
                
                
                print(self.gameplay())
                init = True
            
            elif prompt == "s":
                checker = input('Please enter your password: ')
                encrypted_pass = checker.encode()
                self.real_pass_art =  encrypted_pass[:int(len(encrypted_pass) / 2)] 
                
                for i in self.users.keys():
                    if i == self.real_pass_art:
                        self.count += 1
                    else:
                        pass
                    
                if self.count >= 1:
                    
                    if self.real_pass_art == self.real_pass:
                        pass
                    else: 
                        self.current_users_logged_in += 1
                    print(self.gameplay())
                    init = True

                else:
                    print('That account does not seem to be in the database')
            
            else:
                print("Command is invalid")

        


    def gameplay(self):
        
        current_user = self.users.get(self.real_pass)
        print('Welcome to your password database!' )


        running = True
        while running:
            print('Type a to add a password')
            print('Type v to view a password')
            print('Type r to remove a password')
            print('Type u to update a password')
            print('Type g to view all your accounts in the database')
            print('Type /quit to quit the program! ')
            print('Type /switch to switch users')
            print('--------------------------------------------------')
            print('\n')
            user_prompt = input()

            if user_prompt == "a":
                account_user = input("Please type in a the name of the account (ex; Youtube, Facebook, etc): ")  
                password_acc = input("Please enter the password: ")
                clear = lambda: system('clear')
                clear()
                current_user.insert_node([account_user, password_acc])
            
            elif user_prompt == "v":
                view_acc = input('Please type in the account you want to see: ')

                current_node = current_user.get_head_node()

                if not view_acc in current_user.accounts:
                    print('That account is not valid ')
                    print('\n')
                    
                
                else:
                    while current_node:
                        if current_node.get_value() != None:
                            if current_node.get_value()[0] == view_acc:
                                print(current_node.get_value()[-1])
                                print('\n')
                                break 
                            else:
                                current_node = current_node.get_link()
            
            elif user_prompt == "/clear":
                clear = lambda: system('clear')
                clear()
            
            elif user_prompt == "r":
                remove_account = input('Please type in an account you want to remove: ')
                
                current_node = current_user.get_head_node()

                if not remove_account in current_user.accounts:
                    print('That user is not valid')
                    print('\n')
                else:
                    while current_node:
                        if current_node.get_value()[0] == remove_account:
                            current_node.update_value(None)
                            print('Account {} has been removed'.format(remove_account))
                            print('\n')
                            current_user.accounts.remove(remove_account)
                            break
                        else:
                            current_node = current_node.get_link()

            elif user_prompt == "g":
                current_node = current_user.get_head_node()

                if len(current_user.accounts) == 0:
                    print("There are no accounts in the database yet! ")
                    print("\n")
                
                else:
                    while current_node:
                        if current_node.get_value() != None:
                            print(current_node.get_value()[0])
                            print('\n')
                        current_node = current_node.get_link()
            
            
            elif user_prompt == "u":
                account_choose = input("Please enter the account you want to update: ")
                password = input('Please type in the new password: ')

                clear = lambda: system('clear')
                clear()

                current_node = current_user.get_head_node()

                if not account_choose in current_user.accounts:
                    print('That account is not valid ')
                    print('\n')
                
                else:

                    while current_node:
                        if current_node.get_value() != None:
                            if current_node.get_value()[0] == account_choose:
                                current_node.update_value([current_node.get_value()[0], password])
                                print('Account updated! ')
                                print('\n')
                                break 
                            current_node = current_node.get_link()

            elif user_prompt == "/quit":
                break
            
            elif user_prompt == "/switch":
                print(self.intro())
            
            else:
                print('Command is invalid! ')
                
        
            
            
            





test = Password()

test.intro()
test.gameplay()



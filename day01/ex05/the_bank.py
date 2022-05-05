import sys


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        if isinstance(account, Account):
            self.account.append(account)
            print("--Account [{}] ADDED--\n".format(account.name))
        else:
            print("--NO Account ADDED--\n")

    def find_account(self, account_identifier):
        for client in self.account:
            if isinstance(account_identifier, int):
                if client.id == account_identifier:
                    return client
            elif isinstance(account_identifier, str):
                if client.name == account_identifier:
                    return client
            else:
                print("Error: Find_account :must be int or str")
                break
        return None

    def transfer(self, origin, dest, amount):
        """
        @origin:    int(id) or str(name) of the first account
        @dest:      int(id) or str(name) of the destination account
        @amount:    float(amount) amount to transfer
        @return:    True if success, False if an error occured
        """
        print("--Transfer Processing--")
        client_origin = self.find_account(origin)
        client_dest = self.find_account(dest)
        if not client_origin:
            print("--Transfer Aborted : {} could not be found--"
                  .format(origin))
            return False
        if not client_dest:
            print("--Transfer Aborted : {} could not be found--"
                  .format(dest))
            return False
        if not isinstance(amount, float):
            print("--Transfer Aborted : amount must int or float--")
            return False
        if amount < 0:
            print("--Transfer Aborted: Amount must be > 0--")
            return False
        if self.is_corrupted(client_origin):
            print("--Transfer Aborted: Origin account is corrupted--")
            return False
        if self.is_corrupted(client_dest):
            print("--Transfer Aborted: Dest account is corrupted--")
            return False

        if amount > float(client_origin.value):
            print("\tTransfer Aborted : insufficient fund")
            return False
        client_origin.transfer(-amount)
        client_dest.transfer(amount)
        print("--Transfer from {} to {} Completed--\n"
              .format(client_origin.name, client_dest.name))
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if sucess, False if an error occured
        """
        print("--Fixing Account--")
        client_to_fix = self.find_account(account)
        if not client_to_fix:
            print("Error : {} could not be found".format(account))
            return False
        if not hasattr(client_to_fix, "name"):
            client_to_fix.name = "default_name"
        if not hasattr(client_to_fix, "id"):
            Accounnt.ID_COUNT += 1
            client_to_fix.id = Account.ID_COUNT
        if not hasattr(client_to_fix, "value"):
            setattr(client_to_fix, "value", 0)
            client_to_fix.transfer(0)

        attr_dict = client_to_fix.__dict__
        zip_addr = 0
        for attr_name in attr_dict:
            if attr_name.find("zip") == 0 or attr_name.find("addr") == 0:
                zip_addr = 1
            elif attr_name[0] == "b":
                setattr(client_to_fix, "_" + attr_name, attr_dict[attr_name])
                delattr(client_to_fix, attr_name)
        if not zip_addr:
            setattr(client_to_fix, "zipcode", "75001")

        if len(dir(client_to_fix)) % 2 == 0:
            client_to_fix._dummyattribute = "dummyattribute"
        print("--Account fixed--")
        return True

    def is_corrupted(self, account):
        """
            checks if account is corrupted
            corrupted =  :
            -even number of attributes
            -attribute start with 'b'
            -no attribute zip or addr
            -no attribute id, name and value
            Return False if safe, True if corrupted
        """
        check_dict = {"id": [True, "\t-No 'Id' attribute\n"],
                      "name": [True, "\t-No 'Name' atttribute\n"],
                      "value": [True, "\t-No 'Value' attribute\n"],
                      "addr": [True, "\t-No 'zip' or 'addr' not found\n"],
                      "even": [False, "\t-Even number of attributes\n"],
                      "b": [False, "\t-An Attribute starts with 'b'\n"]}
        attr = account.__dict__
        attr_count = 0
        for elem in attr:
            if elem == "id":
                check_dict["id"][0] = False
            if elem == "name":
                check_dict["name"][0] = False
            if elem == "value":
                check_dict["value"][0] = False
            if elem.find("zip") == 0 or elem.find("addr") == 0:
                check_dict["addr"][0] = False
            if elem[0] == 'b':
                check_dict["b"][0] = True
            attr_count += 1
        if attr_count % 2 == 0:
            check_dict["even"][0] = True
        ret = False
        err = "\tAccount Corrupted :\n"
        for key in check_dict:
            if check_dict[key][0] is True:
                ret = True
                err += check_dict[key][1]
        if ret is True:
            print(err)
        return ret

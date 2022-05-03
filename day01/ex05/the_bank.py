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
        print("--ADD ACCOUNT--")
        if self.check_account_safety(account):
            self.account.append(account)
            print("--Account ADDED--\n")
        else:
            print("--NO Account ADDED--\n")

    def transfer(self, origin, dest, amount):
        """
        @origin:    int(id) or str(name) of the first account
        @dest:      int(id) or str(name) of the destination account
        @amount:    float(amount) amount to transfer
        @return:    True if success, False if an error occured
        """
        print("--Transfer Processing--")
        ret = True
        if not isinstance(amount, float):
            print("\tError : amount must int or float")
            ret = False
        if amount < 0:
            print("\tError: Amount must be > 0")
            ret = False
        if not self.check_account_safety(origin):
            print("\tError: Origin account is corrupted")
            ret = False
        if not self.check_account_safety(dest):
            print("\tError: Dest account is corrupted")
            ret = False

        if amount > float(origin.value):
            print("\tError : Sender has insufficient fund for the transfer")
            ret = False
        if ret:
            origin.transfer(-amount)
            dest.transfer(amount)
            print("--Transfer Completed--\n")
        else:
            print("--Transfer Aborted--\n")
        return ret

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if sucess, False if an error occured
        """
        print("--Fixing Account--")
        ret = False
        if not isinstance(account, Account):
            print("\tError : object is not of type <Account>\n")
            return False
        if not hasattr(account, "name"):
            account.name = "default_name"
        if not hasattr(account, "id"):
            Accounnt.ID_COUNT += 1
            account.id = Account.ID_COUNT
        if not hasattr(account, "value"):
            setattr(account, "value", 0)
            account.transfer(0)

        attr_dict = account.__dict__
        zip_addr = 0
        for attr_name in attr_dict:
            if attr_name.find("zip") == 0 or attr_name.find("addr") == 0:
                zip_addr = 1
            elif attr_name[0] == "b":
                setattr(account, "_" + attr_name, attr_dict[attr_name])
                delattr(account, attr_name)
        if not zip_addr:
            setattr(account, "zipcode", "75001")

        if len(dir(account)) % 2 == 0:
            account._dummyattribute = "dummyattribute"
        print("--Account fixed--")
        return False

    def check_account_safety(self, account):
        """
            Checks full Account safety
            If not safe, tries to fix it
            True Account is safe or has been fixed, False corrupted
        """
        print("\t****Cheking Account Safety****")
        if not isinstance(account, Account):
            print("\tError : object is not of type <Account>\n")
            return False
        if self.is_corrupted(account):
            return False
        print("\t****Account Safe****")
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

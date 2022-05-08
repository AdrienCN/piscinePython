import copy


class CsvReader():

    def __init__(self, filename=None, sep=",",
                 header=False, skip_top=0, skip_bottom=0):

        self.open_ok = 0
        try:
            self.file = open(filename, "r")
        except Exception as msg:
            print("Error cannot open file '{}'".format(filename))
            return
        if sep == "":
            print("Error sep cannot be empty")
            return
        self.header = header
        self.file_header = None
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.sep = sep
        self.record_nb = 0
        self.field_nb = None
        self.data = []
        self.open_ok = 1

    def __enter__(self):

        if not self.open_ok:
            return None
        first_loop = 1
        count = 0
        for line in self.file.readlines():
            if first_loop:
                if self.header:
                    self.file_header = line.strip('\n')
                first_loop = 0
                self.field_nb = line.count(self.sep) + 1
            self.data.append((line.strip('\n')).split(self.sep))

            # Check absence de chaine vide
            for i in self.data[-1]:
                if len(i) <= 0:
                    self.data = None
                    return None
            if len(self.data[-1]) != self.field_nb:
                self.data = None
                return None
        self.record_nb = len(self.data)
        return self

    def __exit__(self, type, value, traceback):
        if value or traceback or type:
            print("Error caught: : {}".format(value, traceback.tb_frame))
        if self.open_ok:
            self.file.close()
        return True

    def getdata(self):
        """
            Retrieves the data/records from skip_top to skip bottom.
            Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        tmp_data = copy.deepcopy(self.data)
        tmp_top = self.skip_top
        tmp_bottom = self.skip_bottom
        tmp_record_nb = self.record_nb
        # remove le header de la liste
        if self.header:
            del tmp_data[0]

        if tmp_top > 0 or tmp_bottom > 0:
            while tmp_record_nb and tmp_top > 0:
                del tmp_data[0]
                tmp_record_nb -= 1
                tmp_top -= 1
            while tmp_record_nb and tmp_bottom > 0:
                del tmp_data[-1]
                tmp_record_nb -= 1
                tmp_bottom -= 1
        return tmp_data

    def getheader(self):
        """
            Retrieves the header from csv file.
            Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False)
        """
        if self.header is True:
            return self.file_header
        else:
            return None

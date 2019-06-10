import mssql


class SQL:
    def __init__(self):
        self.ms = mssql.MSSQL(host="localhost", user="", pwd="", db="airplane")

    def airplane_add(self, flight_no, to_c, from_c, plane_no, time_l, time_a):
        self.ms.ExecNonQuery("insert into airplane values ('%s','%s','%s','%s','%s','%s')" % (
            flight_no, to_c, from_c, plane_no, time_l, time_a))

    def passenger_add(self,ID,name,sex,tel,nationality):
        self.ms.ExecNonQuery("insert into passenger values ('%s','%s','%s','%s','%s')" % (
            ID,name,sex,tel,nationality))

    def collection_add(self,ID,flight_no,finish):
        self.ms.ExecNonQuery("insert into collection values ('%s','%s','%s')" % (
            ID,flight_no,finish))

    def reservation_add(self,ID,flight_no,seat_no):
        self.ms.ExecNonQuery("insert into reservation values ('%s','%s','%s')" % (
            ID,flight_no,seat_no))

    def seat_add(self,ID,seat_a,seat_b,seat_a_price,seat_b_price):
        self.ms.ExecNonQuery("insert into seat values ('%s','%s','%s','%s','%s')" % (
            ID,seat_a,seat_b,seat_a_price,seat_b_price))

    def bill_add(self,ID,price):
        self.ms.ExecNonQuery("insert into bill values ('%s','%s')" % (
            ID,price))

sql=SQL()
sql.airplane_add('a44','df','gf','44','2019-06-10 19:51:00.000','2019-06-10 19:51:00.000')
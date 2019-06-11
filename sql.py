import sql_m


class SQL:
    def __init__(self):
        self.ms = sql_m.SQL(host="127.0.0.1", user="root", pwd="wangdingyi110", db="airplane")

    def airplane_add(self, flight_no, to_c, from_c, plane_no, time_l, time_a):
        self.ms.ExecNonQuery("insert into airplane values ('%s','%s','%s','%s','%s','%s')" % (
            flight_no, to_c, from_c, plane_no, time_l, time_a))

    def passenger_add(self, ID, name, sex, tel, nationality):
        self.ms.ExecNonQuery("insert into passenger values ('%s','%s','%s','%s','%s')" % (
            ID, name, sex, tel, nationality))

    def collection_add(self, ID, flight_no, finish):
        self.ms.ExecNonQuery("insert into collection values ('%s','%s','%s')" % (
            ID, flight_no, finish))

    def reservation_add(self, ID, flight_no, seat_no):
        self.ms.ExecNonQuery("insert into reservation values ('%s','%s','%s')" % (
            ID, flight_no, seat_no))

    def seat_add(self, ID, seat_a, seat_b, seat_a_price, seat_b_price):
        self.ms.ExecNonQuery("insert into seat values ('%s','%s','%s','%s','%s')" % (
            ID, seat_a, seat_b, seat_a_price, seat_b_price))

    def bill_add(self, ID, price):
        self.ms.ExecNonQuery("insert into bill values ('%s','%s')" % (
            ID, price))

    def airplane_getAll(self):
        return self.ms.ExecQuery("SELECT * FROM airplane")

    def passenger_getAll(self):
        return self.ms.ExecQuery("SELECT * FROM passenger")

    def collection_getAll(self):
        return self.ms.ExecQuery("SELECT * FROM collection")

    def reservation_getAll(self):
        return self.ms.ExecQuery("SELECT * FROM reservation")

    def seat_getAll(self):
        return self.ms.ExecQuery("SELECT * FROM seat")

    def bill_getAll(self):
        return self.ms.ExecQuery("SELECT * FROM bill")


sql = SQL()
# sql.airplane_add('a44','df','gf','44','2019-06-10 19:51:00.000','2019-06-10 19:51:00.000')
# results = sql.airplane_getAll()
# for row in results:
#     fname = row[0]
#     lname = row[1]
#     age = row[2]
#     sex = row[3]
#     income = row[4]
#     adddd = row[5]
#     # 打印结果
#     print("fname=%s,lname=%s,age=%s,sex=%s,income=%s,addddd=%s" %
#           (fname, lname, age, sex, income, adddd))

import sql_m


class SQL:
    def __init__(self):
        self.ms = sql_m.SQL(host="127.0.0.1", user="root", pwd="wangdingyi110", db="airplane")

    def airplane_add(self, flight_no, to_c, from_c, plane_no, time_l, time_a):
        print(666666)
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

    def seat_add(self, flight_no, seat_a, seat_b, seat_a_price, seat_b_price):
        self.ms.ExecNonQuery("insert into seat values ('%s','%s','%s','%s','%s')" % (
            flight_no, seat_a, seat_b, seat_a_price, seat_b_price))

    def bill_add(self, ID, price, finish):
        self.ms.ExecNonQuery("insert into bill values ('%s','%s','%s')" % (
            ID, price, finish))

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

    def airplane_get(self, flight_no):
        return self.ms.ExecQuery("SELECT * FROM airplane WHERE flight_no='%s'" % flight_no)

    def passenger_get(self, ID):
        return self.ms.ExecQuery("SELECT * FROM passenger WHERE ID='%s'" % ID)

    def collection_get(self, ID):
        return self.ms.ExecQuery("SELECT * FROM collection WHERE ID='%s'" % ID)

    def reservation_get_backFlight_no(self, ID):
        return self.ms.ExecQuery("SELECT flight_no FROM reservation WHERE ID='%s'" % ID)

    def reservation_get_backFlight_no_seat(self, ID):
        return self.ms.ExecQuery("SELECT flight_no,seat_no FROM reservation WHERE ID='%s'" % ID)

    def seat_get(self, flight_no):
        return self.ms.ExecQuery("SELECT * FROM seat WHERE flight_no='%s'" % flight_no)

    def bill_get(self, ID):
        return self.ms.ExecQuery("SELECT * FROM bill WHERE ID='%s'" % ID)

    def save_seat(self, flight_no, seat_a, seat_b):
        return self.ms.ExecNonQuery(
            "UPDATE seat SET seat_a='%s',seat_b='%s' WHERE flight_no='%s'" % (seat_a, seat_b, flight_no))

    def del_flight(self, flight_no):
        return self.ms.ExecNonQuery("DELETE FROM airplane WHERE flight_no='%s'" % flight_no)

    def del_passenger(self, ID):
        return self.ms.ExecNonQuery("DELETE FROM passenger WHERE ID='%s'" % ID)

    def mod_flight(self, flight_no, to_c, from_c, plane_no, time_l, time_a):
        return self.ms.ExecNonQuery(
            "UPDATE airplane SET to_c='%s', from_c='%s', plane_no='%s', time_l='%s', time_a='%s' WHERE flight_no='%s'" % (
                to_c, from_c, plane_no, time_l, time_a, flight_no))

    def mod_passenger(self, ID, name, sex, tel, nationality):
        return self.ms.ExecNonQuery(
            "UPDATE passenger SET name='%s', sex='%s', tel='%s', nationality='%s' WHERE ID='%s'" % (
                name, sex, tel, nationality, ID))

    def mod_reservation(self, ID, flight_no,seat):
        return self.ms.ExecNonQuery("UPDATE reservation SET seat_no='%s' WHERE ID='%s' and flight_no='%s'" % (
            seat, ID,flight_no))

    def get_reservation_bill(self, ID):
        return self.ms.ExecQuery(
            "select sum(seat_a_price) from seat where flight_no in (select flight_no from reservation where ID='%s');" % ID)


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

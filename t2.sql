SELECT * FROM Hotel WHERE city = "New York";

SELECT name, city from hotels order by city;

--fuck 3
SELECT AVG(price) FROM rooms;

SELECT name.h1, date_from.b1, date_to.b1, room_no.b1 from hotel h1, booking b1 where name.h1 = "New York";


SELECT COUNT(DISTINCT guestNo) FROM Booking
WHERE (date_From <= to_Date("dd-mmm-yy", "01-SEP-99") AND date_To >= to_Date("dd-mmm-yy", "31-SEP-99")) OR
(date_From >= to_Date("dd-mmm-yy", "01-SEP-99") AND datefrom <= to_Date("dd-mmm-yy", "31-SEP-99"));

`

SELECT name.h1, room_no.r1 from hotel h1, room r1 where room_no NOT IN (select room_no from booking);
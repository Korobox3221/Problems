-- Keep a log of any SQL queries you execute as you solve the mystery.
--Descriptions from the crime scene at that day
SELECT description from crime_scene_reports where year = 2024 and month = 7 and day = 28 and street = 'Humphrey Street';
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
littering took place at 16:36. No known witnesses.

-- 16 hours license plates
SELECT license_plate  from bakery_security_logs where year = 2024 and month = 7 and day = 28 and  hour = 16;
+---------------+
| license_plate |
+---------------+
| WD5M8I6       |
| 4468KVT       |
| 207W38T       |
| C194752       |
+---------------+
-- Transcripts(use only bakery ones)
sselect transcript from interviews  where year = 2024 and month = 7 and day = 28;
1.Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

2.I don't know the thief's name, but it was someone I recognized.
Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |

3.As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchas.e the flight ticket.
--OUR GUY LICENSE PLATE
13FNH73
--name
select name from people where license_plate = '13FNH73';
 Sophia
--caller
select
select * from bakery_security_logs where year = 2024 and month = 7 and day = 28;
94KL13X       |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55
select name from people where license_plate = '6P58WS2' or license_plate ='4328GD8' or  license_plate = 'G412CB7' or license_plate ='L93JTIZ' or license_plate =  '322W7JE' or license_plate = '0NTHK55';
+--------+
|  name  |
+--------+
| Barry  |
| Iman   |
| Sofia  |
| Luca   |
| Diana  |
| Kelsey
select name,id from people where name = 'Diana or  name = 'Iman' or name = 'Sofia' or name = 'Barry' or name = 'Kelsey' or name = 'Luca';
+--------+
|   id   |
+--------+
| 243696 |
| 396669 |
| 398010 |
| 467400 |
| 514354 |
| 560886 |
+--------+
select account_number from bank_accounts where person_id = 243696 or person_id = 396669 or person_id =  398010 or person_id =  467400 or person_id = 514354 or person_id = 560886;

|  name  |   id   |
+--------+--------+
| Barry  | 243696 |
| Iman   | 396669 |
| Sofia  | 398010 |
| Luca   | 467400 |
| Diana  | 514354 |
| Kelsey | 560886 |

| person_id | account_number |
+-----------+----------------+
|DIANA: 514354    | 26013199       |
|IMAN: 396669    | 25506511       |
|LUCA: 467400    | 28500762       |
|BARRY: 243696    | 56171033
select account_number, transaction_type,amount from atm_transactions where year = 2024 and month = 7 and day = 28 and atm_location = 'Leggett Street' and account_number = 26013199
or account_number = 25506511 or account_number =  28500762 or account_number =  56171033;
LUCA: 28500762
IMAN:25506511
DIANA:26013199

sqlite> select caller from phone_calls where year = 2024 and month = 7 and day = 28 and duration <60;
+----------------+
|     caller     |
+----------------+
| (130) 555-0289 |
| (499) 555-9472 |
| (367) 555-5533 |
| (499) 555-9472 |
| (286) 555-6063 |
| (770) 555-1861 |
| (031) 555-6622 |
| (826) 555-1652 |
| (338) 555-6650 |
+----------------+

select name, phone_number from people where phone_number = '(725) 555-3243' or phone_number = '(770) 555-1861' or phone_number = '(031) 555-6622' or phone_number = '(826) 555-1652' or phone_number = '(338) 555-6650';
OUR guy is DIANA
Accomplice is Philip
--find airport
select id from airports  where city = 'Fiftyville';
Fiftyville city id is 8
select * from flights where origin_airport_id = 8 and year = 2024 and month = 7 and day = 29;

+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 18 | 8                 | 6                      | 2024 | 7     | 29  | 16   | 0      |
| 23 | 8                 | 11                     | 2024 | 7     | 29  | 12   | 15     |
| 36 | 8                 | 4                      | 2024 | 7     | 29  | 8    | 20     |
| 43 | 8                 | 1                      | 2024 | 7     | 29  | 9    | 30     |
| 53 | 8                 | 9                      | 2024 | 7     | 29  | 15   | 20

Eerliest time 8:20

dest id is 4

select city from airports where id = 4;

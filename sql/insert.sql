-- Active: 1670147479576@@127.0.0.1@3306@bwm
/* INSERT INTO customer
VALUES
	(NULL, ) */

INSERT INTO employee
VALUES
	(NULL, 'Eployee 1', 3000.00, 1000000, 'Leader', 'good', 'good', 'good', NULL),
	(NULL, 'Eployee 2', 2000.00, 1000001, 'BA', 'good', 'good', 'good', NULL),
	(NULL, 'Eployee 3', 2000.00, 1000002, 'BA', 'good', 'good', 'good', NULL),
	(NULL, 'Eployee 4', 1500.00, 1000003, 'Manager', 'good', 'good', 'good', NULL),
	(NULL, 'Eployee 5', 1000.00, 1000004, 'Designer', 'good', 'good', 'good', 1),
	(NULL, 'Eployee 6', 1000.00, 1000005, 'Designer', 'good', 'good', 'good', 2),
	(NULL, 'Eployee 7', 500.00, 1000006, 'Worker', 'good', 'good', 'good', NULL),
	(NULL, 'Eployee 8', 500.00, 1000007, 'Worker', 'good', 'good', 'good', NULL);

INSERT INTO customer
VALUES
	(NULL, '44 Riverside Street', '+86-222-233-4768', 'Juana Bonhomme', 2),
	(NULL, '3827 John Wall Pass', '+62-997-119-7586', 'Agnella Ferretti', 2),
	(NULL, '8 Melody Avenue', '+389-669-940-9891', 'Erny Clancy', 2),
	(NULL, '3079 Bayside Alley', '+230-223-720-8568', 'Alfie Olohan', 2),
	(NULL, '2 Green Ridge Street', '+86-385-503-5650', 'Maxim Ketteringham', 1),
	(NULL, '13 Glacier Hill Court', '+33-375-609-8862', 'Milicent Ure', 1),
	(NULL, '5218 Knutson Hill', '+62-744-990-0379', 'Ellette Itzik', 1),
	(NULL, '55 Hansons Pass', '+55-633-583-2927', 'Sissie Prettyjohns', 1);

INSERT INTO cusaccount
VALUES
	('employee_1', '1_employee', 1),
	('employee_2', '2_employee', 2),
	('employee_3', '3_employee', 3),
	('employee_4', '4_employee', 4),
	('employee_5', '5_employee', 5),
	('employee_6', '6_employee', 6),
	('employee_7', '7_employee', 7),
	('employee_8', '8_employee', 8);

INSERT INTO `order`
VALUES
	('C01', 75.00, '44 Riverside Street', 'full', 1, STR_TO_DATE('03/03/2021', '%d/%m/%Y'), 2),
	('C02', 80.00, '3827 John Wall Pass', 'partial', 2, STR_TO_DATE('03/04/2021', '%d/%m/%Y'), 2),
	('C03', 85.00, '8 Melody Avenue', 'full', 3, STR_TO_DATE('02/05/2021', '%d/%m/%Y'), 2),
	('C04', 76.00, '3079 Bayside Alley', 'partial', 4, STR_TO_DATE('08/11/2021', '%d/%m/%Y'), 2),
	('C05', 77.55, '2 Green Ridge Street', 'full', 5, STR_TO_DATE('07/12/2021', '%d/%m/%Y'), 1),
	('C06', 90.00, '13 Glacier Hill Court', 'partial', 6, STR_TO_DATE('01/01/2021', '%d/%m/%Y'), 1),
	('C07', 200.00, '5218 Knutson Hill', 'full', 7, STR_TO_DATE('02/09/2022', '%d/%m/%Y'), 1),
	('C08', 50.00, '55 Hansons Pass', 'partial', 8, STR_TO_DATE('07/01/2022', '%d/%m/%Y'), 1);

INSERT INTO project
VALUES
	(NULL, 'Demo Project', 1),
	(NULL, 'Final 1', 1),
	(NULL, 'Final 2', 1),
	(NULL, 'Final 3', 1),
	(NULL, 'Final 4', 1),
	(NULL, 'Final 5', 1),
	(NULL, 'Final 6', 1);

INSERT INTO `group`
VALUES
	(NULL, 'Group 1'),
	(NULL, 'Group 2');

INSERT INTO blueprint
VALUES
	(NULL, 'http://dummyimage.com/250x250.png/ff4444/ffffff', 'BLP1'),
	(NULL, 'http://dummyimage.com/250x250.png/ff4444/ffffff', 'BLP2'),
	(NULL, 'http://dummyimage.com/250x250.png/ff4444/ffffff', 'BLP3'),
	(NULL, 'http://dummyimage.com/250x250.png/ff4444/ffffff', 'BLP4'),
	(NULL, 'http://dummyimage.com/250x250.png/ff4444/ffffff', 'BLP5');

INSERT INTO car
VALUES
	(NULL, 200.0, 'black', 75000.00, 'http://dummyimage.com/250x250.png/cc0000/ffffff', 'VinFast', 2018, 'type1', 1, STR_TO_DATE('12/12/2017', '%d/%m/%Y'), 'complete', 1),
	(NULL, 250.0, 'red', 80000.00, 'http://dummyimage.com/250x250.png/cc0000/ffffff', 'BMW', 2021, 'type2', 2, STR_TO_DATE('12/02/2021', '%d/%m/%Y'), 'complete', 2),
	(NULL, 100.0, 'blue', 70000.00, 'http://dummyimage.com/250x250.png/cc0000/ffffff', 'Lambo', 2022, 'type3', 3, STR_TO_DATE('30/11/2022', '%d/%m/%Y'), 'in progress', 3),
	(NULL, 150.0, 'white', 70500.00, 'http://dummyimage.com/250x250.png/cc0000/ffffff', 'Gucci', 2019, 'type4', 4, STR_TO_DATE('07/07/2019', '%d/%m/%Y'), 'complete', 4),
	(NULL, 300.0, 'green', 90000.00, 'http://dummyimage.com/250x250.png/cc0000/ffffff', 'Zeus', 2022, 'type5', 5, STR_TO_DATE('07/12/2022', '%d/%m/%Y'), 'to do', 5);

INSERT INTO design_bp
VALUES
	(NULL, 1),
	(NULL, 2),
	(NULL, 3),
	(NULL, 4),
	(NULL, 5);

INSERT INTO  supplier
VALUES
	(NULL, '431058689103', '6 Division Terrace', 'Lefty Shatford', '1234567', 3),
	(NULL, '810975802594', '05845 Quincy Street', 'Joachim Cesco', '1234568', 4),
	(NULL, '542753151462', '855 Shopko Street', 'Terrill Goricke', '1234569', 5),
	(NULL, '258779196588', '73 Vahlen Trail', 'Darius Merrywether', '1234570', 6),
	(NULL, '870082589843', '298 Northridge Center', 'Kissie Bendik', '1234571', 7);

INSERT INTO component
VALUES
	(NULL, 20.0, 'Machine 1', 'machine', 'Component_1', 'http://dummyimage.com/250x250.png/dddddd/000000', 1, 3, STR_TO_DATE('01/01/2018', '%d/%m/%Y')),
	(NULL, 25.0, 'Interior 1', 'interior', 'Component_2', 'http://dummyimage.com/250x250.png/dddddd/000000', 1, 3, STR_TO_DATE('02/01/2018', '%d/%m/%Y')),
	(NULL, 30.0, 'Interior 2', 'interior', 'Component_3', 'http://dummyimage.com/250x250.png/dddddd/000000', 1, 3, STR_TO_DATE('31/12/2017', '%d/%m/%Y')),
	(NULL, 15.0, 'Machine 2', 'machine', 'Component_4', 'http://dummyimage.com/250x250.png/dddddd/000000', 4, 4, STR_TO_DATE('11/11/2021', '%d/%m/%Y')),
	(NULL, 15.0, 'Exterior 1', 'exterior', 'Component_4', 'http://dummyimage.com/250x250.png/dddddd/000000', 4, 4, STR_TO_DATE('21/11/2021', '%d/%m/%Y')),
	(NULL, 35.0, 'Machine 3', 'machine', 'Component_5', 'http://dummyimage.com/250x250.png/dddddd/000000', 5, 5, STR_TO_DATE('09/12/2021', '%d/%m/%Y')),
	(NULL, 35.0, 'Exterior 2', 'exterior', 'Component_5', 'http://dummyimage.com/250x250.png/dddddd/000000', 5, 5, STR_TO_DATE('10/12/2021', '%d/%m/%Y'));

INSERT INTO machine
VALUES
	(1, 'engine', 'oil', NULL),
	(4, 'brake', NULL, 'forceful'),
	(6, 'engine', 'gas', NULL);

INSERT INTO  interior
VALUES
	(2, 'climateControl', 'great', 'seat', 'red'),
	(3, 'Seat', 'great', 'seat', 'blue');

INSERT INTO exterior
VALUES
	(5, 'wheel', 'type1', 'black', NULL, NULL, NULL),
	(7, 'glass', NULL, NULL, 'silicat', '2', NULL);

INSERT INTO automatic_equippment
VALUES
	(NULL, 'type1', 'My house', 4, 1),
	(NULL, 'type2', 'My house', 4, 2),
	(NULL, 'type3', 'My house', 4, 1),
	(NULL, 'type4', 'My house', 4, 1),
	(NULL, 'type1', 'My house', 4, 5);

INSERT INTO eq_notify_ma
VALUES
	(4, 1),
	(4, 2),
	(4, 3),
	(4, 4);

INSERT INTO notify_message
VALUES
	(NULL, 'overheating', STR_TO_DATE('05/05/2018', '%d/%m/%Y')),
	(NULL, 'overheating', STR_TO_DATE('11/06/2019', '%d/%m/%Y')),
	(NULL, 'repairing', STR_TO_DATE('10/12/2020', '%d/%m/%Y')),
	(NULL, 'repairing', STR_TO_DATE('08/11/2021', '%d/%m/%Y')),
	(NULL, 'overheating', STR_TO_DATE('07/09/2022', '%d/%m/%Y'));

INSERT INTO `account`
VALUES
	('leader_1', 'Leader', 1),
	('BA_1', 'BA', 2),
	('BA_2', 'BA', 3),
	('manager_1', 'Manager', 4),
	('designer_1', 'Designer', 5),
	('designer_2', 'Designer', 6),
	('worker_1', 'Worker', 7),
	('worker_2', 'Worker', 8);

INSERT INTO task
VALUES
	('task_1', 'Do task 1', 1, 1, 1),
	('task_2', 'Do task 2', 1, 1, 1),
	('task_1', 'Do task 1', 2, 2, 1),
	('task_2', 'Do task 2', 3, 2, 1),
	('task_3', 'Do task 3', 5, 2, 1);
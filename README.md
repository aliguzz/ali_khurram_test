# ali_khurram_test
Ormuco test for interview

# SETUP
Activate VENV
source ./env/bin/activate
Flask Mysql db must be installed before use
https://flask-mysqldb.readthedocs.io/en/latest/
MySQL client must be installed and place database credentials in app.py to connect to database
I've pushed ali_khurram_test.sql file please import this file
--
-- Database: `ali_khurram_test`
-- --------------------------------------------------------
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_no` int(11) NOT NULL,
  `birth_date` date NOT NULL,
  `first_name` varchar(14) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `hire_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table `employees`

"Flask run" to run the web server

# Q1
Enter (X1,X2) (X3, X4) and click on check and see the lines overlapping
https://prnt.sc/p9dngl


# Q2
Enter (V1,V2) and click on check and see the versions greater, equal or less
https://prnt.sc/p9do5l


# Q3
Enter Search query like Shahab, Parto, Christian, Mary or anything you want and click on search
I have implemented LRU cache with expiration time of 20 seconds by default to optimize the latency time
when we press search button it searches from Cache first and if not found then it searches from the DB table
And shows both times (Database time and cache time)

# database latency time
https://prnt.sc/p9dq7q

# Cache latancy time
https://prnt.sc/p9drdu


# thanks for giving me the opportunity to taking part in the technical assessment process. Looking forward to meet Ormuco


Highridge Construction Company Payment System
===========================================

Submitted by: Abdullahi Mohamed Jibril
Submission Date: April 9, 2025

OVERVIEW
--------
This system generates weekly payment slips for 400+ construction workers, implementing all requirements from the Module 1 Assignment. Both Python and R versions are provided.

REQUIREMENTS
------------
- Python 3.x (for Python version)
- R (for R version)
- No additional libraries needed

FILES INCLUDED
--------------
1. payment_system.py - Main Python implementation
2. Payment_System.R - Alternative R implementation
3. README.txt - Documentation

PYTHON INSTRUCTIONS
-------------------
1. Run the script:
   python payment_system.py

2. Output:
   - Generates payment_slips.csv
   - Prints progress messages
   - Handles errors gracefully

R INSTRUCTIONS
--------------
1. Run the script:
   Rscript Payment_System.R

2. Output:
   - Generates payment_slips_r.csv
   - Shows status messages
   - Includes error handling

FEATURES
--------
- Generates 400+ worker records with:
  * Employee IDs
  * Random names/genders
  * Department assignments
  * Realistic hours (30-60)
  * Hourly rates ($15-$50)

- Calculates:
  * Base pay
  * Overtime (1.5x after 40 hours)
  * Employee levels:
    - A1 ($10,000-$20,000)
    - A5-F (Female $7,500-$30,000)
    - B2 (Default)

- Exports to CSV with:
  * Payment dates
  * All calculated fields
  * Error-free formatting

ERROR HANDLING
--------------
Both versions include:
- File operation protections
- Calculation safeguards
- Data generation checks
- Clear error messages

SAMPLE OUTPUT
-------------
employee_id,name,gender,department,hours_worked,hourly_rate,weekly_salary,employee_level,payment_date
EMP1001,John Smith,Male,Carpentry,45,25.50,1196.25,B2,2025-04-09
EMP1002,Mary Johnson,Female,Electrical,38,42.00,1596.00,A5-F,2025-04-09

NOTES
-----
- All data is randomly generated
- Output files are overwritten on each run
- System clock sets payment dates
- No personal data used






-------------------------------------------------------------------------------------------------------------------------------------
                                                          Thanks.

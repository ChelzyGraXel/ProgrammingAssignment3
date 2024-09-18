# Programming Assignment 3
### Problem 1: Cars Data Frame
#### STEP 1: Import the Pandas Library
Firstly, I have imported the pandas as pd to be able to access the Pandas library.
#### STEP 2: Load the .csv file into the Data Frame
As I try to use the syntax "pd.read_csv('cars.csv')", it displays that an error has occurred. Then, I suddenly remembered that the cars.csv file must be on the same folder as the Jupyter notebook. After moving the cars.csv file on the same folder of my Jupyter NB file, I successfully imported the data and have assigned it to a variable named "Cars_XLS_Worksheet".
#### STEP 3: Display the First Five Rows
By utilizing the syntax "Cars_XLS_Worksheet.head(5)", it directly displays the first five rows in the data frame.
#### STEP 4: Display the Last Five Rows
In displaying the last five rows of the data frame, it almost has the same syntax as what was used in printing the first five rows. However, instead of using ".head()", ".tail()" is used.

### Problem 2: Subsetting, Slicing, and Indexing
#### STEP 1: Import the Pandas Library
Firstly, I have imported the pandas as pd to be able to access the Pandas library.
#### STEP 2: Load the .csv file into the Data Frame
In order to load the .csv file into the Data Frame, the syntax "pd.read_csv('cars.csv')" has been utilized. After loading the data frame, it was assigned to variable named "cars".
#### STEP 3: Display the First Five Rows with Odd-numbered Columns
To be able to do this, the syntax "cars.iloc[1:10:2]" was used wherein "1:10" is reffering to index 1 until 10 (but not including index 10). Apart from that, ":2" is the step size of the selection of rows in order to only have an output of odd-numbered columns. The selected rows are assigned to a variable named "oddNumCol", then the output is printed by simply calling out the variable name.
#### STEP 4: Display the row that contains the ‘Model’ of ‘Mazda RX4’
The syntax "cars.loc[(cars['Model'])=='Mazda RX4']" was utilized. First, it locates the 'Mazda RX4' in the 'Model' column. After so, it is assigned to the variable named as "mazdaRX4". Then, "mazdaRX4" is printed.
#### STEP 5: Determine how many 'cyl' does 'Camaro Z28' have
The syntax used was "cars.loc[(cars['Model']=='Camaro Z28'),['cyl']]". The program firstly locate the 'Model' named 'Camaro Z38' just like what it did in the previous step. Then, it was specified to output the number of cylinders 'cyl'. The result was assigned to the variable named as "numOfCyl", then it was printed.
#### STEP 6: Determine the Number of Cylinder and Gear Type
There are many specifications asked in this part of the problem. It has been challenging to include more than one 'Model' in the output. After asking an advice from ChatGPT, it suggested me to use the syntax "cars.loc[(cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear'])]". The isin() function in pandas is used to filter data that returns a boolean data frame based on a given condition. After it successfully located the 'Models', it outputs the specified data such us 'cyl' and 'gear'. The results is assigned to variable "deets". After so, then, it was printed.

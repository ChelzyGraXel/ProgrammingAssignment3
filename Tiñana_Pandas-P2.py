{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1155a479-812c-4969-90fb-4c9fef64736d",
   "metadata": {},
   "source": [
    "# Experiment 3: Python Data Analysis (Pandas)\n",
    "#### Name: Chelzy Gracel Tiñana\n",
    "#### Section: 2ECE-D"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "735aaa37-5d77-4f6b-8a45-fb2c135a1924",
   "metadata": {},
   "source": [
    "### PROBLEM 2:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "604ef45f-bb15-42f6-9133-2e0ad1c56938",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the Pandas Library\n",
    "import pandas as pd\n",
    "\n",
    "# Read XLS worksheet file and load into a data frame\n",
    "cars = pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3703c24-dbf4-4819-bd4f-e26e18fa1764",
   "metadata": {},
   "source": [
    "#### A. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "acf62bdc-30f1-4353-ad89-9f074a8ab944",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>21.4</td>\n",
       "      <td>6</td>\n",
       "      <td>258.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.215</td>\n",
       "      <td>19.44</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Valiant</td>\n",
       "      <td>18.1</td>\n",
       "      <td>6</td>\n",
       "      <td>225.0</td>\n",
       "      <td>105</td>\n",
       "      <td>2.76</td>\n",
       "      <td>3.460</td>\n",
       "      <td>20.22</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Merc 240D</td>\n",
       "      <td>24.4</td>\n",
       "      <td>4</td>\n",
       "      <td>146.7</td>\n",
       "      <td>62</td>\n",
       "      <td>3.69</td>\n",
       "      <td>3.190</td>\n",
       "      <td>20.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Merc 280</td>\n",
       "      <td>19.2</td>\n",
       "      <td>6</td>\n",
       "      <td>167.6</td>\n",
       "      <td>123</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.440</td>\n",
       "      <td>18.30</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "1   Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
       "3  Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
       "5         Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3   \n",
       "7       Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4   \n",
       "9        Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4   \n",
       "\n",
       "   carb  \n",
       "1     4  \n",
       "3     1  \n",
       "5     1  \n",
       "7     2  \n",
       "9     4  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Display the first five rows with odd-numbered columns\n",
    "oddNumCol = cars.iloc[1:10:2]\n",
    "oddNumCol"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "970f2da6-d0a0-44ef-aa72-21e09e5d46cf",
   "metadata": {},
   "source": [
    "#### B. Display the row that contains the ‘Model’ of ‘Mazda RX4’."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "8608d473-b152-489f-8c2d-9e9b92fd55fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Display the row that contain the Model of Mazda RX4\n",
    "mazdaRX4 = cars.loc[(cars['Model'])=='Mazda RX4']\n",
    "mazdaRX4"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29465534-2ccf-463b-8148-0773828e8646",
   "metadata": {},
   "source": [
    "#### C. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "cacb5230-67bb-4061-84db-a8c91d33006c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl\n",
       "23    8"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Determine how many cylinders does the car model 'Camaro Z28' have\n",
    "numOfCyl = cars.loc[(cars['Model']=='Camaro Z28'),['cyl']]\n",
    "numOfCyl"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "238a777b-1f3e-4d3e-920d-1dc0b8ebbd6a",
   "metadata": {},
   "source": [
    "#### D. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "6928419a-14c6-41eb-a099-7caa629dd029",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "deets = cars.loc[(cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear'])]\n",
    "deets"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

# check-point5
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9014a7c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a1edd377",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\bechi\\anaconda3\\lib\\site-packages (1.2.4)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from pandas) (2.8.1)\n",
      "Requirement already satisfied: numpy>=1.16.5 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from pandas) (1.20.1)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from pandas) (2021.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "48c43b68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: seaborn in c:\\users\\bechi\\anaconda3\\lib\\site-packages (0.11.1)\n",
      "Requirement already satisfied: numpy>=1.15 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from seaborn) (1.20.1)\n",
      "Requirement already satisfied: pandas>=0.23 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from seaborn) (1.2.4)\n",
      "Requirement already satisfied: matplotlib>=2.2 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from seaborn) (3.3.4)\n",
      "Requirement already satisfied: scipy>=1.0 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from seaborn) (1.6.2)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from matplotlib>=2.2->seaborn) (8.2.0)\n",
      "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from matplotlib>=2.2->seaborn) (2.4.7)\n",
      "Requirement already satisfied: python-dateutil>=2.1 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from matplotlib>=2.2->seaborn) (2.8.1)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from matplotlib>=2.2->seaborn) (1.3.1)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from matplotlib>=2.2->seaborn) (0.10.0)\n",
      "Requirement already satisfied: six in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from cycler>=0.10->matplotlib>=2.2->seaborn) (1.15.0)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from pandas>=0.23->seaborn) (2021.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "04b79575",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: scikit-learn in c:\\users\\bechi\\anaconda3\\lib\\site-packages (0.24.1)\n",
      "Requirement already satisfied: scipy>=0.19.1 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from scikit-learn) (1.6.2)\n",
      "Requirement already satisfied: joblib>=0.11 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from scikit-learn) (1.0.1)\n",
      "Requirement already satisfied: numpy>=1.13.3 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from scikit-learn) (1.20.1)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\bechi\\anaconda3\\lib\\site-packages (from scikit-learn) (2.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f5689652",
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>343</td>\n",
       "      <td>No</td>\n",
       "      <td>2</td>\n",
       "      <td>Collander, Mr. Erik Gustaf</td>\n",
       "      <td>male</td>\n",
       "      <td>28.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>248740</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>76</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Moen, Mr. Sigurd Hansen</td>\n",
       "      <td>male</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>348123</td>\n",
       "      <td>7.6500</td>\n",
       "      <td>F G73</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>641</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Jensen, Mr. Hans Peder</td>\n",
       "      <td>male</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>350050</td>\n",
       "      <td>7.8542</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>568</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Palsson, Mrs. Nils (Alma Cornelia Berglund)</td>\n",
       "      <td>female</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>349909</td>\n",
       "      <td>21.0750</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>672</td>\n",
       "      <td>No</td>\n",
       "      <td>1</td>\n",
       "      <td>Davidson, Mr. Thornton</td>\n",
       "      <td>male</td>\n",
       "      <td>31.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>F.C. 12750</td>\n",
       "      <td>52.0000</td>\n",
       "      <td>B71</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId Survived  Pclass                                         Name  \\\n",
       "0          343       No       2                   Collander, Mr. Erik Gustaf   \n",
       "1           76       No       3                      Moen, Mr. Sigurd Hansen   \n",
       "2          641       No       3                       Jensen, Mr. Hans Peder   \n",
       "3          568       No       3  Palsson, Mrs. Nils (Alma Cornelia Berglund)   \n",
       "4          672       No       1                       Davidson, Mr. Thornton   \n",
       "\n",
       "      Sex   Age  SibSp  Parch      Ticket     Fare  Cabin Embarked  \n",
       "0    male  28.0      0      0      248740  13.0000    NaN        S  \n",
       "1    male  25.0      0      0      348123   7.6500  F G73        S  \n",
       "2    male  20.0      0      0      350050   7.8542    NaN        S  \n",
       "3  female  29.0      0      4      349909  21.0750    NaN        S  \n",
       "4    male  31.0      1      0  F.C. 12750  52.0000    B71        S  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#load data\n",
    "import pandas as pd\n",
    "titanic_data=pd.read_excel('titanic-passengers (1).xlsx')\n",
    "titanic_data.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4e7120d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',\n",
       "       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "33f21037",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    object \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          714 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Cabin        204 non-null    object \n",
      " 11  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(4), object(6)\n",
      "memory usage: 83.7+ KB\n"
     ]
    }
   ],
   "source": [
    "titanic_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "45dbc307",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      int64\n",
       "Survived        object\n",
       "Pclass           int64\n",
       "Name            object\n",
       "Sex             object\n",
       "Age            float64\n",
       "SibSp            int64\n",
       "Parch            int64\n",
       "Ticket          object\n",
       "Fare           float64\n",
       "Cabin           object\n",
       "Embarked        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ff2c87ab",
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
       "      <th>PassengerId</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>257.353842</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>14.526497</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>223.500000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>20.125000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.500000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId      Pclass         Age       SibSp       Parch        Fare\n",
       "count   891.000000  891.000000  714.000000  891.000000  891.000000  891.000000\n",
       "mean    446.000000    2.308642   29.699118    0.523008    0.381594   32.204208\n",
       "std     257.353842    0.836071   14.526497    1.102743    0.806057   49.693429\n",
       "min       1.000000    1.000000    0.420000    0.000000    0.000000    0.000000\n",
       "25%     223.500000    2.000000   20.125000    0.000000    0.000000    7.910400\n",
       "50%     446.000000    3.000000   28.000000    0.000000    0.000000   14.454200\n",
       "75%     668.500000    3.000000   38.000000    1.000000    0.000000   31.000000\n",
       "max     891.000000    3.000000   80.000000    8.000000    6.000000  512.329200"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d4558846",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age            177\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "Cabin          687\n",
       "Embarked         2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "34bbdae4",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c3e8bd6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data['Age'].isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "092ac328",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic_data.drop('Cabin',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "394228ff",
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>343</td>\n",
       "      <td>No</td>\n",
       "      <td>2</td>\n",
       "      <td>Collander, Mr. Erik Gustaf</td>\n",
       "      <td>male</td>\n",
       "      <td>28.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>248740</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>76</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Moen, Mr. Sigurd Hansen</td>\n",
       "      <td>male</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>348123</td>\n",
       "      <td>7.6500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>641</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Jensen, Mr. Hans Peder</td>\n",
       "      <td>male</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>350050</td>\n",
       "      <td>7.8542</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>568</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Palsson, Mrs. Nils (Alma Cornelia Berglund)</td>\n",
       "      <td>female</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>349909</td>\n",
       "      <td>21.0750</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>672</td>\n",
       "      <td>No</td>\n",
       "      <td>1</td>\n",
       "      <td>Davidson, Mr. Thornton</td>\n",
       "      <td>male</td>\n",
       "      <td>31.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>F.C. 12750</td>\n",
       "      <td>52.0000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId Survived  Pclass                                         Name  \\\n",
       "0          343       No       2                   Collander, Mr. Erik Gustaf   \n",
       "1           76       No       3                      Moen, Mr. Sigurd Hansen   \n",
       "2          641       No       3                       Jensen, Mr. Hans Peder   \n",
       "3          568       No       3  Palsson, Mrs. Nils (Alma Cornelia Berglund)   \n",
       "4          672       No       1                       Davidson, Mr. Thornton   \n",
       "\n",
       "      Sex   Age  SibSp  Parch      Ticket     Fare Embarked  \n",
       "0    male  28.0      0      0      248740  13.0000        S  \n",
       "1    male  25.0      0      0      348123   7.6500        S  \n",
       "2    male  20.0      0      0      350050   7.8542        S  \n",
       "3  female  29.0      0      4      349909  21.0750        S  \n",
       "4    male  31.0      1      0  F.C. 12750  52.0000        S  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1cc6215b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 11 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    object \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          891 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(4), object(5)\n",
      "memory usage: 76.7+ KB\n"
     ]
    }
   ],
   "source": [
    "titanic_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2709a893",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      int64\n",
       "Survived        object\n",
       "Pclass           int64\n",
       "Name            object\n",
       "Sex             object\n",
       "Age            float64\n",
       "SibSp            int64\n",
       "Parch            int64\n",
       "Ticket          object\n",
       "Fare           float64\n",
       "Embarked        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "70b6a2ea",
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>343</td>\n",
       "      <td>No</td>\n",
       "      <td>2</td>\n",
       "      <td>Collander, Mr. Erik Gustaf</td>\n",
       "      <td>male</td>\n",
       "      <td>28.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>248740</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>76</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Moen, Mr. Sigurd Hansen</td>\n",
       "      <td>male</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>348123</td>\n",
       "      <td>7.6500</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>641</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Jensen, Mr. Hans Peder</td>\n",
       "      <td>male</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>350050</td>\n",
       "      <td>7.8542</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>568</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Palsson, Mrs. Nils (Alma Cornelia Berglund)</td>\n",
       "      <td>female</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>349909</td>\n",
       "      <td>21.0750</td>\n",
       "      <td>S</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>672</td>\n",
       "      <td>No</td>\n",
       "      <td>1</td>\n",
       "      <td>Davidson, Mr. Thornton</td>\n",
       "      <td>male</td>\n",
       "      <td>31.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>F.C. 12750</td>\n",
       "      <td>52.0000</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId Survived  Pclass                                         Name  \\\n",
       "0          343       No       2                   Collander, Mr. Erik Gustaf   \n",
       "1           76       No       3                      Moen, Mr. Sigurd Hansen   \n",
       "2          641       No       3                       Jensen, Mr. Hans Peder   \n",
       "3          568       No       3  Palsson, Mrs. Nils (Alma Cornelia Berglund)   \n",
       "4          672       No       1                       Davidson, Mr. Thornton   \n",
       "\n",
       "      Sex   Age  SibSp  Parch      Ticket     Fare Embarked  Gender  \n",
       "0    male  28.0      0      0      248740  13.0000        S       1  \n",
       "1    male  25.0      0      0      348123   7.6500        S       1  \n",
       "2    male  20.0      0      0      350050   7.8542        S       1  \n",
       "3  female  29.0      0      4      349909  21.0750        S       0  \n",
       "4    male  31.0      1      0  F.C. 12750  52.0000        S       1  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#convert sex column to numerical values\n",
    "gender=pd.get_dummies(titanic_data['Sex'],drop_first=True)\n",
    "titanic_data['Gender']=gender\n",
    "titanic_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cbb05078",
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>343</td>\n",
       "      <td>No</td>\n",
       "      <td>2</td>\n",
       "      <td>28.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>76</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.6500</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>641</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.8542</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>568</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>21.0750</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>672</td>\n",
       "      <td>No</td>\n",
       "      <td>1</td>\n",
       "      <td>31.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>52.0000</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId Survived  Pclass   Age  SibSp  Parch     Fare  Gender\n",
       "0          343       No       2  28.0      0      0  13.0000       1\n",
       "1           76       No       3  25.0      0      0   7.6500       1\n",
       "2          641       No       3  20.0      0      0   7.8542       1\n",
       "3          568       No       3  29.0      0      4  21.0750       0\n",
       "4          672       No       1  31.0      1      0  52.0000       1"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#drop the columns which are not required\n",
    "titanic_data.drop(['Name','Sex','Ticket','Embarked'],axis=1,inplace=True)\n",
    "titanic_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1e08c4fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       No\n",
       "1       No\n",
       "2       No\n",
       "3       No\n",
       "4       No\n",
       "      ... \n",
       "886    Yes\n",
       "887     No\n",
       "888     No\n",
       "889     No\n",
       "890    Yes\n",
       "Name: Survived, Length: 891, dtype: object"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Seperate Dependent and Independent variables\n",
    "x=titanic_data[['PassengerId','Pclass','Age','SibSp','Parch','Fare','Gender']]\n",
    "y=titanic_data['Survived']\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9e95aac0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import train test split method\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2b4930c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#train test split\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "76de035d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import Logistic  Regression\n",
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "39c4dfaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy=0.78\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\bechi\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:763: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    }
   ],
   "source": [
    "#Fit  Logistic Regression \n",
    "lr=LogisticRegression()\n",
    "lr.fit(x_train,y_train)\n",
    "predict=lr.predict(x_test)\n",
    "print(\"Accuracy={:.2f}\".format(lr.score(x_test, y_test)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5a217a8",
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b0cac55a",
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
       "      <th>Predicted No</th>\n",
       "      <th>Predicted Yes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Actual No</th>\n",
       "      <td>150</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Actual Yes</th>\n",
       "      <td>37</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Predicted No  Predicted Yes\n",
       "Actual No            150             29\n",
       "Actual Yes            37             79"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print confusion matrix \n",
    "from sklearn.metrics import confusion_matrix\n",
    "pd.DataFrame(confusion_matrix(y_test,predict),columns=['Predicted No','Predicted Yes'],index=['Actual No','Actual Yes'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2bb0a455",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "          No       0.80      0.84      0.82       179\n",
      "         Yes       0.73      0.68      0.71       116\n",
      "\n",
      "    accuracy                           0.78       295\n",
      "   macro avg       0.77      0.76      0.76       295\n",
      "weighted avg       0.77      0.78      0.77       295\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report\n",
    "print(classification_report(y_test,predict))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5f0b2693",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Predicted', ylabel='Actual'>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "confusion_matrix = pd.crosstab(y_test,predict , rownames=['Actual'], colnames=['Predicted'])\n",
    "sns.heatmap(confusion_matrix, annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b39ad86f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import make_classification\n",
    "import numpy as np\n",
    "x, y = make_classification(n_samples=2000, n_classes=2, n_features=10, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "bda05c86",
   "metadata": {},
   "outputs": [],
   "source": [
    "random_state = np.random.RandomState(0)\n",
    "n_samples, n_features = x.shape\n",
    "x = np.c_[x, random_state.randn(n_samples, 200 * n_features)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b9472b6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e15d6fd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.naive_bayes import GaussianNB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "d97316a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(max_features=5, n_estimators=500)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf = RandomForestClassifier(max_features=5, n_estimators=500)\n",
    "rf.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "3d0d02e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB()"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nb = GaussianNB()\n",
    "nb.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "8fdbd8ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Prediction probabilities \n",
    "r_probs = [0 for _ in range(len(y_test))]\n",
    "rf_probs = rf.predict_proba(x_test)\n",
    "nb_probs = nb.predict_proba(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a69ee773",
   "metadata": {},
   "outputs": [],
   "source": [
    "rf_probs = rf_probs[:, 1]\n",
    "nb_probs = nb_probs[:, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "3ebf342d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# AUROC and ROC curve values\n",
    "from sklearn.metrics import roc_curve, roc_auc_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "1ceeb4e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Calculate AUROC\n",
    "r_auc = roc_auc_score(y_test, r_probs)\n",
    "rf_auc = roc_auc_score(y_test, rf_probs)\n",
    "nb_auc = roc_auc_score(y_test, nb_probs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "06e5a590",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random (chance) Prediction: AUROC = 0.500\n",
      "Random Forest: AUROC = 0.872\n",
      "Naive Bayes: AUROC = 0.864\n"
     ]
    }
   ],
   "source": [
    "print('Random (chance) Prediction: AUROC = %.3f' % (r_auc))\n",
    "print('Random Forest: AUROC = %.3f' % (rf_auc))\n",
    "print('Naive Bayes: AUROC = %.3f' % (nb_auc))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1757aafc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Calculate ROC curve\n",
    "r_fpr, r_tpr, _ = roc_curve(y_test, r_probs)\n",
    "rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_probs)\n",
    "nb_fpr, nb_tpr, _ = roc_curve(y_test, nb_probs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dc202e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.plot(r_fpr, r_tpr, linestyle='--', label='Random prediction (AUROC = %0.3f)' % r_auc)\n",
    "plt.plot(rf_fpr, rf_tpr, marker='.', label='Random Forest (AUROC = %0.3f)' % rf_auc)\n",
    "plt.plot(nb_fpr, nb_tpr, marker='.', label='Naive Bayes (AUROC = %0.3f)' % nb_auc)\n",
    "\n",
    "# Title\n",
    "plt.title('ROC Plot')\n",
    "# Axis labels\n",
    "plt.xlabel('False Positive Rate')\n",
    "plt.ylabel('True Positive Rate')\n",
    "# Show legend\n",
    "plt.legend() # \n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b05ad37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_excel('article.xlsx',skiprows = [0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
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
       "      <th>Unnamed: 0</th>\n",
       "      <th>ArticleId</th>\n",
       "      <th>ArticleName</th>\n",
       "      <th>M_L_C</th>\n",
       "      <th>Shoe Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>603</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2779</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1636</td>\n",
       "      <td>10 MIX 2ND GRADE STOCK</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3388</td>\n",
       "      <td>1059 DARK BLUE</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3389</td>\n",
       "      <td>1059 TAN</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0  ArticleId             ArticleName M_L_C Shoe Type\n",
       "0         NaN        603                  10 MIX     M    SANDAL\n",
       "1         NaN       2779                  10 MIX     M    SANDAL\n",
       "2         NaN       1636  10 MIX 2ND GRADE STOCK     M    SANDAL\n",
       "3         NaN       3388          1059 DARK BLUE     L      SHOE\n",
       "4         NaN       3389                1059 TAN     L      SHOE"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4979, 5)"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
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
       "      <th>Unnamed: 0</th>\n",
       "      <th>ArticleId</th>\n",
       "      <th>ArticleName</th>\n",
       "      <th>M_L_C</th>\n",
       "      <th>Shoe Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>603</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2779</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1636</td>\n",
       "      <td>10 MIX 2ND GRADE STOCK</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3388</td>\n",
       "      <td>1059 DARK BLUE</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3389</td>\n",
       "      <td>1059 TAN</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0  ArticleId             ArticleName M_L_C Shoe Type\n",
       "0         NaN        603                  10 MIX     M    SANDAL\n",
       "1         NaN       2779                  10 MIX     M    SANDAL\n",
       "2         NaN       1636  10 MIX 2ND GRADE STOCK     M    SANDAL\n",
       "3         NaN       3388          1059 DARK BLUE     L      SHOE\n",
       "4         NaN       3389                1059 TAN     L      SHOE"
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.iloc[:,1:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
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
       "      <th>ArticleId</th>\n",
       "      <th>ArticleName</th>\n",
       "      <th>M_L_C</th>\n",
       "      <th>Shoe Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>603</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2779</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1636</td>\n",
       "      <td>10 MIX 2ND GRADE STOCK</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3388</td>\n",
       "      <td>1059 DARK BLUE</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3389</td>\n",
       "      <td>1059 TAN</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ArticleId             ArticleName M_L_C Shoe Type\n",
       "0        603                  10 MIX     M    SANDAL\n",
       "1       2779                  10 MIX     M    SANDAL\n",
       "2       1636  10 MIX 2ND GRADE STOCK     M    SANDAL\n",
       "3       3388          1059 DARK BLUE     L      SHOE\n",
       "4       3389                1059 TAN     L      SHOE"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Shoe Type\n",
       "BOOT       1014\n",
       "ND           25\n",
       "SANDAL      307\n",
       "SHOE       2872\n",
       "SLIPPER     761\n",
       "Name: Shoe Type, dtype: int64"
      ]
     },
     "execution_count": 218,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Shoe Type')['Shoe Type'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "def helper(row):\n",
    "    try:\n",
    "        row['Model'] = row['ArticleName'].split(' ')[0]\n",
    "    except AttributeError:\n",
    "        row['Model'] = row['ArticleName']\n",
    "    return row\n",
    "df = df.apply(helper,axis='columns')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4979, 5)"
      ]
     },
     "execution_count": 228,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
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
       "      <th>ArticleId</th>\n",
       "      <th>ArticleName</th>\n",
       "      <th>M_L_C</th>\n",
       "      <th>Shoe Type</th>\n",
       "      <th>Model</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>603</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2779</td>\n",
       "      <td>10 MIX</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1636</td>\n",
       "      <td>10 MIX 2ND GRADE STOCK</td>\n",
       "      <td>M</td>\n",
       "      <td>SANDAL</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3388</td>\n",
       "      <td>1059 DARK BLUE</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "      <td>1059</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3389</td>\n",
       "      <td>1059 TAN</td>\n",
       "      <td>L</td>\n",
       "      <td>SHOE</td>\n",
       "      <td>1059</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ArticleId             ArticleName M_L_C Shoe Type Model\n",
       "0        603                  10 MIX     M    SANDAL    10\n",
       "1       2779                  10 MIX     M    SANDAL    10\n",
       "2       1636  10 MIX 2ND GRADE STOCK     M    SANDAL    10\n",
       "3       3388          1059 DARK BLUE     L      SHOE  1059\n",
       "4       3389                1059 TAN     L      SHOE  1059"
      ]
     },
     "execution_count": 235,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['10', '1059', '10988', '11', '1118/117', '1138/108', '12',\n",
       "       '1280/121', '12803', '12803/118', '13', '14', '15', '15120',\n",
       "       '15247', '15339', '15426', '15430', '15431', '15509', '15553',\n",
       "       '15862', '16', '16089', '16187', '16189', '16496', '17', '17073',\n",
       "       '1753/115', '1785/115', '18', '1841/115', '1843/115', '19', '20',\n",
       "       '2031/115', '2033/115', '204/116', '2055/117', '206/116',\n",
       "       '2070/117', '2084/115', '21', '2107/115', '2112/115', '2122/115',\n",
       "       '2199/118', '22', '23', '2309/109', '2312/108', '2314/108',\n",
       "       '2325/108', '2327/115', '2328/115', '2333/115', '2334/115',\n",
       "       '2337/115', '2349/115', '236/116', '237/116', '24', '2489/115',\n",
       "       '2490/115', '25', '2511/115', '2577/115', 2578, '26', '2623/118',\n",
       "       '2651/115', '27', '2712/115', '2717/115', '2718/115', '2719/115',\n",
       "       '2721/115', '2722/115', '2723/115', '2724/115', '2728/115',\n",
       "       '2738/115', '2739/115', '2755(53590)', '2756(53747)', '28',\n",
       "       '2804/117', '29', '2924', '2926/112', '2983/108', '2984/110', '30',\n",
       "       '3072/118', '3098/111', '3098/117', '31', '3136/116', '3144'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Model'].unique()[0:100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "metadata": {},
   "outputs": [],
   "source": [
    "def helper(row):\n",
    "    try:\n",
    "        \n",
    "        row['Final'] = re.split(r\"[^a-zA-Z0-9\\s]\", row['Model'])[0]\n",
    "    except:\n",
    "        row['Final'] = row['Model']\n",
    "    return row\n",
    "df = df.apply(helper,axis = 'columns')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {},
   "outputs": [],
   "source": [
    "boot = df[df['Shoe Type'] == 'BOOT']\n",
    "sandal = df[df['Shoe Type'] == 'SANDAL']\n",
    "shoe = df[df['Shoe Type'] == 'SHOE']\n",
    "slipper = df[df['Shoe Type'] == 'SLIPPER']\n",
    "nd = df[df['Shoe Type'] == 'ND']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "metadata": {},
   "outputs": [],
   "source": [
    "boot_list = list(boot['Final'])\n",
    "sandal_list = list(sandal['Final'])\n",
    "shoe_list = list(shoe['Final'])\n",
    "slipper_list = list(slipper['Final'])\n",
    "nd_list = list(nd['Final'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1014"
      ]
     },
     "execution_count": 272,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 266,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "65124\n",
      "65124\n",
      "65124\n",
      "65124\n",
      "65124\n",
      "65124\n",
      "65124\n",
      "65862\n",
      "65862\n",
      "65862\n",
      "65862\n",
      "65862\n",
      "65862\n",
      "65862\n",
      "61829\n",
      "61829\n",
      "61829\n",
      "61829\n",
      "61829\n",
      "61829\n",
      "61829\n",
      "64953\n",
      "64953\n",
      "64953\n",
      "64953\n",
      "64953\n",
      "64953\n",
      "64953\n"
     ]
    }
   ],
   "source": [
    "import os \n",
    "import shutil\n",
    "folderName = 'Global'\n",
    "if __name__ == \"__main__\": \n",
    "    for (root,dirs,files) in os.walk('Global', topdown=True):\n",
    "        for i in files:\n",
    "            if(i=='.DS_Store'):\n",
    "                pass\n",
    "            else:\n",
    "                completePath = os.path.join(root,i)\n",
    "                temp = i.split(' ')[0]\n",
    "                print(temp)\n",
    "                if(temp in boot_list):\n",
    "                    original = completePath\n",
    "                    target = 'globalCheck/boot/' + i\n",
    "                    shutil.copyfile(original, target)\n",
    "                elif(temp in sandal_list):\n",
    "                    original = completePath\n",
    "                    target = 'globalCheck/sandal/' + i\n",
    "                    shutil.copyfile(original, target)\n",
    "                elif(temp in shoe_list):\n",
    "                    original = completePath\n",
    "                    target = 'globalCheck/shoe/' + i\n",
    "                    shutil.copyfile(original, target)\n",
    "                elif(temp in slipper_list):\n",
    "                    original = completePath\n",
    "                    target = 'globalCheck/slipper/' + i\n",
    "                    shutil.copyfile(original, target)\n",
    "                elif(temp in nd_list):\n",
    "                    original = completePath\n",
    "                    target = 'globalCheck/nd/' + i\n",
    "                    shutil.copyfile(original, target)\n",
    "                \n",
    "                    \n",
    "                    \n",
    "                \n",
    "                \n",
    "                    \n",
    "                    \n",
    "                    \n",
    "                    \n",
    "#             if(i=='.DS_Store'):\n",
    "#                 pass\n",
    "#             else:\n",
    "#                 completePath = os.path.join(root,i)\n",
    "#                 if('RIGHT' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/RIGHT/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('PAIR' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/PAIR/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('SOLE' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/SOLE/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('CLOSE' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/CLOSE/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('LEFT' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/LEFT/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "\n",
    "#                 if('MAIN REVERT' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/MAIN-REVERT/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('MAIN' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/MAIN/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "                \n",
    "#                 if('SIDE BACK' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/SIDE-BACK/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('BACK' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/BACK/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "#                 elif('SIDE' in i.upper()):\n",
    "#                     original = completePath\n",
    "#                     target = 'globalCheck/SIDE/' + i\n",
    "#                     shutil.copyfile(original, target)\n",
    "                    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

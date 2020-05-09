#final bikesharae

#test for bikeshare

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',  
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    cities = ('chicago', 'new york city', 'washington')
    while True:
            city = input('Which of these cities do you want to explore : Chicago, New York City, or Washington? \n> ').lower()
            if city in cities:
                print('Thanks for choosing this city')
                break
            else:
                print('That city is not in the data set please try again')
    

# get user input for month (all, january, february, ... , june)
    months = ('january', 'february', 'march', 'april', 'may', 'june','all')
    while True:
            month = input('Which month do you want to explore? \n> You can select any month from January to June, or you can choose all \n> ').lower()
            if month in months:
                print('Thanks for choosing this month(s)')
                break
            else:
                print('That month is not in the data set please try again')

# get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    while True:
            day = input('Which day do you want to explore? You can also select all \n> ').lower()
            if day in days:
                print('Thanks for choosing this day(s)')
                break
            else:
                print('That day is not in the data set please try again')
                

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The returned month is the month digit, as in 1 = January, 2 = February, etc')
    print('The most common month was', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day was', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The returned hour is in military time')
    print('The most common hour was', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station was', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station was', popular_end_station)



# display most frequent combination of start station and end station trip
    frequent_combo = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start and end station was \n>', frequent_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print('The total travel time value is in days')
    print('Total travel time:', int(total_duration/86400))

    # display mean travel time
    average_trip_duration = df["Trip Duration"].mean()
    print('The average travel time value is in minutes')
    print('Average travel time:', int(average_trip_duration/60))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        print('No Gender data')
    


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('The earliest birth year:', str(int(min_birth_year)))
        print('The most recent birth year:',str(int(max_birth_year)))
        print('The most common birth year:',str(int(common_birth_year)))

    else:
        print('No birth year data')

    

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        #return at least 5 rows of information
        raw = input('\nWould you like to see 5 rows from the data?\nPlease enter yes or no\n').lower()
        if raw in ('yes'):
            i = 0
            
            while True:
                print(df.iloc[i:i+5])
                i += 5
        
                add_five = input('Would you like to see 5 more rows of data?\nPlease enter yes or no:\n ').lower()
                if add_five not in ('yes'):
                    break

        #asks user if they want to restart
        restart = input('\nWould you like to restart? Enter yes or no. \n> ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


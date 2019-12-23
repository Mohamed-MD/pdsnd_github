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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input('Which city would like to filter by (chicago, new york city, washington) ? ')
        if city.lower() not in ['chicago', 'new york city', 'washington']:
            print ('sorry try again')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input("which month would you like to filter by? (january, february, ... , june) or all : ")
        if month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("Sorry try again")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Are you looking for a particler day or all days ? (all or any day) : ")
        if day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            print("Sorry try again")
            continue
        else:
            break
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    
    # TO DO: display the most common month
    popular_month =df['month'].mode()[0]
    print("Most common month: ", popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day : ", popular_day )
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour : ", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station: ", Start_Station)
    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print("Most commonly end station: " , End_Station)
    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station','End Station']).count()
    print("Most commonly used combination of start station and end station trip: ", Start_Station, " & ", End_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print("Total travel time: ", Total_Travel_Time/86400, " Day")
    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("Mean travel time: ", Mean_Travel_Time/60 ," Minutes")
                                     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types: ", user_types)
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender types:\n', gender_types)
    except KeyError:
      print("\nGender types:\nNo data available for this month.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('Earliest year:', Earliest_Year)
    except KeyError:
      print("Earliest year: No data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('Most recent year: ', Most_Recent_Year)
    except KeyError:
      print("Most recent year: No data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('Most common year: ', Most_Common_Year)
    except KeyError:
      print("Most common year: No data available for this month.")

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

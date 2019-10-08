from timetable import TimeTable

timetable1 = TimeTable()
timetable2 = TimeTable()

timetable1.monday = ["7 to 12" , "13 to 15", "16 to 18"]
timetable2.monday = ["8 to 10" , "14 to 16" , "17 to 18"]

NUMBER_OF_HOURS = 11
hour_taken_array = []

# initialize hour_taken_array to zeros
for one_hour_period in range(NUMBER_OF_HOURS):
    hour_taken_array.append(0)




hours_string_prompt = ""

for hour in range(7,19):
    hours_string_prompt = hours_string_prompt + str(hour) + "\t"


# split the scheduled periods to one hour periods
def split_into_one_hour_components( day_schedule ):
    
    # arrays to store the one hour periods
    schedule_time_pairs = []

    for schedule in day_schedule:
        # first split into given hours
        timeScheduleList = schedule.split()
        startHour = int( timeScheduleList[0])
        finishHour = int( timeScheduleList[-1])

        if finishHour - startHour > 1:
            # need to create new strings
            lesson_length = finishHour - startHour
            this_hour = startHour
            for hour in range(lesson_length):

                next_hour = this_hour + 1
                new_schedule_time = str(this_hour) + " to " + str(next_hour) #create a new hour string
                schedule_time_pairs.append(new_schedule_time)

                this_hour = next_hour
        else:
            schedule_time_pairs.append(schedule)


    for time_pair in schedule_time_pairs:
        print(time_pair)

    return schedule_time_pairs



def map_one_hour_slots_to_hour_taken_array( scheduled_one_hour_time):
    
    mappings = {
            "7 to 8" : 0,
            "8 to 9" : 1,
            "9 to 10" : 2,
            "10 to 11" : 3,
            "11 to 12" : 4,
            "12 to 13" : 5,
            "13 to 14" : 6,
            "14 to 15" : 7,
            "15 to 16" : 8,
            "16 to 17" : 9,
            "17 to 18" : 10,
            }

    for one_hour_period in scheduled_one_hour_time:

       index_in_hours_taken_array = mappings.get( one_hour_period , "Invalid hour")
       hour_taken_array[ index_in_hours_taken_array ] = 1

    print(hour_taken_array)


def print_a_timetable_to_the_terminal():

    print( hours_string_prompt)
    shade = ""
    for hour_taken in hour_taken_array:

        if hour_taken == 1:
            shade+=("|" * 8)

        else:
            shade+="\t"
    print( shade)
    print( shade)
    print( shade)
    print( shade)

list_of_one_hour_slots_2 = split_into_one_hour_components(timetable2.monday)
list_of_one_hour_slots_1 = split_into_one_hour_components(timetable1.monday)
map_one_hour_slots_to_hour_taken_array( list_of_one_hour_slots_1)
map_one_hour_slots_to_hour_taken_array( list_of_one_hour_slots_2)
print_a_timetable_to_the_terminal()

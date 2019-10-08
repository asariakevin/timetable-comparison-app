from timetable import TimeTable

timetable1 = TimeTable()
timetable2 = TimeTable()

timetable1.monday = ["7 to 12" , "13 to 15", "16 to 18"]
timetable2.monday = ["8 to 10" , "14 to 16" , "17 to 18"]




def split_into_one_hour_components( day_schedule ):

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

    for time_pair in schedule_time_pairs:
        print(time_pair)

        # if the difference between the second hour and first is greater
        # than one , split 
        # split by adding one to the first hour and come up with a new pair
        # the second element of the new pair , is again used to make a new pair
        # this is done until the 'second hour is reached'

        # this will be a new array

        # check if the elements correspond to a certain when clause 
        # if so update the class taken array as required

split_into_one_hour_components(timetable1.monday)

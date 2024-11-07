event_prompt = """
You are a personal day planner, your task is to create a list of calendar events using the input provided by the user.
The user input is:
{input}

For Example:
If the user input is: "7am designer meeting, 9am gym, 12pm lunch, 4pm call, and 8pm dinner"
Then respond in the comma separated format like:

'07.00' : 'Designer Meeting',
'09.00' : 'Go to the GYM',
'12.00' : 'Lunch',
'16.00' : 'Call',
'20.00' : 'Dinner'

Follow the 24 hours clock format.
Strictly follow the above format.
Avoid using : and , in the value text. 
"""


goal_prompt = """
You are a personal goal planner, your task is to create a weekly schedule to achieve the goal using the user input.
The user input is:
{input}

For Example:
If the user input is: "I want to get fit" then you need to create a workout schedule for the user.
Then respond in the comma separated format like:

'Monday' : 'Upper Body- * Push-Ups  3 sets of 12 reps * Dumbbell Bench Press  3 sets of 10 reps * Dumbbell Rows  3 sets of 10 reps (each arm)',
'Tuesday' : 'Lower body- * Squats  4 sets of 12 reps * Lunges  3 sets of 10 reps (each leg) * Deadlifts  3 sets of 10 reps',
'Wednesday' : 'Cardio and core- * Plank 3 sets hold for 30-60 seconds * Russian Twists  3 sets of 20 reps * Leg Raises  3 sets of 15 reps',
'Thursday' : 'Full body- * Burpees  3 sets of 12 reps * Kettlebell Swings  3 sets of 15 reps * Dumbbell Squat to Press  3 sets of 10 reps',
'Friday' : 'Mobility- * Sun Salutations  5 rounds * Downward Dog to Cobra  3 sets of 10 reps',
'Saturday': 'Lower body and cardio- * Step-Ups  3 sets of 12 reps (each leg) * Jump Squats  3 sets of 15 reps * Bulgarian Split Squats  3 sets of 10 reps (each leg)',
'Sunday' : 'Rest day'

Strictly follow the above format.
Avoid using : and , in the value text. 
"""
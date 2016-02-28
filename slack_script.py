from slacker import Slacker
import random
import copy

slack = Slacker('xoxp-3567316862-3567316864-23450718850-8b8763e5b2')

user_names = ['ohad', 'idonave', 'ido', 'itai', 'alon', 'joel', 'ron',
              'eitan',  'matan', 'mathias', 'kevin']
DUTY_COUNT = 'duty_count'

class DutiesScheduler(object):


    def __init__(self, user_names, num_of_people_in_duty = 1):
        users = {}
        for user_name in user_names:
            users[user_name] = {DUTY_COUNT: 0, 'been_with': []}

        self.users = users
        self.num_of_people_in_duty = num_of_people_in_duty

    def random_bunch(self):
        self.duplicated_temp_list = copy.deepcopy(self.users.keys())
        self.duplicated_temp_list += self.find_missed_users()
        selected_groups = []
        while len(self.duplicated_temp_list) >= self.num_of_people_in_duty:
            random_group = self.select_a_random_group()
            selected_groups.append(random_group)

        return selected_groups

    def find_missed_users(self):
        # min_count = self.users[random.choice(self.users.keys())]['duty_count']
        # user_names = sorted(self.users, key=lambda i: self.users[i][DUTY_COUNT])
        grouped_by_duty_count = {}
        for username, user_data in self.users.iteritems():
            count = user_data[DUTY_COUNT]
            grouped_by_duty_count.setdefault(count, [])
            grouped_by_duty_count[count].append(username)

        # removing the users with the max duties count
        duties_count_list = grouped_by_duty_count.keys()
        duties_count_list.remove(max(duties_count_list))
        self.missed_users  = []
        for duties_count in duties_count_list:
            self.missed_users += grouped_by_duty_count[duties_count]

        return self.missed_users




    def select_a_random_group(self):
        selected_persons =  []
        for x in range(0, self.num_of_people_in_duty):
            random_index = random.randint(0,len(self.duplicated_temp_list)-1)
            selected_username = self.duplicated_temp_list[random_index]
            selected_persons.append(selected_username)
            del self.duplicated_temp_list[random_index]
            self.users[selected_username]['duty_count'] += 1
            # todo update 'been_with'

        return selected_persons

duties_scheduler = DutiesScheduler(user_names, num_of_people_in_duty = 2)
print duties_scheduler.random_bunch()
print '-----------'
print duties_scheduler.random_bunch()
print '-----------'
print duties_scheduler.random_bunch()
print '-----------'
print duties_scheduler.random_bunch()
print '-----------'
print duties_scheduler.random_bunch()
print '-----------'

# todos
# 1.slack messages
# 2.todo save current status to json file + enabling
# pulling current status from json
# 3.connect with calender
# not mvp - ui
# Send a message to #general channel
# slack.chat.post_message('#healthy-avocado', '',
#                         link_names = 1,
#                         username = 'avocado-bot',
#                         icon_emoji = ':chart_with_upwards_trend:')

# Get users list
# response = slack.users.list()
# users = response.body['members']


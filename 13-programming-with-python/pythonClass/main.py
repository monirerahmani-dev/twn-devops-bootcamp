# import user

from user import User

app_user_one =  User("nn@nn.com", "nana", "pwd11", "Devops")
app_user_one.get_user_info()

app_user_one.change_job_title("Software")
app_user_one.get_user_info()
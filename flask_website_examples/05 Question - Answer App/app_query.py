

# Q_001
# Function ---> Index
get_all_qst = '''select
                 questions.id as question_id,
                 questions.question_text,
                 questions.answer_text, 
                 askers.name as asker_name,
                 experts.name as expert_name
from questions
join users as askers on askers.id = questions.asked_by_id
join users as experts on experts.id = questions.expert_id
where questions.answer_text is not null'''

# Q_002
# Function ---> signup
check_if_user_exist = 'select id from users where name = ?'

# Q_003
# Function ---> signup/ insert into db
inject_new_user = 'insert into users (name, password, expert, admin) values (?,?,?,?)'

# Q_004
# Function ---> login
login_query = 'select id, name, password from users where name = ?'

# Q_005
# Function ---> ask
experts = 'select id, name from users where expert = 1'

# Q_006
# Function ---> ask /add question
add_question = 'insert into questions (question_text, asked_by_id, expert_id) values (?,?,?)'

# Q_007
# Function ---> question
get_question = '''select
                  questions.question_text,
                  questions.answer_text,
                  askers.name as asker_name,
                  experts.name as expert_name
from questions
join users as askers on askers.id = questions.asked_by_id
join users as experts on experts.id = questions.expert_id
where questions.id = ?'''

# Q_008
# Function ---> Expert/Answer - get all questions
question_view = 'select id, question_text from questions where id = ?'

# Q_009
# Function ---> Expert/answer - Answer the quetion
inject_answer = 'update questions set answer_text = ? where id = ?'

# Q_010
# Function ---> unanswered
unanswered_qst = '''select
                    questions.id,
                    questions.question_text,
                    users.name
from questions
join users on users.id = questions.asked_by_id
where questions.answer_text is null and questions.expert_id = ?'''

# Q_11
# Function ---> unanswered
unanswered_admin = '''select
                      questions.id,
                      questions.question_text,
                      questions.expert_id,
                      users.name,
                      expert.name as expert_name
from questions
join users on users.id = questions.asked_by_id
join users as expert on expert.id = questions.expert_id
where questions.answer_text is null
'''

# Q_12
# Function ---> Admin / users
query_users = 'select id, name, expert, admin from users'

# Q_13
# Function ---> Admin / promote
check_access_level = 'SELECT id, expert, admin FROM users WHERE id = ?'

# Q_14
# Function ---> Admin / promote
remove_promotion = 'update users set expert = 0 where id = ?'

# Q_15
# Function ---> Admin / promote
add_promotion = 'update users set expert = 1 where id = ?'







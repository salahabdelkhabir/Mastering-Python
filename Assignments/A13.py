#----------------------------------------------------<1>----------------------------------------------------

def get_score(**subjects):
    for subject, value in subjects.items():
        print(f"{subject} ==> {value}")
get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

#----------------------------------------------------<2>----------------------------------------------------

def get_the_scores(name='', **subjects):
    if not subjects:  # Check if there are no subjects provided
        print(f"Hello {name}, You Have No Scores To Show")
    else:
        print(f"Hello {name}, This Is Your Score Table:")
        for subject, value in subjects.items():
            print(f"{subject} ==> {value}")
get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

#----------------------------------------------------<3>----------------------------------------------------

scores_list = {
    'Math': 90,
    'Science': 80,
    'Language': 70
}

def get_the_scores(name='', **subjects):
    if not subjects:  
        print(f"Hello {name}, You Have No Scores To Show")
    
    elif not name:
        for subject, value in subjects.items():
            print(f"{subject} ==> {value}")
    else:
        print(f"Hello {name}, This Is Your Score Table:")
        for subject, value in subjects.items():
            print(f"{subject} ==> {value}")

get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)

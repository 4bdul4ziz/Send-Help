# ==========================================================================================================================
#  ?                                                     ABOUT
#  @author         :  4bdul4ziz & h0lycow
#  @email          :  bb.abdulaziz@gmail.com & subhranshupati0412@gmail.com
#  @repo           :
#  @createdOn      :  25th Feb 2022|01:15AM
#  @description    :  HashCode2022 Submission
# ==========================================================================================================================


import itertools
import time
import math
import glob
import random
import sys
import pandas as pd
from dataclasses import dataclass
from collections import defaultdict
from matplotlib.style import available


# ==========================================================================================================================
#                                                     CLASSES
# ==========================================================================================================================

PATHS = {
    "a": "input_data/a_an_example.in.txt",
    "b": "input_data/b_better_start_small.in.txt",
    "c": "input_data/c_collaboration.in.txt",
    "d": "input_data/d_dense_schedule.in.txt",
    "e": "input_data/e_exceptional_skills.in.txt",
    "f": "input_data/f_find_great_mentors.in.txt",
}


MAX_RUNTIME = 60
max_days = 0
max_best_before = 0
max_score = 0


class Contributor:
    __slots__ = ["name", "skill_count", "skills"]

    def __init__(self, name, skills):
        self.name = name
        self.skill_count = len(skills)
        self.skills = skills

    def __repr__(self):
        return f"Contributor(name={self.name}, skill_count={self.skill_count})"


class Project:
    __slots__ = ["name", "days", "score", "best_before", "skills", "roles"]

    def __init__(self, name, days, score, best_before, skills):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.skills = skills
        self.roles = len(skills)

    def __repr__(self):
        return f"Project(name={self.name}, days={self.days}, score={self.score}, best_before={self.best_before}, roles={self.roles})"

    def value(self, current_day=0):
        global max_days, max_best_before, max_score

        if self.best_before > (current_day + self.days):
            score = self.score
        else:
            score = self.score - ((current_day + self.days) - self.best_before)

        # max_level = 0
        # for skill in self.skills:
        #     if skill[1] > max_level:
        #         max_level = skill[1]
        # if max_level <= 7:
        #     score = score * 10

        score_per_day = score / self.days

        # todo add max level here

        return score_per_day


class ExecutedProject:
    def __init__(self, name, contributors):
        self.name = name
        self.contributors = contributors

    def print_sol(self, ofile):
        print(self.name, file=ofile)
        assert len(self.contributors) >= 1
        print(" ".join(self.contributors), file=ofile)


def filter_projects_by_skill(projects):
    filtered_projects = []
    for p in projects:
        print(p.name)
        print(p.skills)
        max_level = 0
        for skill in p.skills:
            if skill[1] > max_level:
                max_level = skill[1]
        print(max_level)
        if max_level <= 7:
            filtered_projects.append(p)
    return filtered_projects


def solve(INPUT_FILE):
    global max_days, max_best_before, max_score
    # READ INPUT FILE
    with open(INPUT_FILE, "r") as f:
        first_line = f.readline().strip()
        num_contr, num_pro = map(int, first_line.split(" "))

        print("Loading: {}".format(INPUT_FILE))
        print("Contributors:", num_contr)
        print("Projects:", num_pro)

        contributors = {}
        projects = []
        people_by_skill = defaultdict(dict)

        # Contributors
        for _ in range(num_contr):
            name, skill_count = f.readline().strip().split(" ")
            print(name)
            skills = {}
            for _ in range(int(skill_count)):
                sk, level = f.readline().strip().split(" ")
                skills[sk] = int(level)
                people_by_skill[sk][name] = int(level)
            contributors[name] = Contributor(name, skills)

        # Projects
        for _ in range(num_pro):
            name, days, score, best_before, roles = f.readline().strip().split(" ")
            print(name)
            skills = []
            for _ in range(int(roles)):
                sk, level = f.readline().strip().split(" ")
                skills.append((sk, int(level)))
            # normalize
            max_days = max(max_days, int(days))
            max_best_before = max(max_best_before, int(best_before))
            max_score = max(max_score, int(score))
            projects.append(
                Project(name, int(days), int(score), int(best_before), skills)
            )

        # print(contributors)
        # print(projects)

    executed_projects = []

    projects = filter_projects_by_skill(projects)

    remaining_projects = [x for x in projects]
    people_available = set([c.name for c in contributors.values()])
    all_people = set(contributors.keys())
    people_become_available = defaultdict(list)
    t1 = time.time()
    day = 0

    while remaining_projects and time.time() < t1 + MAX_RUNTIME:
        # find out whos available
        a = people_become_available[day]
        if a:
            people_available.update(a)

        # sort projects
        remaining_projects.sort(key=lambda l: l.value(day))

        for p in list(remaining_projects):
            skills_needed = p.skills

            print(p.name)
            # Team (without mentees)
            team = [None] * len(skills_needed)
            for i, (sk, level) in enumerate(skills_needed):
                print(sk)
                have_skill = [c for c, s in people_by_skill[sk].items() if s >= level]
                possible = people_available.intersection(have_skill)
                # take someone!
                if len(possible) > 0:
                    c = possible.pop()  # maybe take a random person
                    team[i] = c
                    people_available.remove(c)

            # find out the skills we have in the team
            highest_skills_wo = [None] * len(skills_needed)
            for current_pos, _ in enumerate(team):
                highest_skill = defaultdict(int)
                for c in list(team[0:current_pos] + team[current_pos + 1 :]):
                    if c is None:
                        continue
                    contributer = contributors[c]
                    for sk, level in contributer.skills.items():
                        highest_skill[sk] = max(level, highest_skill[sk])
                highest_skills_wo[current_pos] = highest_skill
            # print(highest_skills_wo)

            # Team (mentees)
            for current_pos, (sk, level) in enumerate(skills_needed):
                have_skill = [c for c, s in people_by_skill[sk].items() if s >= level]
                if level == 1:
                    can_be_mentee = all_people - set(have_skill)
                else:
                    can_be_mentee = [
                        c for c, s in people_by_skill[sk].items() if s == level - 1
                    ]
                possible_mentees = people_available.intersection(can_be_mentee)
                mentor_levels = highest_skills_wo[current_pos]
                if mentor_levels[sk] >= level and len(possible_mentees) > 0:
                    # we can use the mentee
                    if team[current_pos] is None:
                        # free for mentee anyway
                        m = possible_mentees.pop()
                        team[current_pos] = m
                        people_available.remove(m)
                    else:
                        # there is already someone here ...
                        m = possible_mentees.pop()
                        people_available.add(team[current_pos])
                        team[current_pos] = m
                        people_available.remove(m)
                        # because we can only use one mentee we break here
                        break

            if not None in team:
                # we have a match
                print(team)
                for c in team:
                    people_become_available[day + p.days].append(c)
                executed_projects.append(ExecutedProject(p.name, team))
                remaining_projects.remove(p)
            else:
                # give them back
                people_available.update(team)

        day += 1

    # Print Result to File
    with open(INPUT_FILE.replace(".txt", ".out"), "w") as of:
        print(len(executed_projects), file=of)
        for proj in executed_projects:
            proj.print_sol(of)


def write_trajectory(trajectory, best_project, best_contributor):
    trajectory += f"{best_project.name}"
    for contrib in best_contributor:
        trajectory += f" {contrib.name}"

    trajectory += "\n"

    return trajectory


def get_best_project(dispo_projects, cost_function):
    min_cost = np.inf
    for project in dispo_projects:
        cost_tmp = cost_function(project)
        if cost_tmp < min_cost:
            min_cost = cost_tmp
            best_project = project
    return best_project


def Assignments(DATA, PROJ):
    # create a list of all the projects
    projects = []
    for i in range(len(PROJ)):
        project = Project(
            PROJ[i]["name"],
            PROJ[i]["duration"],
            PROJ[i]["score"],
            PROJ[i]["best_before"],
        )
        for j in range(len(PROJ[i]["roles"])):
            project.add_role(PROJ[i]["roles"][j])
        projects.append(project)
    # create a list of all the contributors
    contributors = []
    for i in range(len(DATA)):
        contributor = Contributor(DATA[i]["name"], DATA[i]["skillCnt"])
        for j in range(len(DATA[i]["roles"])):
            contributor.add_role(DATA[i]["roles"][j])
        contributors.append(contributor)
    # assign the projects to the contributors
    for i in range(len(projects)):
        for j in range(len(projects[i].roles)):
            for k in range(len(contributors)):
                if projects[i].roles[j]["skill"] in contributors[k].skills:
                    if (
                        contributors[k].roles[projects[i].roles[j]["skill"]]
                        >= projects[i].roles[j]["level"]
                    ):
                        projects[i].roles[j]["assigned"] = contributors[k]
                        contributors[k].roles[
                            projects[i].roles[j]["skill"]
                        ] -= projects[i].roles[j]["level"]
                        break
    # print the assignments
    for i in range(len(projects)):
        print(
            "Project: {}\nDuration: {}\nScore: {}\nBest before: {}\nRoles: {}".format(
                projects[i].name,
                projects[i].duration,
                projects[i].score,
                projects[i].best_before,
                projects[i].roles,
            )
        )
    for i in range(len(contributors)):
        print(
            "Contributor: {}\nSkills: {}\nRoles: {}".format(
                contributors[i].name, contributors[i].skills, contributors[i].roles
            )
        )


class Mentors(object):
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.mentored_by = []

    def can_be_assigned_to_role(self, role):
        for skill in self.skills:
            if skill.level >= role.skill.level:
                return True
        return False

    def improve_skill_level(self, role):
        for skill in self.skills:
            if skill.level >= role.skill.level:
                skill.level += 1

    def __str__(self):
        return "Mentor: {}\nSkills: {}".format(self.name, self.skills)


class contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.mentored_by = []

    def can_be_assigned_to_role(self, role):
        return role.skill_level <= self.skills[role.skill]

    def improve_skill_level(self, roles):
        for role in roles:
            self.skills[role.skill] += 1

    def __str__(self):
        return "Contributor: {}\nSkills: {}\nMentored by: {}".format(
            self.name, self.skills, self.mentored_by
        )


def contributor_can_be_assigned_to_project(contributor, project):
    for role in project.roles:
        if contributor.can_be_assigned_to_role(role):
            return True
    return False


# roll func


def roll_project_list_project_possible(
    contributors, projects, cost_function, max_iter=1e5
):

    trajectory = str("\n")
    t = 0
    while (not len(projects) > 0) and t < max_iter:
        t += 1
        update_t(projects, contributors, t)
        dispo_projects = project_possible_list(projects, contributors)
        while len(dispo_projects) > 0:
            best_project = get_best_project(
                dispo_projects, cost_function
            )  # Return a class Project element
            best_contributors = get_best_contributor(
                best_project, contributors
            )  # Need a list of contributors, with role 1 in position 1 and so one
            update_choose(projects, contributors, best_project, best_contributors)
            trajectory = write_trajectory(trajectory, best_project, best_contributors)

    return trajectory


def roll_project_list_project_contributor_possible(
    contributors, projects, cost_function, max_iter=1e5
):

    trajectory = str("\n")
    t = 0
    while (not len(projects) > 0) and t < max_iter:
        t += 1
        update_t(projects, contributors, t)
        dispo_projects, dispo_contributors = project_contributors_possible_list(
            projects, contributors
        )
        while len(dispo_projects) > 0:
            best_project, best_contributor = get_best_project_and_contributors(
                dispo_projects, contributors, cost_function
            )

            update_choose(projects, contributors, best_project, best_contributor)
            trajectory = write_trajectory(trajectory, best_project, best_contributor)

    return trajectory


def cost_function(project, persons):
    return project.score_per_day


def project_possible_list(remaining_projects, persons_list):
    available_projects = remaining_projects
    for project in remaining_projects:
        avaible_persons = persons_list
        feasible_project = False
        for role in project.roles:
            feasible_role = False
            for person in persons_list:
                for skill in person.skills.keys():
                    if skill == role:
                        feasible_role = True
                        avaible_persons.remove(person)
                        break
                if feasible_role:
                    break
            if not feasible_role:
                available_projects.remove(project)
                break
    return available_projects


""" # testing inputs
DATA=[]
PROJ=[]
with open('input_data/a_an_example.in.txt', 'r') as f:
    lines = f.readlines()
    contriCnt,projCnt=lines[0].split(' ')
    lines.pop(0)
    for i in range(int(contriCnt)):
        details={}
        details['id']=i
        a,b=lines[0].split(' ')
        details['name']=a
        details['skillCnt']=int(b)
        lines.pop(0)
        skills=[]
        for j in range(int(b)):
            skill={}
            c,d=lines[0].split(' ')
            skill[c]=int(d)
            skills.append(skill)
            lines.pop(0)
        details['roles']=skills
        DATA.append(details)

    for i in range(int(projCnt)):
        details={}
        details['id']=i
        a,b,c,d,e=lines[0].split(' ')
        details['name']=a
        days=[int(b),int(c),int(d)]
        details['days']=days
        details['skillCnt']=int(e)
        skills=[]
        lines.pop(0)
        for j in range(int(e)):
            skill={}
            f,g=lines[0].split(' ')
            skill[f]=int(g)
            skills.append(skill)
            lines.pop(0)
        details['roles']=skills
        PROJ.append(details)


#inputs from input_data folder

from unicodedata import name """

""" 
class Project:
    def __init__(self, name, duration, score, best_before):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = []
        self.contributors = []
        self.skills = []
    
    def add_role(self, role):
        self.roles.append(role)

    def add_contributor(self, contributor):
        self.contributors.append(contributor)
        for skill in contributor.skills:
            if skill not in self.skills:
                self.skills.append(skill)   
    
    def __str__(self):
        return 'Project: {}'.format(self.name)


 """


def assignment(projects, contributors):
    assignments = []
    for project in projects:
        for contributor in contributors:
            if contributor_can_be_assigned_to_project(contributor, project):
                assignments.append((contributor, project))
    return assignments


def LearningOpportunity(projects, contributors):
    for project in projects:
        for contributor in contributors:
            if contributor.can_be_assigned_to_role(project.roles):
                contributor.improve_skill_level(project.roles)
    return contributors


def Mentoring(projects, contributors):
    for project in projects:
        for contributor in contributors:
            if contributor.can_be_assigned_to_role(project.roles):
                for mentor in contributor.mentored_by:
                    mentor.improve_skill_level(project.roles)
    return contributors


# function to assign a mentor to a contributor whose skill is below the required level
def assign_mentor(projects, contributors):
    for project in projects:
        for mentor in contributors:
            if mentor.can_be_assigned_to_role(project.roles):
                contributor.mentored_by.append(mentor)
                mentor.improve_skill_level(project.roles)
                return True
        return False


def fillingRoles(projects, contributors):
    for project in projects:
        for contributor in contributors:
            if contributor.can_be_assigned_to_role(project.roles):
                for role in project.roles:
                    if contributor.can_be_assigned_to_role(role):
                        if contributor.skills[role.skill] < role.skill_level:
                            contributor.skills[role.skill] = role.skill_level
    return contributors


def compute_skills(contributors, projects):
    skills_data = defaultdict(lambda: defaultdict(int))
    for project in projects:
        for role in project.roles:
            skills_data[role.skill_name][f"f_projects_{int(role.skill_level)}"] += 1
            skills_data[role.skill_name]["f_projects"] += 1

    for contributor in contributors:
        if contributor.available_in < 1:
            for skill in contributor.skills:
                level = contributor.skills[skill]
                skills_data[skill][f"f_contribs_{int(level)}"] += 1
                skills_data[skill]["f_contribs"] += 1

    return pd.DataFrame(skills_data).fillna(0)


# function to level up the contributor abd mentor
def levelUp(projects, contributors):
    for project in projects:
        for contributor in contributors:
            if contributor.can_be_assigned_to_role(project.roles):
                for role in project.roles:
                    if contributor.can_be_assigned_to_role(role):
                        if contributor.skills[role.skill] < role.skill_level:
                            contributor.skills[role.skill] = role.skill_level
    for contributor in contributors:
        for mentor in contributor.mentored_by:
            for role in project.roles:
                if contributor.can_be_assigned_to_role(role):
                    if contributor.skills[role.skill] < role.skill_level:
                        contributor.skills[role.skill] = role.skill_level
    return contributors


def formatSubmission(projects, contributors):
    names = []
    submissionFile = open("submission.txt", "w")
    Description = "{}\n".format(len(projects))
    for project in projects:
        names.append(project.name)
    for contributor in contributors:
        names.append(contributor.name)
    return names


class Submission:
    def __init__(self, projects, contributors):
        self.projects = projects
        self.contributors = contributors
        self.assignments = assignment(projects, contributors)
        self.LearningOpportunity = LearningOpportunity(projects, contributors)
        self.Mentoring = Mentoring(projects, contributors)
        self.fillingRoles = fillingRoles(projects, contributors)

    def __str__(self):
        return "Projects: {}\nContributors: {}\nAssignments: {}\nLearning Opportunity: {}\nMentoring: {}\nFilling Roles: {}".format(
            self.projects,
            self.contributors,
            self.assignments,
            self.LearningOpportunity,
            self.Mentoring,
            self.fillingRoles,
        )


class Scoring:
    def __init__(self, projects, contributors):
        self.projects = projects
        self.contributors = contributors
        self.assignments = assignment(projects, contributors)
        self.LearningOpportunity = LearningOpportunity(projects, contributors)
        self.Mentoring = Mentoring(projects, contributors)
        self.fillingRoles = fillingRoles(projects, contributors)
        self.submission = Submission(projects, contributors)
        self.score = 0
        self.penalty = 0
        self.totalScore = 0
        self.valid = True
        self.validate()


# function to calculate the score after completion including penalties
def calculateScore(self):
    for project in self.projects:
        if project.completed:
            self.score += project.score
            if project.completed_on > project.best_before:
                self.penalty += project.best_before - project.completed_on
    self.totalScore = self.score - self.penalty
    return self.totalScore


# function to check if the level ups are valid with respect to the project difficulty
def validate(self):
    for project in self.projects:
        if project.completed:
            for contributor in project.assigned_contributors:
                if (
                    contributor.skills[project.roles[0].skill]
                    < project.roles[0].skill_level
                ):
                    self.valid = False
    return self.valid


@dataclass
class Role:
    skill_name: str
    skill_level: int


class Project:
    def __init__(self, name, length, score, best_before, roles):
        self.name = name
        self.length = length
        self.score = score
        self.best_before = best_before
        self.roles = roles

    def __str__(self):
        return (
            f"<Project {self.name} | score: {self.score} | roles : {len(self.roles)}>"
        )

    def __repr__(self) -> str:
        return (
            f"<Project {self.name} | score: {self.score} | roles : {len(self.roles)}>"
        )


"""
projects = []
    projects.append(Project("WebServer", 10, 5, 10, [Role("Logging", 1), Role("WebChat", 1)]))
    projects.append(Project("Logging", 10, 5, 10, [Role("WebChat", 1)]))
    projects.append(Project("WebChat", 10, 5, 10, [Role("WebServer", 1), Role("Logging", 1)]))

    contributors = []
    contributors.append(Contributor("Bob", [Role("Logging", 1), Role("WebChat", 1)]))
    contributors.append(Contributor("Anna", [Role("WebServer", 1), Role("WebChat", 1)]))
    contributors.append(Contributor("Maria", [Role("WebServer", 1), Role("Logging", 1)]))
    contributors.append(Contributor("Bob", [Role("WebServer", 1), Role("WebChat", 1)]))

    submission = Submission(projects, contributors)
    print(submission)
    print(submission.assignments)
    print(submission.LearningOpportunity)
    print(submission.Mentoring)
    print(submission.fillingRoles)
    print(submission.submission)
    scoring = Scoring(projects, contributors)
    print(scoring)
    print(scoring.assignments)
    print(scoring.LearningOpportunity)
    print(scoring.Mentoring)
    print(scoring.fillingRoles)
    print(scoring.submission)
    print(scoring.score)
    print(scoring.penalty)
    print(scoring.totalScore)
    print(scoring.valid)
    print(scoring.validate())
    print(scoring.calculateScore())
"""


def emotionalDamage(path):
    contributors = []
    projects = []
    with open(path, "r") as f:
        f_contributors, f_projects = f.readline().split(" ")
        for i in range(int(f_contributors)):
            name, f_skills = f.readline().replace("\n", "").split(" ")
            skills = {}
            for j in range(int(f_skills)):
                skill_name, skill_level = f.readline().replace("\n", "").split(" ")
                skills[skill] = int(level)
            contributors.append({})
            g_contributor = contributors[-1]
            g_contributor["name"], f_skills = f.readline().replace("\n", "").split(" ")
            for k in range(int(f_skills)):
                skillName, skillLev = f.readline().split(" ")
                g_contributor[skillName] = int(skillLev)
            k_contributor = pd.DataFrame(contributors).fillna(0)

        for i in range(int(f_projects)):
            (project_name, project_length, score, best_before, f_roles,) = (
                f.readline().replace("\n", "").split(" ")
            )
            roles = []
            for j in range(int(f_roles)):
                skill_name, skill_level = f.readline().replace("\n", "").split(" ")
                roles.append(Role(skill_name, skill_level))
            projects.append(
                Project(project_name, project_length, score, best_before, roles)
            )

    print("contributors: \n", k_contributor)
    print("projects:\n", projects)
    return contributors, projects


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        files = args[1:]
    else:
        files = glob.glob("*.txt")

    for inputfile in files:
        if "requirements.txt" in inputfile:
            continue
        if ".out" in inputfile:
            continue
        solve(inputfile)


# ==========================================================================================================================
#                                                     EXTRAS
# ==========================================================================================================================

"""
There are M projects. Each project is described by:

its name
the duration of the project in days (how long it takes to complete a project once it is started)
the score awarded for completing the project
the “best before” time in days – if the project last day of work is strictly before the indicated day, it earns the full score. If it’s late (that is, the project is still worked on during or after its "best before day"), it gets one point less for each day it is late, but no less than zero points.
See also the example in the "Assignments" section below.
a list of roles for contributors working on the project
Each project has one or more roles that need to be filled by contributors. Each role requires one skill at a specific level, and can be filled by a single contributor. Each contributor can fill at most one role on a single project.





Each input data set is provided in a plain text file. The file contains only ASCII characters with lines ending with a single '\n' character (also called “UNIX-style” line endings). When multiple strings and numbers are given in one line, they are separated by a single space between each two elements.

The first line of the data set contains:

an integer C (1 ≤ C≤ 105) – the number of contributors,
an integer P (1 ≤ P ≤ 105) – the number of projects.
This is followed by C sections describing individual contributors. Each contributor is described by the following lines:

the first line contains:
the contributor's name (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, or numbers 0-9),
an integer N (1≤ N ≤ 100) - the number of skills of the contributor.
the next N lines describe individual skills of the contributor. Each such line contains:
the name of the skill (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, numbers 0-9, dashes '-' or pluses '+'),
an integer Li (1≤ Li ≤ 10) - skill level.
This is followed by P sections describing individual projects. Each project is described by the following lines:

the first line contains:
the name of the project (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z or numbers 0-9),
an integer Di (1 ≤Di ≤ 105) – the number of days it takes to complete the project,
an integer Si (1 ≤ Si ≤ 105) – the score awarded for project’s completion,
an integer Bi (1 ≤ Bi ≤ 105) – the “best before” day for the project,
an integer Ri (1 ≤ Ri ≤ 100) – the number of roles in the project.
the next Ri lines describe the skills in the project:
a string Xk – the name of the skill (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, numbers 0-9, dashes '-' or pluses '+'),
an integer Lk (1≤Lk≤100) – the required skill level.

example- 
Input file	Description
3 3
Anna 1
C++ 2
Bob 2
HTML 5
CSS 5
Maria 1
Python 3
Logging 5 10 5 1
C++ 3
WebServer 7 10 7 2
HTML 3
C++ 2
WebChat 10 20 20 2
Python 3
HTML 3
3 contributors, 3 projects
contributor Anna
 has C++ skill at level 2
contributor Bob
 has HTML skill at level 5
 has CSS skill at level 5
contributor Maria
 has skill Python at level 3
project Logging needs 1 contributor
 that needs to have C++ at level ≥ 3 (2 with mentoring)
project WebServer needs 2 contributors
 first contributor needs to have HTML at level ≥ 3 (2 with mentoring)
 second contributor needs to have C++ at level ≥ 2 (1 with mentoring)
project WebChat needs 2 contributors
 first contributor needs to have Python at level ≥ 3 (2 with mentoring)
 second contributor needs to have HTML at level ≥ 3 (2 with mentoring)






Assignments
Each contributor can start working on day 0 and can be working on at most one project at the same time. Once the work on a project starts, its contributors will be working on it the number of days equal to its duration and then become available to work on other projects.




A contributor can be assigned to a project for a specific role (at most one role in a single project), if they either:

have the skill at the required level or higher; or
have the skill at exactly one level below the required level, only if another contributor on the same project (assigned to another role), has this skill at the required level or higher. In this case, the contributor will be mentored by their colleague :)
One contributor can mentor multiple people at once, including for the same skill. A contributor can mentor and be mentored by other contributors at the same time.

Not possessing a skill is equivalent to possessing a skill at level 0. So a contributor can work on a project and be assigned to a role with requirement C++ level 1 if they don’t know any C++, provided that somebody else on the team knows C++ at level 1 or higher.




Scoring
Each contributor can only work on one project at a time. If one contributor is assigned to multiple projects, the contributor will work on them in the same order as they appear in the submission file. Each project starts immediately on the first day on which all the assigned contributors are available.
If some project assignment is invalid because the assigned contributor does not have the required skill level for the project after finishing all previously assigned projects, the submission is considered invalid and will not be scored.

Each project that is completed successfully receives its assigned score, as defined in the input file, minus penalty points for any delay. If a project is completed after its “best before” time, it gets one point less for each day it is late (but no less than zero points). Note that even if a project scores zero points, the assigned contributors will work on it (and may improve their skills thanks to it).

The total score is the sum of scores for all correctly completed projects.

"""

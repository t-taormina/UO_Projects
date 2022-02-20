"""
CIS 211 Lab 05
04.28.21
Author: Tyler Taormina
Aliasing:
Program to help ASUO (The Associated Students of the University of Oregon)
form and schedule clubs for students.
"""
from typing import List, Set, Dict, Optional


class Student:

    def __init__(self, name: str,
                 interests: list[str]):
        self.name = name
        self.interests = interests
        self.free_times = set([8, 9, 10, 11, 12, 13, 14, 15])
        self.meetings: list[int] = []

    def schedule_meeting(self, time: int):
        if time in self.free_times:
            self.meetings.append(time)
            self.free_times.discard(time)


class Club:

    def __init__(self, name: str):
        self.name = name
        self.members: list[Student] = []
        self.meeting_time: Optional[int] = None

    def join(self, student: Student):
        self.members.append(student)

    def find_common_time(self) -> int:
        if len(self.members) > 0:
            potential_meeting = self.members[0].free_times
            for member in self.members:
                potential_meeting = potential_meeting.intersection(member.free_times)
            if len(potential_meeting) > 0:
                return potential_meeting.pop()
            return 0
        else:
            return 0

    def schedule(self, time: int):
        for member in self.members:
            member.schedule_meeting(time)
        self.meeting_time = time


    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f"{self.name} ({', '.join(member_names)})"


class ASUO:

    def __init__(self):
        self.students: list[Student] = []
        self.clubs: list[Club] = []

    def enroll(self, s: Student):
        self.students.append(s)

    def form_clubs(self):
        clubs_to_form: Dict[str, Club] = {}
        for student in self.students:
            for interest in student.interests:
                if interest not in clubs_to_form:
                    clubs_to_form[interest] = Club(interest)
                    self.clubs.append(clubs_to_form[interest])

                clubs_to_form[interest].join(student)

    def schedule_clubs(self):
        for club in self.clubs:
            good_time = club.find_common_time()
            if good_time != 0:
                club.schedule(good_time)

    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f"{club} meets at {club.meeting_time}")


def main():
    asuo = ASUO()
    asuo.enroll(Student("Marty", ["badminton", "robotics"]))
    asuo.enroll(Student("Kim", ["backgammon"]))
    asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
    asuo.enroll(Student("George", ["chess", "badminton"]))

    asuo.form_clubs()
    asuo.schedule_clubs()
    asuo.print_club_schedule()


if __name__ == '__main__':
    main()

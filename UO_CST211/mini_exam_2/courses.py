"""Mini-exam: course conflict example
(very simplified to fit in mini-exam format)
"""
from typing import List


class Course:
    """Any course, scheduled or web-based (asynchronous)"""

    def conflicts_with(self, other: "Course") -> bool:
        """Does this course have a time commitment that conflicts
        with other course?
        """
        raise NotImplementedError("conflicts_with not implemented")

    def busy_at(self, hour: int) -> bool:
        """True if this course has a time commitment at
        time 'hour'
        """
        raise NotImplementedError("busy_at not implemented")


class LectureCourse(Course):
    """A lecture course has a scheduled lecture time, which must
    not conflict with the lecture time of any other course a student
    is taking.
    """
    def __init__(self, title: str, hour: int):
        self._hour = hour  # Simplified model of class times
        self.title = title


    def conflicts_with(self, other: "Course") -> bool:
        if type(other) == WebCourse:
            return False
        else:
            return self._hour == other._hour

    def busy_at(self, hour: int) -> bool:
        return self._hour == hour


class WebCourse(Course):
    """A web-based course has no scheduled lecture; it never
    conflicts with another course.
    """

    def __init__(self, title: str):
        self.title = title

    def conflicts_with(self, other: "Course") -> bool:
        return False

    def busy_at(self, hour: int) -> bool:
        return False


class Schedule:
    """Wraps a list of courses"""

    def __init__(self, courses: List[Course]):
        self._courses = courses


        #list contains Courses


    def has_conflicts(self) -> bool:
        for lect in range(len(self._courses)):
            for meet in self._courses[lect + 1:]:
                if self._courses[lect].conflicts_with(meet):
                    return True
        return False





















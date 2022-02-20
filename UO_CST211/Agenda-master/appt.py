"""
CIS 211 Project 1: Appointments
Author: Tyler Taormina
Credits: Alex Anderson, Avery Meyers
April 3, 2021
"""

from datetime import datetime


class Appt:
    """ An appointment has a start time, an end time, and
    a title. The start and end time should be on the same day.
    Usage Example:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
        if appt2 > appt1:
            print (f"appt1 '{appt1}' was over when appt2 '{appt2}' started")
        elif appt1.overlaps(appt2):
            print("Oh no, there is a  conflict in the schedule!")
            print(appt1.intersect(appt2))
    Should print:
        Oh no, there is a conflict in the schedule!
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """

    def __init__(self, start: datetime, finish: datetime, desc: str):
        """ An appointment start time, end time, and with a description of the appointment.
        The start and end time should be on the same day
        """
        assert finish > start, f"Period finish ({finish}) must be after start ({start})"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __eq__(self, other: 'Appt') -> bool:
        """ Equality refers to matching time periods between appointments,
        regardless of description"""
        return self.start == other.start and self.finish == other.finish

    def __lt__(self, other: 'Appt') -> bool:
        """ Less than checks to see if 'self' appointment ends before
        or at the same time as the 'other' appointment"""
        return self.finish <= other.start

    def __gt__(self, other: 'Appt') -> bool:
        """ Returns bool based on whether or not the 'self' appointment
        starts after the 'other' appointment finishes"""
        return self.start > other.finish

    def overlaps(self, other: 'Appt') -> bool:
        """ Returns true or false based on whether or not two appointments
        overlap each other."""
        return (self < (other) == False and self > (other) == False) or (self < other and self > other)

    def intersect(self, other: 'Appt') -> 'Appt':
        """ The overlapping time between two conflicting appointments"""
        #assert self.overlaps(other)  # precondition
        start_overlap = max(self.start, other.start)
        end_overlap = min(self.finish, other.finish)
        overlap_appt = Appt(start_overlap, end_overlap, f"{self.desc} & {other.desc}")
        return overlap_appt

    def __str__(self) -> str:
        """Reformats the appointment information into the format of
        yyyy-mm-dd hh:mm hh:mm | description
        This is only accurate if the start and finish are on the same day
        """
        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"

    def __repr__(self) -> str:
        """ Useful for debugging"""
        return f"Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})"




class Agenda:
    """An Agenda is a collection of appointments,
        similar to a list.

        Usage:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
        agenda = Agenda()
        agenda.append(appt1)
        agenda.append(appt2)
        ag_conflicts = agenda.conflicts()
        if len(ag_conflicts) == 0:
            print(f"Agenda has no conflicts")
        else:
            print(f"In agenda:\n{agenda.text()}")
            print(f"Conflicts:\n {ag_conflicts}")

        Expected output:
        In agenda:
        2018-03-15 13:30 15:30 | Early afternoon nap
        2018-03-15 15:00 16:00 | Coffee break
        Conflicts:
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
        """

    def __init__(self):
        self.elements = [ ]

    def __eq__(self, other: 'Agenda') -> bool:
        """ Delegate to __eq__ (==) of wrapped lists"""
        return self.elements == other.elements

    def __len__(self):
        """ Returns the length of the self.elements lit """
        return len(self.elements)

    def append(self, other: 'Appt'):
        """Moves other appt into the self appointment list """
        self.elements.append(other)

    def __str__(self):
        """Each Appt on its own line"""
        lines = [str(e) for e in self.elements]
        return "\n".join(lines)

    def __repr__(self) -> str:
        """constructor does not actually work this way"""
        return f"Agenda({self.elements})"

    def sort(self):
        """Sort agenda by appointment start times"""
        self.elements.sort(key=lambda appt: appt.start)

    def conflicts(self) -> 'Agenda':
        """Returns an agenda consisting of the conflicts(overlaps)
        between appointments in this agenda.
        Side effect: This agenda is sorted
        """
        conflict_agenda = Agenda()
        if len(self.elements) > 0:
            self.sort()
            i = 0
            for a in self.elements:
                i += 1
                for b in self.elements[i:]:
                    if a.finish < b.start:
                        break
                    else:
                        conflict_agenda.append(a.intersect(b))
        return conflict_agenda





























if __name__ == "__main__":
    print("Running usage examples...")

    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")

    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}' started")
    elif appt1.overlaps(appt2):
        print("Oh no, there is a  conflict in the schedule!")
        print(appt1.intersect(appt2))
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda}")
        print(f"Conflicts:\n {ag_conflicts}")

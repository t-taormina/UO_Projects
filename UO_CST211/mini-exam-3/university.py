"""A university has a hierarchical organization, as do many business organizations.
In a university, typical composite organizations include "schools" and "colleges"
(e.g., school of music, Lundquist school of business, college of arts and sciences,
college of education) and "divisions" (division of natural sciences within the
college of arts and sciences).

The atomic units (leaves of the organization tree) are typically called "departments"
(e.g., physics department, math department) and "programs" (e.g., family and human
services program within the college of education).
"""

from typing import List


class Organization:
    """Abstract class"""

    def where_is(self, name: str) -> List[str]:
        """If this organization contains any sub-organization
        matching name, return [this organization, ... , name]
        where ... is the list of organizations within this organization
        containing name.
        """
        raise NotImplementedError(f"Class {self.__class__.__name__} must implement 'find'")


class Unit(Organization):
    """A unit is an organization that does not contain any other
    organizations, e.g., a department or program.
    """
    def __init__(self, name: str):
        self._name = name
        # Do not modify the constructor

    def where_is(self, name: str) -> bool:
        if self._name == name:
            return [self._name]
        return []



class Composite(Organization):
    """A Composite is an organization that is made up of other
    organizations.  For example, the College of Arts and Sciences is
    made up of the Division of Natural Sciences, the Division of Social Sciences,
    and the Division of Humanities, while the Division of Natural Sciences
    is made up of the Math department, the Physics department, and several
    others.
    """
    def __init__(self, name: str, parts: List[Organization]):
        self._name = name
        self._parts = parts

    def where_is(self, name: str) -> List[str]:
        """Recursive case"""
        if name == self._name:
            return [self._name]

        else:
            for part in self._parts:
                if len(part.where_is(name)) > 0:
                    return part.where_is(name) + [self._name]
        return []













def main():
    acme = Composite("Acme",
                     [Composite("Explosives", [Unit("Dynamite"), Unit("TNT")]),
                      Unit("Jet-Packs")])
    boom_boom = acme.where_is("Dynamite")
    print(f"Wile E. Coyote can buy dynamite from Acme: {boom_boom}")
    whoosh = acme.where_is("Jet-Packs")
    print(f"Wile E. Coyote can buy jet packs from Acme: {whoosh}")
    invisipaint = acme.where_is("Invisibility paint")
    print(f"Wile E. Coyote cannot obtain invisibility paint: {invisipaint}")


if __name__ == "__main__":
    main()

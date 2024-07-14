
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        member['last_name'] = self.last_name
        member['id'] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
            else:
                pass


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members: 
            if member['id'] == id:
                return member
            else:
                pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

#I tried to use this class but couldn't make the dictionaries
class FamilyMember:
    last_name = None
    id = None
    def __init__(self, first_name, age, lucky_numbers):
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers

    def __str__(self):
        return f"{self.first_name} {self.age}"
    
    def dictionary(self):
        return {"id": id, "first_name": self.first_name, "age": self.age, "lucky_numbers": self.lucky_numbers}
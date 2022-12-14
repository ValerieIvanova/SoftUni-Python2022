from exam_prep.oop_exam_11_dec_21.project2.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_correct_init(self):
        self.assertEqual('Team', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_with_incorrect_data_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.incorrect_team = Team('Team123')
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member(self):
        self.team.members = {'Member1': 10, 'Member2': 20}
        members_to_add = {"Member1": 10, 'Member3': 30, 'Member4': 40}
        result = self.team.add_member(**members_to_add)
        self.assertEqual("Successfully added: Member3, Member4", result)
        result2 = self.team.add_member(**members_to_add)
        self.assertEqual('Successfully added: ', result2)
        self.assertEqual({"Member1": 10, 'Member2': 20, 'Member3': 30, 'Member4': 40}, self.team.members)

    def test_remove_non_existing_member(self):
        self.team.members = {'Member1': 10, 'Member2': 20}
        result = self.team.remove_member('Member3')
        self.assertEqual("Member with name Member3 does not exist", result)

    def test_remove_member_correctly(self):
        self.team.members = {'Member1': 10, 'Member2': 20}
        result = self.team.remove_member('Member2')
        self.assertEqual("Member Member2 removed", result)
        self.assertEqual({'Member1': 10}, self.team.members)

    def test_greater_than_method(self):
        self.other_team = Team("TeamTwo")
        self.other_team.members = {'Member1': 10}
        self.team.members = {"Member1": 10, 'Member2': 20}
        self.assertEqual(True, self.team > self.other_team)
        self.other_team.members = {"Member1": 10, 'Member2': 20, 'Member3': 30}
        self.assertEqual(False, self.team > self.other_team)

    def test_len_method(self):
        self.assertEqual(0, len(self.team))

        self.team.members = {"Member1": 10, 'Member2': 20}
        self.assertEqual(2, len(self.team))

    def test_add_method(self):
        self.team.members = {"Member1": 10, 'Member2': 20}

        self.other = Team('Python')
        self.other.members = {'Member3': 30, 'Member4': 40}

        self.new_team = self.team.__add__(self.other)

        self.assertEqual('TeamPython', self.new_team.name)
        self.assertEqual({"Member1": 10, 'Member2': 20, 'Member3': 30, 'Member4': 40}, self.new_team.members)

    def test_str_method(self):
        self.team.members = {'Member1': 10, 'Member2': 20}
        result = "Team name: Team\n" \
                 "Member: Member2 - 20-years old\n" \
                 "Member: Member1 - 10-years old"
        self.assertEqual(str(self.team), result)
        self.team.members = {'Member1': 10, 'Member2': 20, 'Member3': 20}
        result2 = "Team name: Team\n" \
                  "Member: Member2 - 20-years old\n" \
                  "Member: Member3 - 20-years old\n" \
                  "Member: Member1 - 10-years old"
        self.assertEqual(str(self.team), result2)


if __name__ == '__main__':
    main()
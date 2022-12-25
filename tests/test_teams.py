from API.api import Teambook
teams = Teambook()


def test_get_teams():
    status = teams.get_teams()
    assert status == 200


def test_post_teams():
    data = teams.post_teams()
    status = data[0]
    team_id = data[1]
    assert status == 201
    assert team_id

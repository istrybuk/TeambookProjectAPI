from API.api import Teambook

projects = Teambook()


def test_get_token():
    status = projects.get_token()[1]
    token = projects.get_token()[0]
    assert status == 201
    assert token


def test_get_business_units():
    status = projects.get_business_units()
    assert status == 200
    
    
def test_get_managers():
    status = projects.get_managers()
    assert status == 200
    
    
def test_get_projection_info():
    data = projects.create_project()
    project_id = data[1]
    project_url = data[2]
    status = projects.get_projection_info(project_url)
    projects.delete_project(project_id)
    assert status == 200
    assert project_id
    
    
def test_upload_project():
    status = projects.upload_project()
    assert status == 201
    
    
def test_get_time_off_list():
    status = projects.get_time_off_list()
    assert status == 200
    
    
def test_deactivate_project():
    project_id = projects.create_project()[1]
    status = projects.deactivate_project(project_id)
    projects.delete_project(project_id)
    assert status == 200
    
    
def test_activate_project():
    project_id = projects.create_project()[1]
    projects.deactivate_project(project_id)
    status = projects.activate_project(project_id)
    projects.delete_project(project_id)
    assert status == 200
    
    
def test_delete_project():
    project_id = projects.create_project()[1]
    status = projects.delete_project(project_id)
    assert status == 200
    
    
def test_export_project():
    project_id = projects.create_project()[1]
    status = projects.export_project(project_id)
    projects.delete_project(project_id)
    assert status == 201
    
    
def test_get_project_by_id():
    project_id = projects.create_project()[1]
    data = projects.get_project_by_id(project_id)
    status = data[0]
    projects.delete_project(project_id)
    project_name = data[1]
    client_id = data[2]
    manager_id = data[3]
    project_status = data[4]
    assert status == 200
    assert project_name == 'new project'
    assert client_id == 546
    assert manager_id == 2307
    assert project_status == 'Done'
    
    
def test_get_all_projects():
    status = projects.get_all_projects()
    assert status == 200
    
    
def test_get_active_projects():
    status = projects.get_active_projects()
    assert status == 200


def test_get_deactivated_projects():
    status = projects.get_deactivated_projects()
    assert status == 200
    

def test_create_project():
    data = projects.create_project()
    status = data[0]
    project_id = data[1]
    projects.delete_project(project_id)
    assert status == 201
    assert project_id
    
    
    

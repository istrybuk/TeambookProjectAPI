import json

import pytest
import requests

from settings import VALID_EMAIL, VALID_PASSWORD, TEAM_NAME


class Teambook:
	""" API library for website https://web.teambooktest.com """
	
	def __init__(self):
		self.base_url = 'https://web.teambooktest.com/api/'
	
	def get_token(self) -> json:
		""" Request to site swagger to get a users token using the specified email and password """
		form_data = {
			'user[email]': VALID_EMAIL,
			'user[password]': VALID_PASSWORD
		}
		res = requests.post(self.base_url + 'auth/login', form_data)
		text = res.text
		formatted_text = text.replace('"', "").replace('{', "").replace('}', "").replace(":", "").replace("=>", ': ')
		data = {i.split(': ')[0]: i.split(': ')[1] for i in formatted_text.split(', ')}
		my_token = data['token']
		status = res.status_code
		return my_token, status
	
	def create_project(self) -> json:
		""" Request to site swagger to create a project """
		my_token = self.get_token()[0]
		data = {
			'name': 'new project',
			'code': 'new',
			'active': True,
			'color': '#81a4d5',
			'kind': 'non_billable',
			'icon_id': 1,
			'estimated': 300,
			'notes': 'test notes, yes',
			'client_id': 546,
			'manager_id': 2307,
			'status': 'Done',
			'business_unit': 'test bu',
			'token': my_token
		}
		res = requests.post(self.base_url + 'projects', data=data)
		status = res.status_code
		project_id = res.json()['id']
		project_url = res.json()['url']
		return status, project_id, project_url
	
	def get_business_units(self) -> json:
		""" Request to site swagger to get a list of business units """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'projects/business_units' + '?token=' + my_token)
		status = res.status_code
		return status
	
	def get_managers(self) -> json:
		""" Request to site swagger to get a list of managers """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'projects/managers' + '?token=' + my_token)
		status = res.status_code
		return status
	
	def get_projection_info(self, project_url) -> json:
		""" Request to site swagger to get project info by url """
		my_token = self.get_token()[0]
		headers = {'Authorization': f'Bearer {my_token}'}
		data = {
			'url': project_url,
			'date': '2022-12-11'
		}
		res = requests.get(self.base_url + 'projects/projection', params=data, headers=headers)
		status = res.status_code
		return status
	
	@pytest.mark.xfail('when rerunning an error occurs due to the existing name due to impossibility to delete a project')
	def upload_project(self) -> json:
		""" Request to site swagger to upload a project """
		my_token = self.get_token()[0]
		data = {
			'projects_string': 'Project test from xls	PROJ123	Billable	SpaceX (ex.)	16/12/2022	22/9/2023	1000'
		}
		res = requests.post(self.base_url + 'projects/upload' + '?token=' + my_token, params=data)
		status = res.status_code
		print(res.json())
		return status
	
	def get_time_off_list(self) -> json:
		""" Request to site swagger to get a time_off_list """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'projects/time_off' + '?token=' + my_token)
		status = res.status_code
		return status
	
	def deactivate_project(self, project_id) -> json:
		""" Request to site swagger to deactivate a project """
		my_token = self.get_token()[0]
		data = {
			'token': my_token,
			'project_ids[]': project_id
		}
		res = requests.patch(self.base_url + 'projects/deactivate', params=data)
		status = res.status_code
		return status
	
	def activate_project(self, project_id) -> json:
		""" Request to site swagger to activate a project """
		my_token = self.get_token()[0]
		data = {
			'token': my_token,
			'project_ids[]': project_id
		}
		res = requests.patch(self.base_url + 'projects/activate', params=data)
		status = res.status_code
		return status
	
	def delete_project(self, project_id) -> json:
		""" Request to site swagger to delete a project """
		my_token = self.get_token()[0]
		data = {
			'token': my_token,
			'project_ids[]': project_id
		}
		res = requests.patch(self.base_url + 'projects/delete', params=data)
		status = res.status_code
		return status
	
	def export_project(self, project_id) -> json:
		""" Request to site swagger to export a project """
		my_token = self.get_token()[0]
		data = {
			'token': my_token,
			'project_ids[]': project_id
		}
		res = requests.post(self.base_url + 'projects/export', params=data)
		status = res.status_code
		return status
	
	def get_project_by_id(self, project_id) -> json:
		""" Request to site swagger to get a project by id """
		my_token = self.get_token()[0]
		data = {
			'project_ids[]': project_id
		}
		res = requests.get(self.base_url + 'projects/in_range' + '?token=' + my_token, params=data)
		status = res.status_code
		project_name = res.json()[0]['name']
		client_id = res.json()[0]['client_id']
		manager_id = res.json()[0]['manager_id']
		project_status = res.json()[0]['status']
		return status, project_name, client_id, manager_id, project_status
	
	def get_all_projects(self) -> json:
		""" Request to site swagger to get a list of all projects """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'projects' + '?token=' + my_token)
		status = res.status_code
		return status
	
	def get_active_projects(self) -> json:
		""" Request to site swagger to get a list of active projects """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'projects/active' + '?token=' + my_token)
		status = res.status_code
		return status
	
	def get_deactivated_projects(self) -> json:
		""" Request to site swagger to get a list of deactivated projects """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'projects/deactivated' + '?token=' + my_token)
		status = res.status_code
		return status

	def get_teams(self) -> json:
		""" Index all Teams """
		my_token = self.get_token()[0]
		res = requests.get(self.base_url + 'teams' + '?token=' + my_token)
		status = res.status_code
		return status

	def post_teams(self) -> json:
		""" Create new Team """
		my_token = self.get_token()[0]
		data = {
			'name': TEAM_NAME
		}
		res = requests.post(self.base_url + 'teams' + '?token=' + my_token, params=data)
		status = res.status_code
		team_id = res.json()['id']
		return status, team_id

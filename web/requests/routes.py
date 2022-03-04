from flask import Blueprint, request, render_template

from .scenarios import StudentsInGroupScenario


requests_app = Blueprint('requests_app', __name__, template_folder='templates')


@requests_app.route('/students-in-group', methods=['GET', 'POST'])
def students_in_group():
	if request.method == 'GET':
		return render_template('students_in_group_form.html')
	else:
		group = request.form.get('group', None)
		if group is None:
			return 'Group attribute required'
		students = StudentsInGroupScenario(group=group).execute()
		return render_template('students_in_group_result.html', students=students)

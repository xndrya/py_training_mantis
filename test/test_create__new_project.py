import operator

def test_create_project(app, start, db, json_project):
    project = json_project
    old_project_list = app.soap.get_projects()
    app.project.create(project)
    new_project_list = app.soap.get_projects()
    old_project_list.append(project)
    assert sorted(old_project_list, key=operator.attrgetter('name')) == sorted(new_project_list, key=operator.attrgetter('name'))
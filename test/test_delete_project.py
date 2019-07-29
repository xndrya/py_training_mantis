import operator

def test_delete_project(app, start, db, json_project):
    project = json_project
    old_project_list = db.get_project_list()
    app.project.delete(project)
    new_project_list = db.get_project_list()
    assert sorted(old_project_list, key=operator.attrgetter('name')) > sorted(new_project_list, key=operator.attrgetter('name'))

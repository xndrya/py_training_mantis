from model.project import Project
import operator

def test_delete_project(app, start, db, json_project):
    project = json_project
    if len(db.get_project_list()) == 0:
        app.project.fill_project_form(Project(name="A", description="B"))
    old_project_list = db.get_project_list()
    app.project.delete(project)
    new_project_list = db.get_project_list()
    assert sorted(old_project_list, key=operator.attrgetter('name')) > sorted(new_project_list, key=operator.attrgetter('name'))

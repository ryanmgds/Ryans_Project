#Data "setup" for Projects 
#next step would be to extract project data from a database
def setup():
  #Person Data
  name = "Ryans Website"
  github = "https://github.com/ryanmgds"
  youtube = "https://www.youtube.com/channel/UCZnCh2FDjYaWZCFFA9mWaGg?view_as=subscriber"
  source = {"name": name, "github": github, "youtube": youtube}
  #Project Data
  project1 =  "Hello Series"
  projlinks1 = [
    Link("Project Plan", "https://docs.google.com/document/d/17N2MkXo-_LUpaIfzWVqRwXqclbws3RSklNCshGCijHY/edit?usp=sharing"),
    Link("Repl", "https://repl.it/@BraydenBasinger/First-Project-Guess-The-Number#README.md"),
    Link("Resources", "https://padlet.com/jmortensen7/csp2021")
  ]
  project2 =  "Flask Project"
  projlinks2 = [
    Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
    Link("Repl", "https://repl.it/@BraydenBasinger/Flask-Web-Series-Coder-Joes#README.MD"),
    Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
  ]
  #Project Objects
  proj1 = Project(project1, projlinks1)
  proj2 = Project(project2, projlinks2)
  #HTML Data
  projects = Projects(source, [proj1, proj2])
  return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
  #link data with button and href (url)
  def __init__(self, btn, href):
    self.btn = btn
    self.href = href
  def get_btn(self):
    return self.btn
  def get_href(self):
    return self.href

#Project data class contain project name and links (Link class objects)
class Project():
  #project data with name and links
  def __init__(self, name, links):
    self.name = name
    self.links = links
  def get_name(self):
    return self.name
  def get_links(self):
    return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
  #HTML data with source and projects    
  def __init__(self, source, projects):
    self.source = source
    self.projects = projects
  #source data getter
  def get_source(self):
    return self.source
  #project data getter
  def get_projects(self):
    return self.projects
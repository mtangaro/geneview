#!/usr/bin/venv python

from jinja2 import Environment, FileSystemLoader
import argparse

template_dir = './templates'


#______________________________________
def render():
  print "plaaceholder"

  env = Environment( loader=FileSystemLoader(template_dir) )

  template = env.get_template("geneview.j2")

  rendered_template = template.render(data_m={"datam":"123"}, data_d={"datad":"456"}, deta_series={"series":"789"})

  print rendered_template

  with open("prova.html", "w") as fout:
    fout.write(rendered_template)


#______________________________________
if __name__ == '__main__':
  render()

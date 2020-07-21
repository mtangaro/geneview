#!/usr/bin/venv python

from jinja2 import Environment, FileSystemLoader
import argparse

template_dir = './templates'

# Rendering parameters
custom_tick_number = 5
abslolute_position_min = 158141736
abslolute_position_max = 158287227

# Data series style
utr5_style_dict= { "pointWidth": "20", "color": "red", "name": "5UTR" }
cds_style_dict= { "pointWidth": "20", "color": "orange", "name": "CDS" }
intron_style_dict= { "pointWidth": "2","color": "black", "name": "Intron" }
utr3_style_dict= { "pointWidth": "20", "color": "blue", "name": "3UTR" }

#______________________________________
def cli_options():
  parser = argparse.ArgumentParser(description='GeneView Render script')
  parser.add_argument('--enable-coverage', dest='coverage_section', default=False, action='store_true', help='Enable coverage section')
  return parser.parse_args()

#______________________________________
def render_positions_data(fin):
  print "placeholder"

  #find min and max!

#______________________________________
def render_series_data(fin):
  print "placeholder"

#______________________________________
def render():

  options = cli_options()

  # Render data for geneview here!

  env = Environment( loader=FileSystemLoader(template_dir) )

  template = env.get_template("geneview_v2.j2")

  rendered_template = template.render( 
                                       data_m={"datam":"123"},
                                       data_d={"datad":"456"},
                                       deta_series={"series":"789"},
                                       custom_tick_number=custom_tick_number,
                                       abslolute_position_min = abslolute_position_min,
                                       abslolute_position_max = abslolute_position_max,
                                       coverage_section=options.coverage_section
                                     )

  # Save the output html page
  with open("geneview_test.html", "w") as fout:
    fout.write(rendered_template)


#______________________________________
if __name__ == '__main__':
  render()

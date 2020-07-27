#!/usr/bin/venv python

from jinja2 import Environment, FileSystemLoader
import argparse
import pandas as pd
import numpy as np
import ast

template_dir = './templates'

# Some rendering parameters
custom_tick_number = 5

#______________________________________
def cli_options():
  parser = argparse.ArgumentParser(description='GeneView Render script')
  parser.add_argument('--input', dest='input_allgenes', default='./examples/allgenes.txt.gz', help='Input files')
  parser.add_argument('--gene-name', dest='gene_name', default='GRIA2', help='Gene name')
  parser.add_argument('--chr', dest='gene_chr', default='chr4', help='Define chr')
  parser.add_argument('--start', dest='abslolute_position_min', default=0, help='Start point')
  parser.add_argument('--end', dest='abslolute_position_max', default=0, help='End point')
  parser.add_argument('--enable-coverage', dest='coverage_section', default=False, action='store_true', help='Enable coverage section')

  return parser.parse_args()

#______________________________________
def render_series_data(fin, name):

  # Crate Pandas Data Frame
  allgenes_table = pd.read_csv(fin,sep='\t',header=None)

  # Set Column name for fast grouping
  allgenes_table.columns = ['gene_name', 'gene_id', 'transcript_info']

  # Select data by gene name
  gene_data = allgenes_table.loc[allgenes_table['gene_name'] == name]

  # Render data serie for geneview
  gene_data_list = gene_data['transcript_info'].to_list()
  serie = "{data: " + str(gene_data_list).replace('}",', '}",\n') +  "}" 
  serie = serie.replace('{data: [','{data: [\n')
  serie = serie.replace(']}','\n]},')

  # Removing unnecessary info from transcript column after "-" 
  #gene_data['transcript_info'] = allgenes_table['transcript_info'].apply(lambda x: x.split('-',1)[0]+"'}")

  # Grouping by gene
  # TODO: Gene is specified as input. No more needed. Will be removed in final version
  #allgenes_list = allgenes_table.groupby('gene_name')['transcript_info'].apply(list)

  # Create new DataFrame for fast edit
  # TODO: Gene is specified as input. No more needed. Will be removed in final version
  #data = pd.DataFrame({'gene_name':allgenes_list.index, 'transcript_info':allgenes_list.values})

  # Format data for geneview
  # TODO: Gene is specified as input. No more needed. Will be removed in final version
  #gene_data['transcript_info'] = gene_data['transcript_info'].apply(lambda x: "{data: " + str(x) +  "}")

  ## Render data series for geneview
  #series = ''
  ##for i in range(0,allgenes_list.shape[0]):
  #for i in range(0,2):
  #  series += data.loc[i]['transcript_info']+ ',\n'

  return serie

#______________________________________
def render():

  options = cli_options()

  # Render data for geneview here!
  data_series = render_series_data(options.input_allgenes, options.gene_name)

  env = Environment( loader=FileSystemLoader(template_dir) )

  template = env.get_template("geneview.j2")

  rendered_template = template.render( 
                                       data_m={"datam":"123"},
                                       data_d={"datad":"456"},
                                       data_series=data_series,
                                       custom_tick_number=custom_tick_number,
                                       gene_name=options.gene_name,
       	                               gene_chr=options.gene_chr,
                                       abslolute_position_min = options.abslolute_position_min,
                                       abslolute_position_max = options.abslolute_position_max,
                                       coverage_section=options.coverage_section
                                     )

  # Save the output html page
  with open("geneview_test.html", "w") as fout:
    fout.write(rendered_template)


#______________________________________
if __name__ == '__main__':
  render()

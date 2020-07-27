GeneView
========

TODO: Add description


Requirements
------------

GeneView requires python2 and virtualenv.

Installation
------------

1. Clone this repository.

2. Create a virtual environment

```
cd geneview
virutalenv venv 
```

3. Install the requirements

```
source ./venv/bin/activate
pip install -r requirements.txt
```

Usage
-----

```
python render_geneview.py --gene-name GRIA2 --start 158141846 --end 158287221 --chr chr4
```

The rendered page is named **geneview_test.html**

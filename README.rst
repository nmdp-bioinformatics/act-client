===============================
gfe_client
===============================


.. image:: https://img.shields.io/pypi/v/gfe_client.svg
        :target: https://pypi.python.org/pypi/gfe_client

.. image:: https://img.shields.io/travis/mhalagan-nmdp/gfe_client.svg
        :target: https://travis-ci.org/mhalagan-nmdp/gfe_client

.. image:: https://readthedocs.org/projects/gfe-client/badge/?version=latest
        :target: https://gfe-client.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/mhalagan-nmdp/gfe_client/shield.svg
     :target: https://pyup.io/repos/github/mhalagan-nmdp/gfe_client/
     :alt: Updates


Python client for calling the `ACT service`_


* Free software: LGPL 3.0
* Documentation: https://gfe-client.readthedocs.io.


Usage
---------

To annotated a sequence initialize a new ``BioSeqAnn`` object and then pass the sequence to the
``annotate`` method. The sequence must be a Biopython ``Seq``. The locus of the sequence is not required but it will improve the accuracy of the annotation.


.. code-block:: python3

    import gfe_client
    api = gfe_client.TypeSeqApi()
    response = api.typeseq_get(seq, imgthla_version="3.31.0")


CLI
------------

.. code-block:: shell
    
    usage: gfecli [-h] -i FILE [-l LOCUS] [-d DBVERSION] [-a ACTSERVICE] [-f] [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -i FILE, --file FILE  input file
      -l LOCUS, --locus LOCUS
                            HLA locus
      -d DBVERSION, --dbversion DBVERSION
                            IMGT/HLA dbversion
      -a ACTSERVICE, --actservice ACTSERVICE
                            URL for ACT service
      -f, --features        Return all features
      -v, --verbose         Option for running in verbose


Annotations
------------

.. code-block:: shell

            {
                "features": [
                 {
                    "accession": 2,
                    "rank": 6,
                    "sequence": "ATAGAAAAGGAGGGAGCTACTCTCAGGCTGCAA",
                    "term": "exon"
                  },
                  {
                    "accession": 1,
                    "rank": 6,
                    "sequence": "GTAAGTATGAAGGAGGCTGATGCCTGAGGTCCTTGGGATATTGTGTTTGGGAGCCCATGGGGGAGCTCACCCACCCCACAATTCCTCCTCTAGCCACATCTTCTGTGGGATCTGACCAGGTTCTGTTTTTGTTCTACCCCAG",
                    "term": "intron"
                  },
                  {
                    "accession": 1,
                    "rank": 7,
                    "sequence": "GCAGTGACAGTGCCCAGGGCTCTGATGTGTCTCTCACAGCTTGTAAAG",
                    "term": "exon"
                  }
                ],
                 "hla": "HLA-A*02:01:01:12",
                 'gfe': 'HLA-Aw2-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-4'
            }


Install
------------

.. code-block:: shell
    
    pip install gfe-client



Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`ACT Service`: http://act.b12x.org

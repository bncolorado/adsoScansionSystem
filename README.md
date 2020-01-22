# A metrical scansion system for fixed-metre Spanish poetry

Version 3.1.1 - July 2017
Borja Navarro Colorado
University of Alicante

Here is the code of the paper "A metrical scansion system for fixed-metre Spanish poetry" *Digital Scholarship in the Humanities*, 2017,  doi: https://doi.org/10.1093/llc/fqx009.


## Using the system with Docker
An image is already available in the Docker Hub.

To use it:
```
$ docker run -it -v $(pwd):/adso/data_in -v $(pwd):/adso/data_out linhdpostdata/adso
```
Where `data_in` contains plain text files to be analyzed and `data_out` will contain the output after the analysis is done.


The included Dockerfile can also be built running (from the root folder):
```
$ docker build -t adso .
```

And then run:
```
$ docker run -it -v $(pwd):/adso/data_in -v $(pwd):/adso/data_out adso
```

Some runtime options are available as environment variables in the `docker run -e ENV_VAR=value` command:
- `DATA_IN`, defaults to `"data_in"`
- `DATA_OUT`, defaults to `"data_out"`
- `FREELINGDIR`, defaults to `"/usr"` as per the local installation in the container.
- `FREELING_OPTIONS`, defaults to `"001010010001"`. See https://freeling-user-manual.readthedocs.io/en/latest/modules/maco/. Current options are as specified by Borja Navarro Colorado to replicate results agains the ADSO 100 Poem Corpus.

More detailed instructions to locally run the system can be found in the [analysis folder](analysis/README.md).

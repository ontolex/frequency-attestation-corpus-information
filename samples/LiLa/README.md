# Sample of the LiLa data

In this folder you'll find a sample of frequencies, citations and embeddings for 
a few words in 2 corpora in the [LiLa](https://lila-erc.eu/) collection.

## What is LiLa?

[LiLa](https://lila-erc.eu/) is an ERC-funded project lead by Marco Passarotti, 
and carried out at the [CIRCSE](https://centridiricerca.unicatt.it/circse_index.html) 
research center, Università Cattolica del Sacro Cuore, Milan (Italy).

It aims to connect language resources for Latin using the Linked Open Data paradigm. 
Its goal is to create a network of corpora, NLP resources and lexicons of Latin 
where components are fully interoperable and integrated in the larger LLOD cloud.


## Which corpora?

Frequencies and citations were measured on RDF representations of the following 
corpora, which were produced in the context of LiLa:

* the Index Thomisticus Treebank ([ITTB](https://itreebank.marginalia.it/)): 
a syntactically annotated corpus of the Latin works of Thomas Aquinas (13th century)

* the Latin section of [Dante Search](https://dantesearch.dantenetwork.it/), a 
lemmatized and morphologially annotated corpus of the works of Dante Alighieri 
(13th-14th century)

The two corpora can be seen as LOD data, respectively: [here](http://lila-erc.eu/data/corpora/ITTB/id/corpus) 
and [here](http://lila-erc.eu/data/corpora/DanteSearch/id/corpus).

A third corpus that is mentioned here is the [Opera Latina](http://web.philo.ulg.ac.be/lasla/opera-latina/#), 
created and maintained by the [LASLA](http://web.philo.ulg.ac.be/lasla/) 
laboratory in Liège. The morphologically annoated corpus (amounting to ca. 1,7 
milion words of Classical Latin) was used to train one of the two embeddings (see below).

## Which words?

For this sample, we chose 4:

* *subsisto*: a verb (see the [lemma](http://lila-erc.eu/data/id/lemma/126379))
* *officium*: a noun (see the [lemma](http://lila-erc.eu/data/id/lemma/114811))
* *mereo*: a verb, with a variant inflectional paradigm (see the [lemma](http://lila-erc.eu/data/id/lemma/11209))
* *mereor*: like the previous verb, but taken as deponent (i.e. lacking the active 
form; see [lemma](http://lila-erc.eu/data/id/lemma/112108)

Note that in the [LiLa lemma bank](https://github.com/CIRCSE/LiLa_Lemma-Bank) 
*mereo* and *mereor* are connected with a special relation of `lemma variant`, 
meaning that, while most dictionaries would list them as forms of the same 
words (see [here](https://logeion.uchicago.edu/mereo) for instance),
the different corpora can use either the one or the other as canonical form. As 
it happens, this is precisely the situation in the two corpora presented here. 
While the ITTB lemmatize only under *mereo*, Dante Search use both forms.

We decided to:
1. create 2 lexical entries, one for each canonical form;
2. in a second step (presently not yet reflected in the sample) to connect the 
two entries (via `skos:relatedMatch` perhaps?)

## Which embeddings?

The embeddings reported for the 4 sample words are taken from 
[these datasets](https://embeddings.lila-erc.eu/#topnav)

## How were the data collected?

ITTB and Dante Search can be queried using LiLa's [SPARQL Endpoint](https://lila-erc.eu/sparql/). 
We used SPARQL queries to obtain both the frequencies and the sequence of the 
preceding and following 5 words in a random occurrence.

## What's next?

It'd be a lot of fun to produce FrAC-modelled data on all the words in the corpora connected 
to LiLa, and those that will be in the future!

Just stay tuned...

## Funding

The *LiLa: Linking Latin* project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme – Grant Agreement No. 769994.

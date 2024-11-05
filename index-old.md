# The Ontolex Module for Frequency, Attestation and Corpus Information
# Draft Community Group Report 

Editors:

* Christian Chiarcos ([Applied Computational Linguistics, University of Augsburg, Germany](https://www.uni-augsburg.de/de/fakultaet/philhist/professuren/angewandte-computerlinguistik/)) 

Contributors: (please add yourself)

* Besim Kabashi ([Corpus and Computational Linguistics, Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany](https://www.linguistik.phil.fau.de/))
* Fahad Khan ([Istituto di Linguistica Computazionale <<A. Zampolli>>, Italy](www.ilc.cnr.it/))
* Ciprian-Octavian Truică
* Katerina Gkirtzou
* John P. McCrae
* Sander Stolk
* Thierry Declerck+
* Jesse de Does
* Katrien Depuydt
* Elena-Simona Apostol
* Max Ionov (Institute for Digital Humanities, University of Cologne, Germany)
* ...

[Copyright](https://www.w3.org/Consortium/Legal/ipr-notice#Copyright) © 2023 the Contributors to the The Ontolex Module for Frequency, Attestation and Corpus Information Specification, published by [Ontology Lexica](http://www.w3.org/community/ontolex/) under the [W3C Community Contributor License Agreement (CLA)](https://www.w3.org/community/about/agreements/cla/). A human-readable summary is [available](https://www.w3.org/community/about/agreements/cla-deed/). 

<section id="abstract">

This document describes the _module for frequency, attestation and corpus information_ of the OntoLex Lexicon Model for Ontologies (_OntoLex-Lemon_) developed by the W3C Community Group Ontology-Lexica. The module is targeted at complementing dictionaries and other linguistic resources containing lexicographic data with a vocabulary to express

*   corpus-derived information (frequency and cooccurrence information, collocation analysis, distributional similarity),
*   pointers from lexical resources to corpora and other collections of text (attestations, examples),
*   the linking of corpora and linguistic primary data with lexical information (dictionary linking), and
*   distributional semantics (collocation vectors, word embeddings, sense embeddings, concept embeddings).

The module tackles use cases in corpus-based lexicography, corpus linguistics and natural language processing, and operates in combination with the _OntoLex-Lemon_ core module (_Lemon_), as well as with other _lemon_ modules.

</section>

<section id="sotd">

This document is a working draft for a module for frequency, attestation and corpus data of the OntoLex specifications. It is not a W3C Standard nor is it on the W3C Standards Track.

> Note: the following information is to be removed from the final report

    There are a number of ways that one may participate in the development of this report:

    *   Mailing list: [public-ontolex@w3.org](http://lists.w3.org/Archives/Public/public-ontolex/)
    *   Wiki: [Main page](https://www.w3.org/community/ontolex/wiki/Main_Page)
    *   More information about meetings of the ONTOLEX group can be obtained [here](https://www.w3.org/community/ontolex/wiki/Main_Page#Meetings)
    *   [Source code](https://github.com/ontolex/frequency-attestation-corpus-information/) for this document can be found on Github.

Disclaimer: This draft follows closely the structure and design of [The Ontolex Lexicography Module. Draft Community Group Report 28 October 2018](https://jogracia.github.io/ontolex-lexicog/), edited by Julia Bosque-Gil and Jorge Gracia. In particular, motivational and introductory text are partially adapted without being marked as quotes. This is to be replaced by original text before publication.

> Note: HTML template to be applied

</section>

## Table of Contents

  * [Introduction](#introduction)
    + [Background and Motivation](#background-and-motivation)
    + [Aim and Scope](#aim-and-scope)
    + [Namespaces](#namespaces)
  * [Overview](#overview)
  * [Observations and Observables](#observations-and-observables)
    + [Observable (Class)](#observable--class-)
    + [Observation (Class)](#observation--class-)
    + [observedIn (ObjectProperty)](#observedin--property-)
  * [Frequency](#frequency)
    + [Frequency (Class)](#frequency--class-)
    + [unit (Property)](#unit--property-)
    + [frequency (ObjectProperty)](#frequency--objectproperty-)
    + [total (ObjectProperty)](#total--property-)
  * [Attestation](#attestation)
    + [Attestation (Class)](#attestation--class-)
    + [attestation (Property)](#attestation--property-)
    + [citation (Property)](#citation--property-)
    + [gloss (Property)](#gloss--property-)
    + [locus (Property)](#locus--property-)
  * [Collocations](#collocations)
    + [Collocation (Class)](#collocation--class-)
    + [cScore (property)](#cScore--property-)
    + [head (property)](#head--property-)
  * [Embeddings](#embeddings)
    + [Embedding (Class)](#embedding--class-)
    + [embedding (ObjectProperty)](#embedding--objectproperty-)
    + [FixedSizeVector (Class)](#fixedsizevector--class-)
    + [TimeSeries (Class)](#timeseries--class-)
    + [BagOfWords (Class)](#bagofwords--class-)
    + [attestationEmbedding (ObjectProperty)](#attestationembedding--objectproperty-)
  * [Similarity](#similarity)
    + [Similarity (Class)](#similarity--class-)
  * [Corpus Annotation (non-normative)](#corpus-annotation--non-normative-)
    + [oa:Annotation (Class)](#oa-annotation--class-)
    + [oa:hasBody (Object Property)](#oa-hasbody--object-property-)
    + [oa:hasTarget (Object Property)](#oa-hastarget--object-property-)
- [Usage guidelines](#usage-guidelines)
  * [Resource-specific subclasses of FrAC concepts](#resource-specific-subclasses-of-frac-concepts)
  * [RDF Serializations and CSV](#rdf-serializations-and-csv)
- [Acknowledgements](#acknowledgements)
- [References](#references)

<section>

## Introduction 

back to ([Table of Contents](#table-of-contents))

<section>

### Background and Motivation

back to ([Table of Contents](#table-of-contents))

[OntoLex-Lemon](https://www.w3.org/2016/05/ontolex/) provides a [core](https://www.w3.org/2016/05/ontolex/#core) vocabulary to represent _linguistic information_ associated to ontology and vocabulary elements. The model follows the principle of _semantics by reference_ in the sense that the semantics of a [lexical entry](https://www.w3.org/2016/05/ontolex/#LexicalEntry) is expressed by reference to an individual, class or property defined in an ontology. The OntoLex module for Frequency, Attestations and Corpus-Based Information (OntoLex-FrAC) complements OntoLex-Lemon with the capability of including information drawn from or found in corpora and linguistic primary data.

This builds on two primary motivations:

- corpus-based lexicography: OntoLex-Lemon has been increasingly used to publish, exchange and create dictionaries and lexicographical data in a *machine-readable* way. This module is partially motivated by requirements of corpus-based lexicography (frequency, collocations, semantic similarity) and digital philology (linking lexical resources with attestations and corpus data) and complements the [OntoLex module for lexicography](https://www.w3.org/2019/09/lexicog/) in that regard.

- natural language processing: With the rise of distributional semantics since the early 1990s, lexical semantics have been complemented by corpus-based co-occurrence statistics, collocation vectors (Schütze 1993), word embeddings (Collobert et al. 2012) and sense embeddings (Rothe and Schütze, 2017). With the proposed module and in addition to the requirements from corpus-based lexicography, OntoLex can serve as a community standard to encode, store and exchange numerical vector representations (embeddings) along with the lexical concepts, senses, lemmas, words or contexts (attestations) that they represent.

The added value of using linked data technologies to represent such information is an increased level of interoperability and integration between different types of lexical resources, the textual data they pertain to, as well as distributional representations of words, lexical senses and lexical concepts. Creating a designated module within OntoLex is a suitable means for establishing a vocabulary on a broad consensus that takes into account all use cases identified above in an adequate fashion. The OntoLex community is the natural forum to accomplish this for several reasons:

1.  The extended use of OntoLex-Lemon to support digital lexicography,
2.  the improved application and applicabiltiy of OntoLex-Lemon in natural language processing,
3.  the coming together of the lexicography, AI and human language technology communities, resp. resources, and
4.  the possibility of reusing already available mechanisms in OntoLex-Lemon, preventing researchers from "re-inventing the wheel",

</section>

<section>

### Aim and Scope

back to ([Table of Contents](#table-of-contents))

The goal of this module is to complement _OntoLex-Lemon_ elements with a vocabulary layer to represent lexicographical and semantic information derived from or defined with reference to corpora and external resources in a way that (a) _generalizes_ over use cases from digital lexicography, natural language processing, artificial intelligence, computational philology and corpus linguistics, that (b) facilitates _exchange, storage and re-usability_ of such data along with lexical information, and that (c) _minimizes information loss_ in comparison to other commonly used formalisms for such data.

The scope of the model is three-fold:

1.  complementing _OntoLex-Lexicog_ with corpus information to support corpus-driven lexicography (results of statistical analyses) and the inclusion of corpus evidence (attestations),
2.  modelling _existing_ lexical and distributional-semantic resources (corpus-based dictionaries, collocation dictionaries, embeddings) as linked data, to allow their conjoint publication and inter-operation by Semantic Web standards, and
3.  providing a conceptual / abstract model of relevant concepts in _distributional semantics_ (embeddings, similarity metrics, collocations) that facilitates building linked data-based applications that consume and combine both lexical and distributional information.

<div class="note">

_Corpus_ as used throughout this document is understood in its traditional, broader sense as a structured data collection -- or material suitable for being included into such a collection, such as manuscripts or other works. We do not intend to limit the use of the term to corpora in a linguistic or NLP sense. Language resources of any kind (web documents, dictionaries, plain text, unannotated corpora, etc.) are considered "corpus data" and a collection of such information as a "corpus" in this sense. Any information drawn from or pertaining to such information is considered "corpus-based". Accordingly, we account for observations in any kind of resource (identified by a URI), but ask users to specify its specific type according to the Dublin Core standard.

</div>

</section>

<section>

### Namespaces

back to ([Table of Contents](#table-of-contents))

This is a list of relevant namespaces that will be used in the rest of this document:

OntoLex module for frequency, attestation and corpus information

```@prefix frac: <http://www.w3.org/ns/lemon/frac#> .```

OntoLex (core) model and other _lemon_ modules:

```
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix synsem: <http://www.w3.org/ns/lemon/synsem#> .
@prefix decomp: <http://www.w3.org/ns/lemon/decomp#> .
@prefix vartrans: <http://www.w3.org/ns/lemon/vartrans#> .
@prefix lime: <http://www.w3.org/ns/lemon/lime#> .
@prefix lexicog: <http://www.w3.org/ns/lemon/lexicog#> .
```

Other models [TO REVIEW]:

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix skos: <http://www.w3.org/2004/02/skos#>.
@prefix dbr: <http://dbpedia.org/resource/>.
@prefix dbo: <http://dbpedia.org/ontology/>.
@prefix void: <http://rdfs.org/ns/void#>.
@prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#>.
@prefix dct: <http://purl.org/dc/terms/>.
@prefix provo: <http://www.w3.org/ns/prov#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix oa: <http://www.w3.org/ns/oa#>.
@prefix aat: <http://vocab.getty.edu/aat/>.
@prefix voaf: <http://purl.org/vocommons/voaf#>.
@prefix dcam: <http://purl.org/dc/dcam/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dcmitype: <http://purl.org/dc/dcmitype/> 

```

Helper namespace (for monitoring revision status, remove from final):

```
@prefix vs: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
```


### Vocabulary declaration

Necessary for bootstrapping Turtle from **this file**, keep in, but remove section before preparing the final report.


```
##########################
# vocabulary declaration #
##########################

<http://www.w3.org/ns/lemon/frac#>
    a owl:Ontology, voaf:Vocabulary ;
    # owl:imports <http://www.w3.org/ns/lemon/ontolex> 
    .

#########################
# imported vocabularies #
#########################

rdf:Bag
    rdfs:subClassOf rdfs:Container .

rdf:Seq
    rdfs:subClassOf rdfs:Container .

rdfs:member
    a owl:ObjectProperty .

rdf:value
    a owl:DatatypeProperty .

dct:extent
    a owl:DatatypeProperty .

dct:description
    a owl:DatatypeProperty .
```

</section>

<section>

## Overview

back to ([Table of Contents](#table-of-contents))

The following diagram depicts the OntoLex module for frequency, attestation and corpus information (_OntoLex-FrAC_). Boxes represent classes of the model. Arrows with filled heads represent object properties. Arrows with empty heads represent `rdfs:subClassOf`. Vocabulary elements introduced by this module are shaded grey (classes) or set in _italics_.


![](https://raw.githubusercontent.com/acoli-repo/frac-addenda/master/img/diagram-2023.png)
Fig. 2 OntoLex Module for Frequency, Attestation and Corpus Information (_FrAC_), overview 

> Note: old diagram: 
    
    ![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-observation-compact.puml?cache=no)

    Please use [this link](https://service.tib.eu/webvowl/#opts=doc=1;cd=180;dd=220;filter_disjoint=false;filter_setOperator=true;mode_compact=true;#iri=https://github.com/ontolex/frequency-attestation-corpus-information/raw/master/owl/frac.ttl) to get a live view on [the ontology](owl/frac.ttl).

</section>

<section>

## Observations and Observables

```
#####################
# top-level classes #
#####################
```

back to ([Table of Contents](#table-of-contents))

OntoLex-FrAC provides the necessary vocabulary to express *observations* obtained from a language resource about any linguistic or conceptual entity that can be observed in a corpus ("observable"). By observable, we mean 

- any *lexical entity* that can be described with OntoLex (including, but not limited to OntoLex core classes `ontolex:LexicalEntry`, `ontolex:Form`, `ontolex:LexicalSense` or `ontolex:LexicalConcept`), as well as
- any *ontological entity* from a knowledge graph (corresponding to the object of an `ontolex:denotes`, `ontolex:reference` or `ontolex:isConceptOf` property). 

The top-level concepts of OntoLex-FrAC are thus `frac:Observable` and `frac:Observation`, complemented by a designating where the observation has been `frac:observedIn`.


<div class="entity">

> ----------------------- ------------------------------------
> ### Observable (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Observable](http://www.w3.org/nl/lemon/frac#Observable)
> **Observable** is an abstract superclass for any element of a lexical resource that frequency, attestation or corpus-derived information can be expressed about. This includes, among others, `ontolex:LexicalEntry`, `ontolex:LexicalSense`, `ontolex:Form`, and `ontolex:LexicalConcept`. Elements that FrAC properties apply to  must be observable in a corpus or another linguistic data source.
> ----------------------- ------------------------------------
</div>

```
frac:Observable
    a owl:Class ;
    # vs:term_status "stable" ;
    skos:definition """Observable is an abstract superclass for any element of a lexical resource that frequency, attestation or corpus-derived information can be expressed about. This includes, among others, `ontolex:LexicalEntry`, `ontolex:LexicalSense`, `ontolex:Form`, and `ontolex:LexicalConcept`. Elements that FrAC properties apply to  must be observable in a corpus or another linguistic data source."""@en;
    rdfs:label "observable"@en.

ontolex:Form
    rdfs:subClassOf frac:Observable ;
    vs:term_status "stable" .

ontolex:LexicalConcept
    rdfs:subClassOf frac:Observable ;
    vs:term_status "stable" .

ontolex:LexicalEntry
    rdfs:subClassOf frac:Observable ;
    vs:term_status "stable" .

ontolex:LexicalSense
    rdfs:subClassOf frac:Observable ;
    vs:term_status "stable" .
```

![](img/ontolex-element.png "frac:Observable")
Fig. 1. `frac:Observable` as a superclass of ontolex:LexicalEntry, ontolex:Form, ontolex:LexicalSense and ontolex:LexicalConcept

For OntoLex, we assume that frequency, attestation and corpus information can be provided about _every_ linguistic content element in the OntoLex-Lemon core model and in existing or forthcoming OntoLex modules. This includes `ontolex:Form` (for token frequency, etc.), `ontolex:LexicalEntry` (frequency of disambiguated lemmas), `ontolex:LexicalSense` (sense frequency), `ontolex:LexicalConcept` (e.g., synset frequency), `lexicog:Entry` (if used for representing homonyms: frequency of non-disambiguated lemmas), etc. (cf. Fig. 1). 
In particular, we consider all these elements as being countable, annotatable/attestable and suitable for a numerical representation by means of an embedding. For this reason, we introduce `frac:Observable` as a top-level element within the FrAC module that is used to define the `rdfs:domain` of any properties that link lexical and corpus-derived information. 

> **Note:** The definition `frac:Observable` does not posit an exhaustive list of possible observables. Instead, anything that can be observed in a corpus can be defined as `frac:Observable`. This includes elements of OntoLex modules not listed here (e.g., `decomp:Component`, `synsem:SyntacticArgument`, etc.) or future OntoLex vocabularies. Likewise, it can also include URIs which have no relation to OntoLex whatsoever, as these are foreseen as external elements that OntoLex-Lemon can provide information about, but only if they are based on or linked with corpus information, attested in a document, a text or its annotations.

<div class="entity">

> ----------------------- ------------------------------------
> ### Observation (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Observation](http://www.w3.org/nl/lemon/frac#Observation)
> **Observation** is an abstract superclass for anything that can be observed in a corpus about an Observable. An observation MUST have at least one `rdf:value` to express its value, it SHOULD have exactly one `frac:observedIn` property that defines the data from which this information was drawn, and it SHOULD have a `dct:description` explaining the methodolgy and/or extraction method by which the observation was obtained.
> rdfs:subclassOf 1 `frac:observedIn`
> rdfs:subclassOf min 1 `dct:description`
> rdfs:subClassOf 1 rdf:value
> ----------------------- ------------------------------------
</div>

```
frac:Observation
    a owl:Class;
    rdfs:subClassOf [
        a <http://www.w3.org/2002/07/owl#Restriction> ;
        <http://www.w3.org/2002/07/owl#minCardinality> "1"^^<http://www.w3.org/2001/XMLSchema#nonNegativeInteger> ;
        <http://www.w3.org/2002/07/owl#onProperty> rdf:value
   ] ;

   rdfs:subClassOf [
        a <http://www.w3.org/2002/07/owl#Restriction> ;
        <http://www.w3.org/2002/07/owl#minCardinality> "1"^^<http://www.w3.org/2001/XMLSchema#nonNegativeInteger> ;
        <http://www.w3.org/2002/07/owl#onProperty> frac:observedIn
   ] ;

    # the following constraint is semantically empty
    # it is supposed to express that there should be
    # a human-readable description, but we don't enforce it
    # in order not to break validation
    rdfs:subClassOf [
        a <http://www.w3.org/2002/07/owl#Restriction> ;
        <http://www.w3.org/2002/07/owl#minCardinality> "0"^^<http://www.w3.org/2001/XMLSchema#nonNegativeInteger> ;
        <http://www.w3.org/2002/07/owl#onProperty> dct:description
    ] ;
    vs:term_status "tbc" . 
```

Observations as understood here are **empirical** (quantitative) observations that are made against a corpus, a text, a document or another type of language data. Observations can be made in any  kind  of  (collection  or excerpt of)  linguistic  data  at  any scale,  structured  or  unstructured, regardless of its physical materialization (as an electronic corpus, as a series of printed books, as a bibliographical database or as metadata record for a particular corpus).

> ----------------------- ------------------------------------
> ### observedIn (ObjectProperty)
> For a `frac:Observation`,  the property **observedIn** defines the URI of the data source (or its metadata entry) that this particular observation was made in or derived from. This can be, for example, a corpus or a text represented by its access URL, a book represented by its bibliographical metadata, etc.
> As these data sources can have different characteristics, users SHOULD specify their respective type using the [DCMI Type Vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7).
> **Domain:** frac:Observation
> **Range:** anyURI
>
> ----------------------- ------------------------------------

```
frac:observedIn
    a owl:ObjectProperty ;
    rdfs:domain frac:Observation ;
    rdfs:range [   
        a owl:Restriction ;
        owl:onProperty rdf:type ;
        owl:someValuesFrom [
            a owl:Restriction ;
            owl:onProperty dcam:memberOf ;
            owl:hasValue dcterms:DCMIType ] ] ;
    vs:term_status "tbc" ;
    rdfs:comment """For an Observation, the property observedIn defines the URI of the data
    source (or its metadata entry) that this particular observation was made in or derived from.
    This can be, for example, a corpus or a text represented by its access URL, a book 
    represented by its bibliographical metadata, etc."""@en .
```

For machine-readable corpora that are/can be characterized by their size, data providers can provide overall size information using the property `frac:total`, see section on Frequency below.

We provide four examples for FrAC data sources below:

1. 2012 English news subcorpus of the Leipzig Corpora collection, primarily used for computational lexicography. For `frac:total`, see the frequency section. The data provider provides the total number of sentences, lemmas ("types") and words ("tokens"), as reflected by the units of the `frac:Frequency`. The use of additional language resource metadata, e.g., language or publication year, is highly recommended, but not formally required.

        <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012> a dcmitype:Collection ;
            frac:total 
                [ a frac:Frequency ; frac:measure "sentences" ; rdf:value "8,525,045" ] ,
                [ a frac:Frequency ; frac:measure "tokens" ;    rdf:value "177,363,729" ] ,
                [ a frac:Frequency ; frac:measure "lemmas" ;    rdf:value "1,126,551" ] ;
            dct:language <http://lexvo.org/id/iso639-3/eng> ;
            dct:date "2012" ;
            dct:description """Leipzig Corpora Collection: English news corpus based on material 
                            from 2012. Leipzig Corpora Collection. Dataset."""@en .

2. Google Books NGrams, a collection of n-grams. This is not a corpus, but a table of tab-separated values with sequences of words, their frequency in the underlying corpus and the number of individual documents they occur in (document frequency) for individual languages and n-gram sizes. This is a multilingual resource, so we cannot provide a unique language code. Further, it does not provide a total.

        <https://books.google.com/ngrams> a dcmitype:Dataset .

3. The EPSD corpus, the data basis underlying the Electronic Penn Sumerian Dictionary. This is a multilingual corpus, consisting primarily of Sumerian, but also of Akkadian texts, hence it provides two language codes. The frequencies ("almost ...", "over ...") are provided in the same form as on the EPSD website for version 2.7. Note that `frac:Frequency` can be RDFS-inferred from `frac:total` and `frac:measure`, so that it can be left implicit.

        <http://oracc.museum.upenn.edu/epsd2> a dcmitype:Collection ;
            dct:language "sux", "akk" ;
            frac:total [ frac:measure "lexemes" ;        rdf:value "almost 16,000" ] ;
            frac:total [ frac:measure "names" ;          rdf:value "over 50,000" ] ;
            frac:total [ frac:measure "distinct forms" ; rdf:value "more than 225,000" ] ;
            frac:total [ frac:measure "texts" ;          rdf:value "over 110,000" ] ;
            frac:total [ frac:measure "tokens" ;         rdf:value "almost 3.4 million" ] .

4. Yet another type of FrAC data sources are `dcmitype:Text` objects, including digitally edited text, edited text bundled with metadata about the original text, or digital metadata about a non-digital text. Also note that in this particular case, the only total provided by the original metadata / description (indirectly, though) is that this constitutes one letter.

        <https://www.dbnl.org/tekst/groo001brie04_01/groo001brie04_01_0003.php> a dcmitype:Text ;
            dct:language "nl" ;
            dct:date "1629-01-06" ;
            dct:author "N. van Reigersberch" ;
            rdfs:comment """Hugo de Groot, Briefwisseling van Hugo Grotius. Deel 4(1964), 1361. 
                1629 januari 6. Van N. van Reigersberch, Adres: (A Mon)sieur Monsieur Grotius à 
                Paris. 
                In dorso schreef Grotius: 6 Jan. 1629 N. Reigersberg."""@nl .

    > Note: For anchoring individual attestations in documents, groups of documents, or their components, the property `frac:locus` can be used in addition to `frac:observedIn`, see Attestation section below. Furthermore, it is recommended to employ specialized vocabularies for bibliographical references.

> Implementation note: tbc. whether all example datasets used in text are listed here

> Note that for FrAC data sources illustrated above, we use the original access URL as data source URI. As these will resolve only if the data providers themselves provide linked-data-compliant metadata, these URIs will not resolve at the moment. For providers of lexical data, a best practice recommendation for cases in which they are not in control of the access URL is to mint (and host) a distinct data source URI and define it to be `owl:sameAs` the access URL.

</section>


<section>

## Frequency

```
#############
# frequency #
#############
```

back to ([Table of Contents](#table-of-contents))


Frequency information is a crucial component in human language technology. Corpus-based lexicography originates with Francis and Kucera (1958), and subsequently, the analysis of frequency distributions of word forms, lemmas and other linguistic elements has become a standard technique in lexicography and philology, and given rise to the field of corpus linguistics. At its core, this means that lexicographers use (corpus) frequency and distribution information while compiling lexical entries (also see the section on collocations and similarity below). As a qualitative assessment, frequency can be expressed with [lexinfo:frequency](http://www.lexinfo.net/ontology/2.0/lexinfo#frequency), "[t]he relative commonness with which a term occurs". However, this is an object property with possible values lexinfo:commonlyUsed, lexinfo:infrequentlyUsed, lexinfo:rarelyUsed, while absolute counts over a particular resource (corpus) require novel vocabulary elements.

For modelling, we focus on absolute frequencies, as relative frequencies can be derived if absolute frequencies and totals are known. Absolute frequencies are used in computational lexicography (e.g., the [Electronic Penn Sumerian Dictionary](http://oracc.museum.upenn.edu/epsd2/)), and they are an essential piece of information for NLP and corpus linguistics.
In order to avoid confusion with lexinfo:Frequency (which provides lexicographic assessments such as commonly used, infrequently used, etc.), this is defined with reference to a particular dataset, a corpus.

<div class="entity">

> ----------------------- ------------------------------------
> ### Frequency (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Frequency](http://www.w3.org/nl/lemon/frac#Frequency)
> **Frequency** is a `frac:Observation` of the absolute number of attestations (`rdf:value`) of a particular `frac:Observable` (see `frac:frequency`) that is `frac:observedIn` in a particular data source. Using `frac:unit`, frequency objects can also identify the (segmentation) unit that their counts are based on. 
> **SubClassOf:** `frac:Observation`
> **SubClassOf:** `rdf:value` exactly 1 , `frac:observedIn` exactly 1
>
> ----------------------- ------------------------------------
</div>

```
frac:Frequency
    a owl:Class ;
    rdfs:subClassOf frac:Observation ;
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:cardinality "1"^^xsd:nonNegativeInteger ;
        owl:onDataRange xsd:int ;
        owl:onProperty rdf:value
    ] ;
    vs:term_status "stable" .
```

<div class="entity">

> ----------------------- ------------------------------------
> ### unit (Property)
> **URI:** [http://www.w3.org/nl/lemon/frac#unit](http://www.w3.org/nl/lemon/frac#unit)
> For a `frac:Frequency` object, the property **unit** provides an identifier of the respective segmentation unit.
> **rdfs:range** `frac:Frequency`
>
> ----------------------- ------------------------------------
</div>

Examples for `frac:unit` include string literals such as `"tokens"`, `"sentences"`, etc. If a future community standard provides reference URIs for such datatypes, `frac:unit` should be used as a datatype property. Until such a convention has been established, it is recommended to be used as a datatype property.

> Note: One function of `frac:unit` is to calculate relative frequencies from absolute values as provided by the `rdf:value` of `frac:Frequency` objects. While these can be calculated by diving `rdf:value` of a particular frequency object *f* by the `rdf:value` of its `frac:observedIn/frac:total`, this equation is restricted to frequency objects using the same `frac:unit`.

> Implementation note: check whether domain and range are always put right!

<div class="entity">

> ----------------------- ------------------------------------
> ### frequency (ObjectProperty)
> **URI:** [http://www.w3.org/nl/lemon/frac#frequency](http://www.w3.org/nl/lemon/frac#frequency)
> The property **frequency** assigns a particular `frac:Observable` a `frac:Frequency`.
> **rdfs:domain** `frac:Observable`
> **rdfs:range** `frac:Frequency`
>
> ----------------------- ------------------------------------
</div>

```
frac:frequency
    a owl:ObjectProperty ;
    rdfs:domain frac:Observable ;
    rdfs:range frac:Frequency ;
    vs:term_status "stable" .
```


<div class="note">

> If information from multiple language resources is aggregated (also cf. the section on embeddings below), these should be aggregated into a a single data source that can be referred to by `frac:observedIn`, as there must be exactly one `frac:observedIn`.

> TODO: make sure that this unique cardinality constrain is respected in the examples here.

</div>

The definition above only applies to absolute frequencies. For expressing relative frequencies, we  expect  the associated data source (`frac:observedIn`) object to  define  a  total  of  elements  contained  (`frac:total`). In many practical applications, it is necessary to provide relative  counts,  and  in  this  way,  these  can  be  easily  derived  from  the  absolute  (element)  frequency  provided  by the Frequency class  and  the  total  defined  by the underlying  corpus. If the real absolute values are unknown and only relative scores are provided, data providers should use percentage values for both the `Frequency` `rdf:value` and for the `frac:total` (i.e., `100%`) of the associated corpus.

> ----------------------- ------------------------------------
> ### total (ObjectProperty)
> The object property **total** assigns  any potential FrAC data source (i.e., `dct:Collection`, `dct:Dataset`, `dct:Text` or any other member of DCMI Type) the  total  number  of  elements  that  it  contains as a `frac:Frequency` object.
> **Domain:** class that is a `dcam:memberOf` DCMI Type
> **Range:** frac:Frequency
>
> ----------------------- ------------------------------------

> Note: For `frac:total`, users should provide both the frequency and the segmentation/unit over which this frequency is obtailed. For an observable, then, relative frequencies (for any given unit *u*) can then be calculated from the object values of `frac:frequency/rdf:value`  and `frac:frequency/frac:observedIn/frac:total/rdf:value` if (and only if) the correspondung units match.


```
frac:total
    a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain [
        a owl:Restriction ;
        owl:onProperty rdf:type ;
        owl:someValuesFrom [
            a owl:Restriction ;
            owl:onProperty  dcam:memberOf ;
            owl:hasValue dcterms:DCMIType  ] ] ;
    rdfs:range xsd:int ;
    rdfs:label "could be renamed to frac:tokens, as different kinds of totals as possible for multi-word expressions"@en ;
    vs:term_status "tbc" .
```



The following example illustrates word and form frequencies for the Sumerian word _a_ (n.) "water" from the [Electronic Penn Sumerian Dictionary](http://oracc.museum.upenn.edu/epsd2/sux) and the frequencies of the underlying corpus.

<div class="beispiel">

<div>

    # word frequency, over all form variants 
    epsd:kalag_strong_v a ontolex:LexicalEntry;
        frac:frequency [
            a frac:Frequency; 
            rdf:value "2398"^^xsd:int; 
            frac:observedIn <http://oracc.museum.upenn.edu/epsd2/pager>
        ] .

    # form frequency for individual orthographical variants 
    epsd:kalag_strong_v ontolex:canonicalForm [
        ontolex:writtenRep "kal-ga"@sux-Latn; 
        frac:frequency [
            a frac:Frequency; 
            rdf:value "2312"^^xsd:int; 
            frac:observedIn <http://oracc.museum.upenn.edu/epsd2/pager>
            ]
        ] .

    epsd:kalag_strong_v ontolex:otherForm [ 
        ontolex:writtenRep "kalag"@sux-Latn; 
        frac:frequency [ 
            a frac:Frequency; 
            rdf:value "70"^^xsd:int; 
            frac:observedIn <http://oracc.museum.upenn.edu/epsd2/pager>
            ]
        ] .

</div>

</div>

The example shows orthographic variation (in the original writing system, Sumerian Cuneiform sux-Xsux, and its Latin transcription sux-Latn). It is slightly simplified insofar as the ePSD2 provides individual counts for different periods and that only three of six orthographical variants are given. Note that these are orthographical variants, not morphological variants (which are not given in the dictionary).

<div class="note">
> TODO: update the examples below with explicit `Corpus` elements. Add total.
</div>

<div class="note">

> It is necessary to provide the link to the underlying corpus _for every frequency assessment_ because the same element may receive different counts over different corpora. For data modelling, it is recommended to define a corpus- or collection-specific subclass of frac:Frequency with a fixed `frac:observedIn` object. This leads to more compact data and avoids potential difficulties with the Open World Assumption (interpretability of incomplete data).

<div class="beispiel">

<div>

<pre>                
# Frequency in the EPSD corpus
:EPSDFrequency rdfs:subClassOf frac:Frequency.
:EPSDFrequency rdfs:subClassOf
 [ a owl:Restriction ;
   owl:onProperty frac:observedIn ;
   owl:hasValue <http://oracc.museum.upenn.edu/epsd2/pager> ] .

# frequency assessment
epsd:a_water_n frac:frequency [ 
  a :EPSDFrequency;
  rdf:value "4683"^^xsd:int ].`
    </pre>

</div>

</div>

</div>

<div class="note">

`frac:Frequency` can be extended with additional filter conditions to define sub-corpora. For example, we can restrict the subcorpus to a particular time period, e.g., the Neo-Sumerian Ur III period:

<div class="beispiel">

<div>

<pre>                
# EPSD frequency for the Ur-III period (aat:300019910)
:EPSDFrequency_UrIII 
 rdfs:subClassOf :EPSDFrequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue aat:300019910 ] .

# frequency assessment for sub-corpus
epsd:a_water_n frac:frequency [ 
  a :EPSDFrequency_UrIII;
  rdf:value "2299"^^xsd:int ].` </pre>

</div>

</div>

</div>

</section>

<section>
    
## Attestation

```
###############
# attestation #
###############
```

back to ([Table of Contents](#table-of-contents))

Attestations constitute  a  special  form  of  citation  that  provide  evidence  for  the  existence  of  a  certain  lexical  phenomena; they can elucidate meaning or illustrate various  linguistic  features.

In  scholarly  dictionaries,  attestations  are  a  representative selection  from  the  occurrences  of  a  headword  in  a  textual corpus.  These  citations  often  consist  of  a quotation  accompanied  by  a  reference  to  the  source.  The  quoted  text  usually contains  the  occurrence  of  the  headword.

<div class="entity">

> --------
> ### Attestation (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Attestation](http://www.w3.org/nl/lemon/frac#Attestation)
>  An **Attestation** is a `frac:Observation` that represents one exact or normalized quotation  or  excerpt  from  a  source  document  that  illustrates a  particular  form,  sense,  lexeme  or  features  such  as  spelling variation,  morphology,  syntax,  collocation,  register.  An attestation SHOULD have an `rdf:value`, it CAN have a `frac:gloss`, and it SHOULD have a `frac:observedIn` or `frac:locus` object to identify the source of this material.
For an attestation, `rdf:value` represents the text of a quotation as represented in the original source. If that needs to be distinguished or is different from the way how it is represented in the dictionary, FrAC users should use `frac:gloss` for the latter purpose. 
> **SubClassOf:** `rdf:value` max 1 
> **SubClassOf:** `frac:Observation`
>
> ------
</div>

```
frac:Attestation
    rdfs:subClassOf frac:Observation ;
    vs:term_status "stable" .
```

> ----
> ### attestation (ObjectProperty)
> The property **frac:attestation** associates an attestation to the frac:Observable.  This  is  a  subproperty  of  `frac:citation` using concrete data as  evidence.
> **Domain:** `Observable`
> **Range:** `Attestation`
> **SubPropertyOf:** `citation`
>
> ---- 
</div>

```
frac:attestation
    a owl:ObjectProperty ;
    rdfs:domain frac:Observable ;
    rdfs:range frac:Attestation ;
    rdfs:subPropertyOf frac:citation ;
    vs:term_status "stable" .
```

> --------
> ### citation (ObjectProperty)
> The property **frac:citation** associates a  citation  to  the  `Observable`  citing  it.
> **Domain:**  `Observable`
>
> --------

``` 
frac:citation
    a owl:ObjectProperty ;
    rdfs:domain frac:Observable ;
    vs:term_status "tbc" .
```

In general, the object of a citation represents the successful act of citing an entity which can be referred to by a standardised bibliographic reference, cf. Peroni (2012) \cite{peroni2012fabio}: 

>[a Citation is] ``a conceptual directional link from a citing entity to a cited entity, created by a human performative act of making a citation, typically instantiated by the inclusion of a bibliographic reference  in the reference list of the citing entity, or by the inclusion within the citing entity of a link, in the form of an HTTP Uniform Resource Locator (URL), to a resource on the World Wide Web''. 

However, note that FrAC does not formally define a general "Citation" class to define the range of `citation`, but only provides `Attestation` as one specific possibility. Beyond attestations, different vocabularies have been suggested for linking bibliographical information, and we advise users of FrAC to make a consistent choice among them, adequate for their respective needs and the conventions of their users community. `frac:citation` serves as an interface to these external vocabularies. If the [CITO vocabulary](https://sparontologies.github.io/cito/current/cito.html) is used in a particular resource, their FrAC Citations can be defined as the subclass of CITO citations having <tt>frac:Observable</tt> as citing entity and attestations would correspond to citations with the <tt>cito:hasCitationCharacterization</tt> value <tt>citesAsEvidence</tt>. Other relevant vocabularies include, for example, [BIBFRAME](https://www.loc.gov/bibframe/), [FRBR](https://www.ifla.org/node/881) and [FaBiO](https://sparontologies.github.io/fabio/current/fabio.html), but also, generic vocabularies such as [schema.org](https://schema.org/citation).


> --------
> ### gloss (Property)

> The **gloss** of an attestation contains  the  text  content  of  an  attestation  *as  represented  within  a  dictionary*.  This property should not be used to provide direct quotations from the original data source, which should be represented by `rdf:value`. Instead, its recommended use is for representations that are either enriched (e.g., by annotations and metadata), amended (e.g., by expanding ligatures or omissions), simplified (e.g., by omissions from the original context, e.g., of the lexeme under consideration) or otherwise differentiated from the plain text representation of the context.
> **Domain:** `Attestation`
> **Range:** `xsd:String`  
>
> --------

```
frac:gloss
    a owl:DatatypeProperty ;
    rdfs:domain frac:Attestation ;
    rdfs:range xsd:string ;
    rdfs:comment "An attestation gloss is the representation of the attestation as provided in a lexical resource. This may contain, for example, amendments or additional comments. For the string as found in the original text, use rdf:value." ;
    vs:term_status "tbc" .
```

> Note: With `frac:gloss` and `rdf:value`, `frac:Attestation` provides *two* different properties to represent the context of an observable in any particular data source. `rdf:value` should provide information as found in the underlying corpus, e.g., a plain text string. If the dictionary provides a different representation, or if the attestation as given in an underlying dictionary has not yet been confirmed to match the context in the underlying corpus, applications should use `frac:gloss` instead of `rdf:value`. In other words, `rdf:value` corresponds to the representation of the context in the underlying corpus, `frac:gloss` to its representation in the underlying dictionary. If both are confirmed to be equal, use `rdf:value`.

As an example, for Old English *hwæt-hweganunges*, Bosworth (2014) gives the example `"Ða niétenu ðonne beóþ hwæthuguningas [MS. Cote. -hwugununges] ...`. In OntoLex-FrAC, this would be the `frac:gloss` because it contains additional information about spelling variation/normalized spelling not found found in the quoted source (`MS. Cote.`):

    <https://bosworthtoller.com/20070> a ontolex:LexicalEntry;
        frac:attestation [
            a frac:Attestation;
            rdf:value "Ða niétenu ðonne beóþ hwæthwugununges" ;
            frac:gloss "Ða niétenu ðonne beóþ hwæthuguningas [MS. Cote. -hwugununges] ..."
            # TODO: resolve literature pointers properly!
        ] .

> Bosworth, Joseph. “hwæt-hweganunges.” In _An Anglo-Saxon Dictionary Online_, edited by Thomas Northcote Toller, Christ Sean, and Ondřej Tichy. Prague: Faculty of Arts, Charles University, 2014. https://bosworthtoller.com/20070. [REFORMAT]

In many applications, it is desirable to specify the location of the occurrence of a headword in the quoted text of an attestation, for example, by means of character offsets. Different conventions for referencing strings by character offsets do exist, representative solutions are string URIs as provided by RCF5147 (for plain text) and NIF (all mimetypes), As different vocabularies can be used to establish locus objects, the FrAC vocabulary is underspecified with respect to the exact nature of the locus object. Accordingly, the <tt>locus</tt> property that links an attestation with its source takes any URI as object.

<div class="property">

> ----
> ### locus (Property)
> **frac:locus** points  to  the  location  at  which  the  relevant  word(s)  can  be  found.
> **Domain:** `Attestation`
> 
> ----
</div>

```
frac:locus
    a owl:ObjectProperty ;
    rdfs:domain frac:Attestation ;
    vs:term_status "stable" ;
    rdfs:comment """Points from an Observation to the exact location in the source material on where it is to be found. This can be, for example, a page in a book, the string URI of a passage in a text, a canonical reference to a passage in piece of literatur, or any Web Annotation selector. We have confirmed name, function and necessity of this property.
    When the locus is provided, it is not necessary to also refer to the source material as a whole. The existence of such a reference is nevertheless implied."""@en .
```

</div>

> Note: In humanities practice, locations (`frac:locus` objects) can be provided at different levels of granularity, e.g., referring to a particular text span within a text, to a verse, paragraph or chapter within which the text can be found, to a complete work, or a collection of works. Data providers should generally use `frac:observedIn` unless the the specific semantics require the use of `frac:locus`. In particular, if the location is a complete work (e.g., `dct:Text`) or a corpus identifiable by a URI (i.e., a `dct:Collection`), data providers should use the `frac:observedIn` property. For references within a work or to a collection without explicitly defined boundaries (e.g., `Plato` to designate all of Plato's preserved works as well as any statement ascribed to him from an unpreserved work), data providers should use `frac:locus`.

> Implementation note: as the type of data source is now to indicated by `dct:DMCIType`, we can merge `frac:locus` and `frac:observedIn`, again.


**example**:  [DiaMaNT (_Diachroon seMAntisch lexicon van de Nederlandse Taal_)](http://diamant.ivdnt.org/diamant-ui/) is a diachronic semantic computational  lexicon  of  Dutch,  at its core  formed by four scholarly historical dictionaries of  Dutch covering a language period from ca. 500 –  1976. The example below illustrates the combination of FrAC attestations with the [CITO](https://sparontologies.github.io/cito/current/cito.html) and [FRBR](http://purl.org/vocab/frbr/core#) vocabularies, as well as with the [NLP Interchange Format](https://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core/nif-core.html).

    diamant:entry_WNT_M030758 a ontolex:LexicalEntry ; 
        ontolex:sense diamant:sense_WNT_M030758_bet_207 .

    diamant:sense_WNT_M030758_bet_207 a ontolex:LexicalSense;
        rdfs:label "V.-" ;
    frac:attestation diamant:attestation_2108540 ; 
    skos:definition "Iemand een kat (of de kat) aan het  been  jagen...... iemand in moeilijkheden brengen." .

    diamant:attestation_2108540 a frac:Attestation ; 
        cito:hasCitedEntity diamant:cited_document_WNT_332819  ;
        cito:hasCitingEntity diamant:sense_WNT_M030758_bet_207; 
        frac:locus diamant:locus_2108540  ;
        frac:quotation "... dat men licht yemant de cat aen het been kan werpen," .

    diamant:locus_2108540 a diamant:Occurrence ; 
        nif:beginIndex 107 ;
        nif:endIndex 110 .

    diamant:cited_document_WNT_332819 a frbr:Manifestation ;
        frbr:embodimentOf diamant:expression_WNT_332819 ; 
        diamant:witnessYearFrom 1621 ;
        diamant:witnessYearTo 1621 .

    diamant:expression_WNT_332819 a frbr:Expression ; 
        dcterms:creator "N. V. REIGERSB." ; 
        dcterms:title "Brieven van Nicolaes van Reigersberch aan Hugo de Groot" ; 
        frbr:embodiment diamant:quotation_WNT_332819 .


Note: In the example above, NIF is not correctly used: NIF requires string URIs for loci, including the identification of the source document within the base URI and the identification of a context (this is instead provided via `hasCitedEntity`). To be revised or replaced.

Note: Update example to https://www.dbnl.org/tekst/groo001brie04_01/groo001brie04_01_0003.php?q=dat%20men%20licht%20yemant%20de%20cat%20aen%20het%20been%20kan%20werpen;#hl1

</section>

<section>

## Collocations

```
###############
# collocation #
###############
```

back to ([Table of Contents](#table-of-contents))

Collocation analysis is an important tool for lexicographical research and instrumental for modern NLP techniques. It has been the mainstay of 1990s corpus linguistics and continues to be an area of active research in computational philology and lexicography.

Collocations are usually defined on surface-oriented criteria, i.e., as a relation between forms or lemmas (lexical entries), not between senses, but they can be analyzed on the level of word senses (the sense that gave rise to the idiom or collocation). Indeed, collocations often contain a variable part, which can be represented by a <tt>ontolex:LexicalConcept</tt>.

Collocations can involve two or more words, they are thus modelled as an <tt>rdfs:Container</tt> of <tt>frac:Observables</tt>s. Collocations may have a fixed or a variable word order. Where fixed word order is required, the collocation must be defined as a sequence (<tt>rdf:Seq</tt>), otherwise, the default interpretation is as an ordered set (<tt>rdf:Bag</tt>).

Collocations obtained by quantitative methods are characterized by their method of creation (<tt>dct:description</tt>), their collocation strength (<tt>rdf:value</tt>), and the corpus or data source used to create them (<tt>frac:observedIn</tt>). Collocations share these characteristics with other `frac:Observation`s and thus, these are inherited from the abstract <tt>frac:Observation</tt> class.


<div class="entity">

> ---
> ### Collocation (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Collocation](http://www.w3.org/nl/lemon/frac#Collocation)
> A **Collocation** is a <tt>frac:Observation</tt> that describes the co-occurrence of two or more <tt>frac:Observables</tt>s within the same context window and that can be characterized by their collocation score (or weight, <tt>frac:cScore</tt>) in a particular data source (<tt>frac:observedIn</tt>). Collocations are both observations and observables, and they are modelled as an aggregate (`rdfs:Container`) of observables.
> **SubClassOf:** <tt>frac:Observation, rdfs:Container, frac:Observable</tt>
> **rdfs:member:** only <tt>frac:Observable</tt>
> **SubClassOf:** `frac:head` max 1
>
> ---
</div>

```
frac:Collocation
    rdfs:subClassOf rdfs:Container, frac:Observable, frac:Observation, [
        a owl:Restriction ;
        owl:minQualifiedCardinality "2"^^xsd:nonNegativeInteger ;
        owl:onClass frac:Observable ;
        owl:onProperty rdfs:member
    ] ,
    [
        a <http://www.w3.org/2002/07/owl#Restriction> ;
        <http://www.w3.org/2002/07/owl#allValuesFrom> <http://www.w3.org/ns/lemon/frac#Observable> ;
        <http://www.w3.org/2002/07/owl#onProperty> <http://www.w3.org/2000/01/rdf-schema#member>
    ] ;
    vs:term_status "stable" .
```
    
Collocations are collections of `frac:Observables`, and formalized as <tt>rdfs:Container</tt>, i.e., <tt>rdf:Seq</tt> or <tt>rdf:Bag</tt>. The elements of any collocation can be accessed by `rdfs:member`. In addition, the elements of an ordered collocation (`rdfs:subClassOf rdf:Seq`) can be accessed by means of numerical indices (`rdf:_1`, `rdf:_2`, etc.). 
    
By default, <tt>frac:Collocation</tt> is insensitive to word order. If a collocation is word order sensitive, it should be defined as `rdfs:subClassOf rdf:Seq`. Collocation analysis typically involves additional parameters such as the size of the context window considered. Such information can be provided in human-readable form in <tt>dct:description</tt>. 

<div class="note">
> Note that FrAC collocations can be used to represent collocations both in the lexicographic sense (as complex units of meaning) and in the quantative sense (as determined by collocation metrics over a particular corpus), but that the quantitative interpretation is the preferred one in the context of FrAC. To mark collocations in the lexicographic sense as such, they can be assigned a corresponding `lexinfo:termType`, e.g., by means of `lexinfo:idiom`, `lexinfo:phraseologicalUnit` or `lexinfo:setPhrase`. If explicit sense information is being provided, the recommended modelling is by means of `ontolex:MultiWordExpression` and the OntoLex-Decomp module rather than `frac:Collocation`. To provide collocation scores about a `ontolex:MultiWordExpression`, it can be linked via `rdfs:member` with a `frac:Collocation`.
</div>
    
Collocations are `frac:Observable`s, i.e., they can be ascribed `frac:frequency`, `frac:attestation`, `frac:embedding`, they can be described in terms of their (embedding) similarity, and they can be nested inside larger collocations.
    
Collocations can be described in terms of various collocation scores. If scores for multiple metrics are being provided, these should not use the generic `rdf:value` property, but a designated subproperty of `frac:cScore`:

<div class="property">

> ---
> ### cScore (property)
> **URI:** [http://www.w3.org/nl/lemon/frac#Collocation](http://www.w3.org/nl/lemon/frac#cScore)
> **Collocation score** is a subproperty of `rdf:value` that provides the value for one specific type of collocation score for a particular collocation in its respective corpus. Note that this property should not be used directly, but instead, its respective sub-properties for scores of a particular type.
> **SubPropertyOf:** <tt>rdf:value</tt>
> **domain:** <tt>frac:Collocation</tt>
>
> ---
</div>

```
frac:cScore
    rdfs:subPropertyOf rdf:value ;
    rdfs:domain frac:Collocation ;
    vs:term_status "stable" .
```

FrAC defines a number of popular collocation metrics as sub-properties of `frac:cScore`:

- `frac:relFreq` (*relative frequency*): <img src="https://render.githubusercontent.com/render/math?math=RF(x,y|x) = \frac{f_{xy}}{f_x} (= R_x)"> (asymmetric, requires `frac:head`)
    ```frac:relFreq rdfs:subPropertyOf frac:cScore . ```
- `frac:pmi` (*pointwise mutual information*, sometimes referred to as *MI-score* or *association ratio*, cf. [Church and Hanks 1990, via Ewert 2005](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf): <img src="https://render.githubusercontent.com/render/math?math=PMI(x,y)=log_2 \frac{f_{xy} N}{f_x f_y}"> 
    ```frac:pmi rdfs:subPropertyOf frac:cScore .```
- `frac:pmi2` (*PMI²-score*): <img src="https://render.githubusercontent.com/render/math?math=PMI^2(x,y)=log_2 \frac{f_{xy}^2 N}{f_x f_y}">
    ```frac:pmi2 rdfs:subPropertyOf frac:cScore . ```
- `frac:pmi3` (*PMI³-score*, cf. [Daille 1994 in Ebert 2005, p.89](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf)): <img src="https://render.githubusercontent.com/render/math?math=PMI^3(x,y)=log_2 \frac{f_{xy}^3 N}{f_x f_y}">
    ```frac:pmi3 rdfs:subPropertyOf frac:cScore .```
- `frac:pmiLogFreq` (*PMI.log-f*, *salience*, formerly default metric in SketchEngine): <img src="https://render.githubusercontent.com/render/math?math=PMI.log-f(x,y)=log_2 \frac{f_{xy} N}{f_x f_y} \times log f_{xy}">
    ```frac:pmiLogFreq rdfs:subPropertyOf frac:cScore .```
- `frac:dice` (*Dice coefficient*): <img src="https://render.githubusercontent.com/render/math?math=Dice(x,y)=\frac{2 f_{xy}}{f_x %2B f_y}">
    ```frac:dice rdfs:subPropertyOf frac:cScore .```
- `frac:logDice` (default metric in SketchEngine, [Rychly 2008](https://www.sketchengine.eu/wp-content/uploads/2015/03/Lexicographer-Friendly_2008.pdf)): <img src="https://render.githubusercontent.com/render/math?math=LogDice(x,y)=14 %2B log_2 Dice(x,y)">
    ```frac:logDice rdfs:subPropertyOf frac:cScore .```
- `frac:minSensitivity` (*minimum sensitivity*, cf. [Pedersen 1998](https://www.sketchengine.eu/wp-content/uploads/ske-statistics.pdf)): <img src="https://render.githubusercontent.com/render/math?math=MS(x,y)=min(R_x,R_y)">
    ```frac:minSensitivity rdfs:subPropertyOf frac:cScore .```

with
    
- <img src="https://render.githubusercontent.com/render/math?math=x,y"> the (head) word and its collocate
- <img src="https://render.githubusercontent.com/render/math?math=f_x"> the number of occurrences of the word *x*
- <img src="https://render.githubusercontent.com/render/math?math=f_y"> the number of occurrences of the word *y*
- <img src="https://render.githubusercontent.com/render/math?math=f_{xy}"> the number of co-occurrences of the words *x* and *y*
- <img src="https://render.githubusercontent.com/render/math?math=R_y = \frac{f_{xy}}{f_{y}}"> relative frequency of *y*
- <img src="https://render.githubusercontent.com/render/math?math=N"> the total number of words in the corpus, this should be documented in `dct:description`

In addition to collocation scores, also statistical independence tests are being employed as collocation scores:

- `frac:logLikelihood` (*log likelihood*, *G²* [Dunning 1993, via Ewer 2005](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf))
    ```frac:logLikelihood rdfs:subPropertyOf frac:cScore .```
- `frac:tScore` (*Student's t test*, *T-score*, cf. [Church et al. 1991, via Ewert 2005, p.82](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf) ): <img src="https://render.githubusercontent.com/render/math?math=T(x,y)=\frac{f_{xy}-\frac{(f_x f_y)}{N}}{\sqrt{f_{xy}}}">
    ```frac:tScore rdfs:subPropertyOf frac:cScore .```
- `frac:chi2` (*Person's Chi-square test* [Manning 1999](https://nlp.stanford.edu/fsnlp/) ): <img src="https://render.githubusercontent.com/render/math?math=\chi^2(x,y)=\frac{N(O_{11}O_{22}-O_{12}O_{21})^2}{(O_{11} %2B O_{12})(O_{11} %2B O_{21})(O_{12} %2B O_{22})(O_{21} %2B O_{22})}">
    ```frac:chi2 rdfs:subPropertyOf frac:cScore .```

with
- <img src="https://render.githubusercontent.com/render/math?math=O_{11}=f_{xy}"> 
- <img src="https://render.githubusercontent.com/render/math?math=O_{12}=f_{y} - f_{xy}"> 
- <img src="https://render.githubusercontent.com/render/math?math=O_{21}=f_{x} - f_{xy}"> 
- <img src="https://render.githubusercontent.com/render/math?math=O_{22}=N - f_{x} - f_{y} %2B 2f_{xy}"> 
- <img src="https://render.githubusercontent.com/render/math?math=N"> the total number of words in the corpus 
    
In addition to classical collocation metrics as established in computational lexicography and corpus linguistics, related metrics can also be found in different disciplines and are represented here as subproperties of frac:cScore, as well. This includes metrics for association rule mining. In this context, an association  rule (collocation) <img src="https://render.githubusercontent.com/render/math?math=x \rightarrow y"> means that the existence of word *x* implies the existence of word *y* 

- `frac:support` (the *support* is an indication of how frequently the rule appears in the dataset): <img src="https://render.githubusercontent.com/render/math?math=support(x \rightarrow y) = \frac{f_{xy}}{N}"> (with *N* the total number of collocations)
    ```frac:support rdfs:subPropertyOf frac:cScore .```
- `frac:confidence` (the *confidence* is an indication of how often the rule has been found to be true): <img src="https://render.githubusercontent.com/render/math?math=confidence(x \rightarrow y) = \frac{f_{xy}}{f_{x}}">
    ```frac:confidence rdfs:subPropertyOf frac:cScore .```
- `frac:lift` (the *lift* or *interest* of a rule measures how many times more often *x* and *y* occur together than expected if they are statistically independent): <img src="https://render.githubusercontent.com/render/math?math=lift(x \rightarrow y) = \frac{f_{xy}}{f_{x}f_{y}}">
    ```frac:lift rdfs:subPropertyOf frac:cScore .```
- `frac:conviction` (the *conviction* of a rule is interpreted as the ratio of the expected frequency that *x* occurs without *y*, i.e., the frequency that the rule makes an incorrect prediction, if *x* and *y* are independent divided by the observed frequency of incorrect predictions): <img src="https://render.githubusercontent.com/render/math?math=conviction(x \rightarrow y) = \frac{(1 - f_{y})f_{x}}{f_{x} - f_{xy}}">
    ```frac:conviction rdfs:subPropertyOf frac:cScore .```
 
> Note: As OntoLex does not provide a generic inventory for grammatical relations, scores defined for grammatical relations are omitted (cf. https://www.sketchengine.eu/wp-content/uploads/ske-statistics.pdf). However, these may be defined by the user.
    
Many of these metrics are asymmetric and distinguish the lexical element they are about (the head) from its collocate(s). If such metrics are provided, a collocation should explicitly identify its head:

<div class="property">

> ---
> ### head (property)
> **URI:** [http://www.w3.org/nl/lemon/frac#Collocation](http://www.w3.org/nl/lemon/frac#head)
> The **head** property identifies the element of a collocation that its scores are about. A collocation must not have more than one head.
> **domain:** <tt>frac:Collocation</tt>
> **range:** <tt>frac:Observable</tt>
>
> ---
</div>

```
frac:head
    a owl:ObjectProperty ;
    rdfs:domain frac:Collocation ;
    rdfs:range frac:Observable ;
    vs:term_status "stable" .
```

As an example, the relative frequency score is the number of occurrences of a collocation relative to the overall frequency of its head.
    
> Note: The function of the property `frac:head` is restricted to indicate the directionality of asymmetric collocation scores. It must not be confused with the notion of "head" in certain fields of linguistics, e.g., dependency syntax. 
> Note: `frac:head` should not be used to model the structure of collocation dictionaries, i.e., the selection of collocations to be displayed with a particular head word. For these functions, please resort to the *lexicog:` vocabulary. 
    
The most elementary level of a collocation is an n-gram, as provided, for example, by [Google Books](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html), which provide n-gram frequencies per publication year as tab-separated values. For 2008, the 2012 edition provides the following statistics for the bigram _kill_ + _switch_.

<div class="beispiel">

<div>

<pre>
# form-form bigrams
kill    switch  2008    199 121

# form-lexeme bigrams
kill    switch_NOUN 2008    187 115
kill    switch_VERB 2008    8   8

# lexeme-form bigrams
kill_ADJ    switch  2008    70  48
kill_NOUN   switch  2008    89  64
kill_VERB   switch  2008    40  30

# lexeme-lexeme bigrams
kill_VERB   switch_VERB 2008    2   2
kill_NOUN   switch_NOUN 2008    83  61
kill_VERB   switch_NOUN 2008    35  26
kill_ADJ    switch_NOUN 2008    69  48
kill_NOUN   switch_VERB 2008    6   6` </pre>

</div>

</div>

In this example, forms are string values (cf. <tt>ontolex:LexicalForm</tt>), lexemes are string values with parts-of-speech (cf. <tt>ontolex:LexicalEntry</tt>). A partial ontolex-frac representation is given below:

<div class="beispiel">

<div>

<pre>
# kill (verb)
:kill_v a ontolex:LexicalEntry;
  lexinfo:partOfSpeech lexinfo:verb;
  ontolex:canonicalForm :kill_cf.

# kill (canonical form)
:kill_cf ontolex:writtenRep "kill"@en.

# switch (noun)
:switch_n a ontolex:LexicalEntry;
  lexinfo:partOfSpeech lexinfo:noun;
  ontolex:canonicalForm :switch_cf.

# switch (canonical form)
:switch_cf ontolex:writtenRep "switch"@en.

# form-form bigrams
[ rdf:_1 :kill_cf; rdf:_2 :switch_cf ] a frac:Collocation, rdf:Seq ;
  rdf:value "199";
  dct:description "2-grams, English Version 20120701, word frequency";
  frac;observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.

[ rdf:_1 :kill_cf; rdf:_2 :switch_cf ] a frac:Collocation, rdf:Seq ; 
  rdf:value "121";
  dct:description "2-grams, English Version 20120701, document frequency";
  frac:observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.

# form-lexeme bigrams
[ rdf:_1 :kill_cf; rdf:_2 :switch_n ] a frac:Collocation, rdf:Seq ;
  rdf:value "187";
  dct:description "2-grams, English Version 20120701, word frequency";
  frac:observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.

[ rdf:_1 :kill_cf, rdf:_2 :switch_n ] a frac:Collocation, rdf:Seq ;
  rdf:value "115";
  dct:description "2-grams, English Version 20120701, document frequency";
  frac:observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.` </pre>

</div>

</div>

The second example illustrates more complex types of collocation are provided as provided by the [Wortschatz](http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012) portal (scores and definitions as provided for [beans](http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012&word=beans), [spill the beans](http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012&word=spill+the+beans), etc.

<div class="beispiel">

<div>

    @prefix wsen: <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012&word=>
    # selected lexical entries
    # (we assume that every Wortschatz word is an independent lexical entry)
    wsen:beans a ontolex:LexicalEntry;
      ontolex:canonicalForm/ontolex:writtenRep "beans"@en.
    wsen:spill a ontolex:LexicalEntry;
      ontolex:canonicalForm/ontolex:writtenRep "spill"@en.
    wsen:green a ontolex:LexicalEntry;
      ontolex:canonicalForm/ontolex:writtenRep "green"@en.
    wsen:about a ontolex:LexicalEntry;
      ontolex:canonicalForm/ontolex:writtenRep "about"@en

    # collocations, non-lexicalized
    [ rdfs:member wsen:spill, wsen:beans ] a frac:Collocation;
      rdf:value "182";
      dct:description "cooccurrences in the same sentence, unordered";
      frac:observedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>.

    [ rdf:_1 wsen:green; rdf:_2 wsen:beans ] a frac:Collocation, rdf:Seq ;
      rdf:value "778";
      dct:description "left neighbor cooccurrence";
      frac:observedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>;
      lexinfo:termType lexinfo:idiom.

     [ rdf:_1 wsen:beans; rdf:_2 wsen:about ] a frac:Collocation, rdf:Seq;
      rdf:value "35";
      dct:description "right neighbor cooccurrence";
      frac:observedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>;
      lexinfo:termType lexinfo:idiom.

    # multi-word expression, lexicalized (!)
    wsen:spill+the+beans a ontolex:MultiWordExpression;
      ontolex:canonicalForm/ontolex:writtenRep "spill the beans"@en.

    [ rdfs:member wsen:beans, wsen:spill+the+beans ] a frac:Collocation;
      rdf:value "401";
      dct:description "cooccurrences in the same sentence, unordered";
      frac:obsevedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>.` </pre>

</div>

</div>

<div class="note">

> Again, it is recommended to define resource-specific subclasses of <tt>frac:Collocation</tt> with default values for <tt>dct:description</tt>, <tt>frac:obsevedIn</tt>, and (where applicable) <tt>lexinfo:termType</tt>.

</div>

</section>

<section>

## Embeddings

```
#############
# embedding #
#############
```

back to ([Table of Contents](#table-of-contents))


In distributional semantics, the contexts in which a word is attested are taken to define its meaning. Contextual similarity is thus a correlate of semantic similarity. Different representations of context are possible, the most prominent model to date is the form of a vector. A word vector can be created, for example, by means of a reference list of vocabulary items, where every reference word is associated with a fixed position, e.g., _ship_ with position 1, _ocean_ with 2, _sky_ with 3, etc. Given a corpus (and a selection criterion for collocates, e.g., within the same sentence), every word in the corpus can be described by the frequency that a reference word occurred as a collocate in the corpus. Assume we want to define the meaning of _frak_, with (exactly) the following attestations in our sample corpus (random samples from [wikiquote](https://en.wikiquote.org/wiki/Battlestar_Galactica_(2003))):

*   _It's in the frakking ship!_
*   _Have you lost your frakkin' mind?_
*   _Oh, for frak's sake, let me see if I can make heads or tails of it._
*   _It's a frakking Cylon._
*   _Our job isn't to be careful, it's to shoot Cylons out of the frakking sky!_

With the following list of reference words: <tt>(ship, ocean, lose, find, brain, mind, head, sky, Cylon, ...)</tt>, we obtain the vector <tt>(1,0,1,0,0,1,1,1,2,...)</tt> for the lemma (lexical entry) _frak_. For practical applications, these vectors are projected into lower-dimensional spaces, e.g., by means of statistical (Schütze 1993) or neural methods (Socher et al. 2011). The process of mapping a word to a numerical vector and its result are referred to as "word embedding". Aside from collocation counts, other methods for creating word embeddings do exist, but they are always defined relative to a corpus.

Embeddings have become a dominating paradigm in natural language processing and machine learning, but, if compiled from large corpora, they require long training periods and thus tend to be re-used. However, embedding distributions often use tool-specific binary formats (cf. [Gensim](https://radimrehurek.com/gensim/models/word2vec.html)), and thus a portability problem arises. CSV and related formats (cf. [SENNA embeddings](https://github.com/baojie/senna/tree/master/embeddings)) are a better alternative, but their application to sense and concept embeddings (as provided, for example, by Rothe and Schütze 2017) is problematic if their distribution is detached from the definition of the underlying sense and concept definitions. With frac, Ontolex-lemon provides a vocabulary for the conjoint publication and sharing of embeddings and lexical information at all levels: non-lemmatized words (ontolex:Form), lemmatized words (ontolex:LexicalEntry), phrases (ontolex:MultiWordExpression), lexical senses (ontolex:LexicalSense) and lexical concepts (ontolex:LexicalConcept).

<div class="note">

> We focus on _publishing and sharing_ embeddings, not on their processing by means of Semantic Web formalisms, and thus, embeddings are represented as untyped or string literals with whitespace-separated numbers. If necessary, more elaborate representations, e.g., using rdf:List, may subsequently be generated from these literals.

</div>

Lexicalized embeddings provide their data via <tt>rdf:value</tt>, and should be published together with their metadata, most importantly

*   procedure/method (<tt>dct:description</tt> with free text, e.g., "CBOW", "SKIP-GRAM", "collocation counts")
*   corpus (<tt>frac:observedIn</tt>)
*   dimensionality (<tt>dct:extent</tt>)


<div class="entity">

> ---
> ### Embedding (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Embedding](http://www.w3.org/nl/lemon/frac#Embedding)
> An **Embedding** is a representation (of a given frac:Observable (see <tt>frac:embedding</tt>) in a numerical feature space. It is defined by the methodology used for creating it (<tt>dct:description</tt>), the URI of the corpus or language resource from which it was created (<tt>frac:observedIn</tt>). The literal value of an Embedding is  provided by <tt>rdf:value</tt>). In OntoLex-FrAC, embeddings are `frac:Observation`s that are obtained from a particular corpus.
> **SubClassOf:** rdf:value exactly 1 xsd:string, frac:observedIn exactly 1, dct:description min 1
> **SubClassOf:** `frac:Observation`
>
> ---
</div>

```
frac:Embedding
    rdfs:subClassOf frac:Observation, [
        a owl:Restriction ;
        owl:onDataRange xsd:int ;
        owl:onProperty dct:extent ;
        owl:qualifiedCardinality "1"^^xsd:nonNegativeInteger
    ] ;
    vs:term_status "stable" .
```

<div class="entity">

> ----
> ### embedding (ObjectProperty)
> **URI:** [http://www.w3.org/nl/lemon/frac#embedding](http://www.w3.org/nl/lemon/frac#embedding)
> The property **embedding** is a relation that maps a frac:Observable into a numerical feature space. An embedding is a structure-preserving mapping in the sense that it encodes and preserves contextual features of a particular frac:Observable (or, an aggregation over all its attestations) in a particular corpus.
> **rdfs:range** ontolex:Element
> **rdfs:domain** frac:Embedding
>
> ---
</div>

```
frac:embedding
    a owl:ObjectProperty ;
    rdfs:domain frac:Observable ;
    rdfs:range frac:Embedding ;
    vs:term_status "stable" .
```


</div>

<div class="note">
The use of the term "embedding" adopted here follows the terminology in mathematics: For the embedding of an object  _X_  in another object  _Y_, the embedding _f_ :  _X_  →  _Y_  (alternatively _f_ : _X_ ↪ _Y_) is defined as an  injective, structure-preserving map (morphism). (Rephrased from [https://en.wikipedia.org/wiki/Embedding](https://en.wikipedia.org/wiki/Embedding))  For "embedding" in the sense conventionally used in language technology, see the subclass frac:FixedSizeVector.</div>

<div class="note">
FrAC does not define the type of literal provided in the rdf:value of an embedding. The following examples use JSON literals, this is, however, informative, not normative. Alternative encodings based on tool-specific string representations (e.g., whitespace-separated numbers or comma-separated values) are possible. For string literals or untyped literal values, it is recommended to provide a regular expression that defines how to parse it as part of the description of the Embedding. As an example, the following regular expression for parsing embedding values can be used to parse whitespace-separated numbers (example in Perl):

`split(/[^0-9\.,\-]+/, $value)`

This means that doubles should be provided in the conventional format, not using the exponent notation.

Also note that different subclasses of frac:Embedding may have different encoding strategies.
</div>

<div class="entity">

> ---
> ### FixedSizeVector (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#FixedSizeVector](http://www.w3.org/nl/lemon/frac#FixedSizeVector)
> A **FixedSizeVector** is the value of a frac:embedding into a fixed-size numerical feature space. The literal value (<tt>rdf:value</tt>) of a FixedSizeVector is a list of numbers. The dimensionality of the feature space should be encoded by dct:extent.
> **SubClassOf:** Embedding, dct:extent exactly 1
>
> ---
</div>

```
frac:FixedSizeVector
    rdfs:subClassOf frac:Embedding ;
    vs:term_status "stable" .
```

Word, sense or concept embeddings as conventionally used in language technology are fixed size vectors. The 50-dimensional [GloVe](https://nlp.stanford.edu/projects/glove/) 6B (Wikipedia 2014+Gigaword 5) embedding for _frak_ is given below:

<tt>frak 0.015246 -0.30472 0.68107 -0.59727 -0.95368 -1.0931 0.58783 -0.19128 0.49108 0.61215 -0.14967 0.68197 0.22723 0.38514 -0.54721 -0.71187 0.21832 0.59857 0.1076 -0.23619 -0.86604 -0.91168 0.26087 -0.42067 0.60649 0.80644 -1.0477 0.67461 0.34154 -0.072511 -1.01 0.35331 -0.35636 0.9764 -0.62665 -0.29075 0.50797 -1.3538 0.18744 0.27852 -0.22557 -1.187 -0.11523 -0.078265 0.29849 0.22993 -0.12354 0.2829 1.0697 0.015366</tt>

As a lemma (LexicalEntry) embedding, this can be represented as follows:

<div class="beispiel">

<div>

<pre>
:frak a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "frak"@en;
  frac:embedding [ 
    a frac:FixedSizeVector;
    rdf:value "[ 0.015246 , -0.30472 , 0.68107,  ... ]"^^rdf:JSON;
    frac:observedIn
      &lt;http://dumps.wikimedia.org/enwiki/20140102/>,
      &lt;https://catalog.ldc.upenn.edu/LDC2011T07>;
      # note: two values for frac:obseredIn entails that these are owl:sameAs
    dct:extent 50^^^xsd:int;
    dct:description "GloVe v.1.1, documented in Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014\. GloVe: Global Vectors for Word Representation, see https://nlp.stanford.edu/projects/glove/; uncased"@en. ].`
    </pre>

</div>

</div>

In this example, the rdf:value of the embedding is represented my a JSON array (abbreviated).

<div class="note">

As with <tt>frac:Frequency</tt>, we recommend defining resource-specific subclasses of <tt>frac:Embedding</tt> in order to reduce redundancy in the data:

<div class="beispiel">

<div>

<pre>
 # resource-specific embedding class
:GloVe6BEmbedding_50d rdfs:subClassOf frac:FixedSizeVector;
  rdfs:subClassOf 
    [ a owl:Restriction;
      owl:onProperty frac:observedIn;
      owl:hasValue
          &lt;http://dumps.wikimedia.org/enwiki/20140102/>,
          &lt;https://catalog.ldc.upenn.edu/LDC2011T07> ],
    [ a owl:Restriction;
      owl:onProperty rdf:value;
      owl:allValuesFrom rdf:JSON ],
    [ a owl:Restriction;
      owl:onProperty dct:extent;
      owl:hasValue 50^^xsd:int ],
    [ a owl:Restriction;
      owl:onProperty dct:description;
      owl:hasValue "GloVe v.1.1, documented in Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014\. GloVe: Global Vectors for Word Representation, see https://nlp.stanford.edu/projects/glove/; uncased"@en. ].

# embedding assignment
:frak a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "frak"@en;
  frac:embedding [ 
    a :GloVe6BEmbedding_50d;
    rdf:value "[ 0.015246 , -0.30472 , 0.68107 ,  ... ]"^^rdf:JSON.`</pre>

</div>

</div>

</div>

<div class="note">

Examples for non-word embeddings:

*   [AutoExtend](http://www.cis.lmu.de/~sascha/AutoExtend/): (a method to build) synset and lexeme embeddings, data [here](http://www.cis.lmu.de/~sascha/AutoExtend/embeddings.zip)
*   [SenseGram](https://github.com/uhh-lt/sensegram): sense embeddings, data [here](http://ltdata1.informatik.uni-hamburg.de/sensegram/)
*   [Vec2Synset](http://tudarmstadt-lt.github.io/vec2synset/): (a method to build) WordNet synset (= LexicalConcept) embeddings
*   [Character embeddings](https://minimaxir.com/2017/04/char-embeddings/) are probably beyond the scope of OntoLex, unless characters are regarded LexicalEntries. (Which they could, for languages such as Chinese or Sumerian certainly, but also for Western languages -- given the fact that character-level pseudo entries are sometimes used in dictionaries to describe the phonology and orthography of a language. This is the case, for example, for Grimm's [Deutsches Wörterbuch](http://woerterbuchnetz.de/cgi-bin/WBNetz/wbgui_py?sigle=DWB).)

</div>

</section>

<section>

<div class="entity">

> ---
> ### TimeSeries (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#TimeSeries](http://www.w3.org/nl/lemon/frac#TimeSeries)
> A **TimeSeries** is a sequence of observations represented as numerical values, e.g., sensor data. Every point in the sequence is represented by a fixed number of numerical values. The time series is the concatenation of these values. The obligatory attribute <tt>dct:extent</tt> defines the number of observations (dimensionality) for every individual point of time. 
> **SubClassOf:** Embedding, dct:extent exactly 1
>
> ---
</div>

```
frac:TimeSeries
    rdfs:subClassOf frac:Embedding ;
    vs:term_status "stable" .
```

Note: name to be discussed. Maybe "Sequence".
Example to be provided by Manolis and Sander.
...

Note: Other embeddings are usually obtained by aggregation over multiple attestations in a corpus. TimeSeries, however, can also encode a single observation that serves as a prototype.

Other examples of time series:
- a sequence of contextualized word embeddings to represent longer phrases, e.g., in attention-based neural architectures [REF: Bahdanau, D., Cho, K., & Bengio, Y. (2015, January). Neural machine translation by jointly learning to align and translate. In _3rd International Conference on Learning Representations, ICLR 2015_. -- this ] 
- formant analysis as provided in phonetic analysis by Praat [REF: Boersma, Paul; van Heuven, Vincent (2001). ["Speak and unSpeak with Praat"](http://www.fon.hum.uva.nl/paul/papers/speakUnspeakPraat_glot2001.pdf)  (PDF). _Glot International_. **5** (9/10): 341–347.]

<div class="entity">

> ---
> ### BagOfWords (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#BagOfWords](http://www.w3.org/nl/lemon/frac#TimeSeries)
> For any frac:Observable, a **frac:BagOfWords** represents the collocates it occurs with in a particular corpus. In a weighted bag of words, every collocate is stored together with a frequency, confidence score or association weight. A bag of words must not define a dct:extent.
>
> **SubClassOf:** Embedding, dct:extent exactly 0
>
> ---
</div>

```
frac:BagOfWords
    rdfs:subClassOf frac:Embedding ;
    vs:term_status "stable" .
```

Bags of words can be compared to word embeddings (in languagte technology) in the sense that they represent infinite-dimensional, uncompressed frequency counts obtained from the aggregation over attestations in a corpus. The interpretability of their respective numerical dimensions, however, depends on the lexical provided along with it, so the normal data structure of a bag of words is not a vector, but a map (from collocates to weights, frequencies or association scores) or a set (of collocates, assuming each collocate is equally weighted). The encoding of the rdf:value must be specified in the dct:description. The example below uses an rdf:JSON literal representing a map. 

    
Example taken from [Wortschatz](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=frac#coocs), collocations of _frac_ (significant collocates in the same sentence), with frequency scores provided, filtered for significance (log-likelihood):

[sand](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=sand) (508), [mining](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=mining) (82), [Chesterland-based](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Chesterland-based) (75), [wells](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=wells) (73), [DNR](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=DNR) (73), [Silica](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Silica) (53), [fluid](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fluid) (52), [category](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=category) (51), [spill](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=spill) (49), [rigs](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=rigs) (48), [New Canaan](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=New+Canaan) (48), [oil](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=oil) (47), [drilling](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=drilling) (46), [County](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=County) (45), [shale](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=shale) (45), [mine](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=mine) (43), [Permian](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Permian) (41), [tons](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=tons) (40), [Canaan](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Canaan) (39), [gas](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=gas) (39), [More](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=More) (38), [fracturing](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fracturing) (38), [Texas](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Texas) (37), [Monroe](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Monroe) (35), [hydraulic](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=hydraulic) (35), [per](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=per) (35), [judge’s](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=judge%E2%80%99s) (35), [plant](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=plant) (34), [miner](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=miner) (34), [fluids](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fluids) (34), [Alpine](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Alpine) (33), [company](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=company) (33), [crews](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=crews) (30), [producer](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=producer) (28), [used](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=used) (26), [disposal](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=disposal) (25), [million](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=million) (24), [chemicals](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=chemicals) (23), [premium](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=premium) (22), [approximately](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=approximately) (22), [raw](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=raw) (21), [coal](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=coal) (20), [stages](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=stages) (20), [review](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=review) (20), [permit](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=permit) (18), [water](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=water) (18), [industry](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=industry) (18), [industrial](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=industrial) (17), [fees](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fees) (16), [production](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=production) (16), [attorney](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=attorney) (15), [lines](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=lines) (14), [active](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=active) (13), [Canadian](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Canadian) (12), [feet](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=feet) (12), [demand](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=demand) (12), [county](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=county) (11), [River](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=River) (11), [major](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=major) (11), [in](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=in) (11)

<div class="beispiel">

<div>

<pre>
:frac a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "frac"@en;
  frac:embedding [ 
    a frac:BagOfWords;
    dct:description "Cooccurrences of a word are those words that occur 
    noticeably often together with it. This may be the case as immediate 
    left neighbour, as immediate right neighbour, or in the same sentence. 
    The relevance of a cooccurrence is measured using a significance 
    measure; cooccurrences are ordered by their significance. At the 
    _Leipzig Corpora Collection_ the log-likelihood ratio is used as significance 
    measure and word pairs of little significance are removed.";
    frac:observedIn &lt;https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=frac>;
    rdf:value " { \"sand\" : \"508\" , \"mining\" : \"82\" , ... }"^^rdf:JSON.`
    </pre>
</div>

</div>

</div>

> Note: It is important to not confuse `frac:BagOfWords` and `frac:Collocation`. Both represent words in their context, but they differ in their usage and interpretation. A bag of words is an aggregation over *all* contexts that a word occurs in. A collocation represents *one* specific context constellation and its likelihood to occur for the word.

The modelling described so far pertains to static (non-contextualized) embeddings. 
Since 2018, static word and concept embeddings have been increasingly replaced by contextualized (dynamic) embeddings. For these, the embedding is not a property of the observable itself, but of the observable in a particular context (i.e., an attestation). This is modelled by means of `frac:attestationEmbedding`.

<div class="entity">

> ----
> ### attestationEmbedding (ObjectProperty)
> **URI:** [http://www.w3.org/nl/lemon/frac#embedding](http://www.w3.org/nl/lemon/frac#embedding)
> The property **attestation embedding** is a relation that maps an attestation of a particular observable into a numerical feature space. The string representation of the attestation should represent the necessary context that the respective embedding is calculated from.
> **rdfs:domain** frac:Attestation
> **rdfs:range** frac:Embedding
>
> ---
</div>


```
frac:attestationEmbedding
    a owl:ObjectProperty ;
    rdfs:domain frac:Attestation ;
    rdfs:range frac:Embedding ;
    vs:term_status "stable" .
```

TODO: example attestation embedding

</section>

<section>

## Similarity

```
##############
# similarity #
##############
```

back to ([Table of Contents](#table-of-contents))

Similarity is a paradigmatic relation between elements that can replace each other in the same context. In distributional semantics, a quantitative assessment of the similarity of two forms, lexemes, phrases, word senses or concepts is thus grounded in numerical representations of their respective contexts, i.e., their embeddings. In a broader sense of `embedding', also bags of words fall under the scope of <tt>frac:Embedding</tt>, see the usage note below.

Similarity is characterized by a similarity score (<tt>rdf:value</tt>), e.g., the number of shared dimensions/collocates (in a bag-of-word model) or the cosine distance between two word vectors (for fixed-size embeddings), the corpus used to generate this score (<tt>frac:observedIn</tt>), and the method used for calculating the score (<tt>dct:description</tt>).

Similarity is symmetric. The order of similes is irrelevant.

Like <tt>frac:Collocation</tt>, quantitative similarity relations are aggregates (containers, here `rdfs:Bag`s) of Observables.

<div class="entity">

> ----
> ### Similarity (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Similarity](http://www.w3.org/nl/lemon/frac#Similarity)
> **Similarity** is a <tt>frac:Observation</tt> about the relatedness between two or more <tt>frac:Embedding</tt>s, and it is characterized by a similarity score (<tt>rdf:value</tt>) in a specific source corpus (<tt>frac:observedIn</tt>) and a <tt>dct:description</tt> that explains the method of comparison.
> **SubClassOf:** <tt>frac:Observation, rdfs:Bag</tt>
> **rdfs:member:** only <tt>frac:Embedding</tt>
>
>---
</div>

```
frac:Similarity
    rdfs:subClassOf rdf:Bag, frac:Observation, [
        a owl:Restriction ;
        owl:minCardinality "2"^^xsd:nonNegativeInteger ;
        owl:onProperty rdfs:member
    ] ,
    [
       a <http://www.w3.org/2002/07/owl#Restriction> ;
        <http://www.w3.org/2002/07/owl#allValuesFrom> <http://www.w3.org/ns/lemon/frac#Embedding> ;
        <http://www.w3.org/2002/07/owl#onProperty> <http://www.w3.org/2000/01/rdf-schema#member>
    ] ;
    vs:term_status "stable" .
```

<tt>frac:Similarity</tt> applies to two different use cases: The specific similarity between (exactly) two words, and similarity clusters (synonym groups obtained from clustering quantitatively obtained synonym candidates according to their distributional semantics in a particular corpus) that can contain an arbitrary number of words. Both differ in the semantics of <tt>rdf:value</tt>: Quantitatively obtained similarity _relations_ normally provide a different score for every pair of similes. Within a similarity _cluster_, a generalization over these pair-wise scores must be provided. This could be the minimal similarity between all cluster members or a score produced by the clustering algorithm (e.g., depth or size of cluster). This must be explained in <tt>dct:description</tt>.

<div class="note">

> Similarity clusters are typical outcomes of [Word Sense Induction](https://www.cs.york.ac.uk/semeval2010_WSI/datasets.html) techniques or [unsupervised POS tagging](http://www.aclweb.org/anthology/D10-1056). Classical sample data are Brown clusters, e.g., [here](https://github.com/Derekkk/Brown-Word-Clustering-and-word-similarity/blob/master/results-brown.txt) or [here](https://s3-eu-west-1.amazonaws.com/downloads.gate.ac.uk/resources/derczynski-chester-boegh-brownpaths.tar.bz2).

</div>

<div class="note">

> <tt>Similarity</tt> is defined as a property of embeddings, not between <tt>ontolex:Element</tt>s. This excludes at least two important use cases:
> 
> *   manual similarity assessments as used for evaluating similarity assessments, and as created, for example, as part of psycholinguistic association or priming experiments (also cf. WordNet synsets, which provide, however, detailed lexicographic information in addition to similarity, and which thus to be represented as <tt>ontolex:LexicalConcept</tt>),
> *   similarity assessments obtained by other means than embeddings, e.g., by means of a traditional bag of words.
>
> In both (and similar) cases, the recommendation is to make use of (a resource-specific subclass of) <tt>frac:Embedding</tt>, nevertheless, and to document the specifics of the similarity relation and/or the embeddings in the <tt>dct:description</tt> of these embeddings. For the first use case, this approach can be justified by assuming that embeddings are correlated with a psycholinguistically `real' phenomenon. For the second use case, any bag of words can be interpreted as an infinite-size binary vector for which an embedding provides a fixed-size approximation.

</div>

<div class="note">

> As with frequency and embeddings, a resource-specific similarity type can be defined, analoguously. In particular, this is required if directed (asymmetric) similarity assessments are to be provided.

</div>

</section>

<section>

## Corpus Annotation (non-normative)
back to ([Table of Contents](#table-of-contents))

<div class="note">

The Ontolex Module for Frequency, Attestation and Corpus Information does not specify a vocabulary for annotating corpora or other data with lexical information, as this is being provided by the [Web Annotation Vocabulary](https://www.w3.org/TR/annotation-vocab/). The following description is non-normative as Web Annotation is defined in a separate W3C recommendation. The definitions below are reproduced, and refined only insofar as domain and range declarations have been refined to our usecase.

</div>

In Web Annotation terminology, the annotated element is the 'target', the content of the annotation is the `body', and the process and provenance of the annotation is expressed by properties of <tt>oa:Annotation</tt>.

<div class="entity">

> ---
>### oa:Annotation (Class)
> **IRI:** [http://www.w3.org/ns/oa#Annotation](http://www.w3.org/ns/oa#Annotation)
> **Required Predicates:** [oa:hasTarget](#hastarget), [rdf:type](#rdf-type), [oa:hasBody](#hasbody)
> **Recommended Predicates:** [oa:motivatedBy](#motivatedby), [dcterms:creator](#dcterms-creator), [dcterms:created](#dcterms-created)
> **Other Predicates:** [oa:styledBy](#styledby), [dcterms:issued](#dcterms-issued), [as:generator](#as-generator)
>
> ---
</div>

</div>


![](https://www.w3.org/TR/annotation-vocab/images/examples/annotation.png)
Fig. 5. oa:Annotation with properties

<div class="entity">

> ----
> ### oa:hasBody (Object Property)
> **IRI:** [http://www.w3.org/ns/oa#hasBody](http://www.w3.org/ns/oa#hasBody)
>  The object of the relationship is a resource that is a body of the Annotation. In the context of _lemon_, the body is an <tt>ontolex:Element</tt></div>
> **Domain:** oa:Annotation
> **Range:** ontolex:Element
>
> ---
</div>

![](https://www.w3.org/TR/annotation-vocab/images/examples/hasBody.png)
Fig. 6. oa:hasBody


<div class="entity">

> ----
>### oa:hasTarget (Object Property)
> **IRI:** [http://www.w3.org/ns/oa#hasTarget](http://www.w3.org/ns/oa#hasTarget)
>The relationship between an Annotation and its Target.
> **Domain:** oa:Annotation
>
>----
</div>

The Web Annotation Vocabulary supports different ways to define targets. This includes:

*   plain URI: The target can be a URI defined within the corpus (e.g., if corpus data is provided as native RDF, or by means of the <tt>@about</tt> attribute in an [HTML/XML+RDFa](https://www.w3.org/TR/rdfa-primer/) document, or by means of <tt>@xml:id</tt> in a [TEI/XML](http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.global.html) document).
*   string URI: String URIs provide the possibility to point directly to a text fragment in a web document, using the URI schemas as provided by [RFC5147](https://tools.ietf.org/html/rfc5147) (text files only) or [NIF](http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core/nif-core.html#introduction) (all text-based formats).
*   [oa:TextPositionSelector](https://www.w3.org/TR/annotation-vocab/#textpositionselector): a range of text defined by the start and end positions of the selection in the stream
*   [oa:DataPositionSelector](https://www.w3.org/TR/annotation-vocab/#datapositionselector): a range of data by recording the start and end positions of the selection in the stream
*   [oa:TextQuoteSelector](https://www.w3.org/TR/annotation-vocab/#textquoteselector): The TextQuoteSelector describes a range of text by copying it. The TextQuoteSelector can include some of the text immediately before (a prefix) and after (a suffix) it to distinguish between multiple copies of the same sequence of characters. If this does suffice for disambiguation, all matching text fragments in the document are being annotated.
*   [oa:XPathSelector](https://www.w3.org/TR/annotation-vocab/#xpathselector): select elements and content within a resource that supports the Document Object Model via a specified XPath value.
*   [oa:RangeSelector](https://www.w3.org/TR/annotation-vocab/#rangeselector): identify the beginning and the end of the selection by using other Selectors.

<div class="note">

> <tt>oa:Annotation</tt> explicitly allows _n:m_ relations between <tt>ontolex:Element</tt>s and elements in the annotated elements. It is thus sufficient for every <tt>ontolex:Element</tt> to appear in one <tt>oa:hasBody</tt> statement in order to produce a full annotation of the corpus.

</div>

<div class="note">

> As for frequency, embeddings, etc., resource-specific annotation classes can be defined by <tt>owl:Restriction</tt> so that modelling effort and verbosity are reduced. These should follow the same conventions.

</div>

</section>

<section>

# Usage guidelines
back to ([Table of Contents](#table-of-contents))

<section>

## Resource-specific subclasses of FrAC concepts
back to ([Table of Contents](#table-of-contents))

As corpus-derived information requires provenance and other metadata, the frac module uses reification (class-based modelling) for concepts such as frequency or embeddings. In a data set, this information will be recurring, and for redundancy reduction, we recommend to provide resource-specific subclasses of frac concepts that provide metadata by means of <tt>owl:Restriction</tt>s that provide the value for the respective properties. This was illustrated above for the relevant frac classes.

As a rule of best practice, we recommend for such cases to provide (a copy of) the OWL definitions of resource-specific classes _in the same graph (and file) as the data_. Within the graph containing the data, the following SPARQL 1.1 query _must_ return the full frac definition of all instances of, say, <tt>:EPSDFrequency</tt> (see examples above):

<div class="beispiel">

<div>

    CONSTRUCT {
        ?data a ?class, ?sourceClass; ?property ?value.
    } WHERE {
      ?data a ?sourceClass.                   # e.g., [] a :EPSDFrequency
      ?sourceClass (rdfs:subClassOf|owl:equivalentClass)* ?class.
      FILTER(strstarts(str(?class),'http://www.w3.org/ns/lemon/frac#'))
        # ?class: all superclasses of ?sourceClass which are in the frac namespace
      { # return all value restrictions
          ?class (rdfs:subClassOf|owl:equivalentClass)* ?restriction.
          ?restriction a owl:Restriction.
          ?restriction owl:onProperty ?property.
          ?restriction owl:hasValue ?value.
      } UNION {
        # return all directly expressed values
          ?data ?property ?value.
          FILTER(?property in (frac:observedIn,rdf:value))
          # TODO: update list of properties
      }
    }

</div>

</div>

This query can be used as a test for _frac_ compliancy, and for property `inference'. Note that it does not support <tt>owl:intersection</tt> nor <tt>owl:join</tt>, nor <tt>owl:sameAs</tt>.

<div class="note">

> We use the OWL2/DL vocabulary for modelling restrictions. However, _lemon_ is partially compatible with OWL2/DL only in that several modules use <tt>rdf:List</tt> -- which is a reserved construct in OWL2\. Therefore, the primary means of accessing and manipulation _lemon_ and _ontolex-frac_ data is by means of SPARQL, resp., RDF- (rather than OWL-) technology. In particular, we do not guarantee nor require that OWL2/DL inferences can be used for validating or querying _lemon_ and _ontolex-frac_ data.

</div>

> Note: **TODO** analoguous example for corpus-specific collocations

</section>

<section>

## RDF Serializations and CSV
back to ([Table of Contents](#table-of-contents))

Usually, numerical information drawn from corpora is distributed and shared as comma-separated values (CSV), e.g., ngram lists or embeddings. Ontolex-frac as an RDF vocabulary is agnostic about its serialization (RDF/TTL, RDF/XML, JSON-LD, etc.), but in particular, it is compliant with CSV and related tabular formats by means of W3C recommendations such as [CSV2RDF](https://www.w3.org/TR/csv2rdf/), [RDB Direct Mapping](https://www.w3.org/TR/rdb-direct-mapping/) and the [RDB to RDF Mapping Language](https://www.w3.org/TR/r2rml/). For corpus-derived lexical-semantic information which is typically distributed in CSV, the best practice is to continue to do so, but to provide a mapping to Ontolex-frac as this provides a vocabulary for their interpretation as Linked Data, and thus establishes an interoperability layer over the raw data without creating additional overhead.

<div class="note">

Ontolex-frac is compliant with CSV formats, but its handling of structured information has an impact on the CSV format. In particular, individual dimensions of embeddings must not use comma as separator in order to be mapped to a single literal. For the example embedding of _frak_ above, the first column (containing the word) should be comma-separated, the following columns (containing the embedding) should be white-space separated.

</div>

</section>

</section>

# Acknowledgements
back to ([Table of Contents](#table-of-contents))

TBC

# References
back to ([Table of Contents](#table-of-contents))

<div class="note">

from lexicog, to be revised

</div>

<dt id="bib-mccrae-lemon">[1]</dt>

<dd>J. McCrae, G. Aguado-de Cea, P. Buitelaar, P. Cimiano, T. Declerck, A. Gómez-Pérez, J. Gracia, L. Hollink, E. Montiel-Ponsoda, D. Spohr, and T. Wunner, [<cite>"Interchanging lexical resources on the Semantic Web"</cite>](http://dx.doi.org/10.1007/s10579-012-9182-3). Language Resources and Evaluation, vol. 46, 2012.</dd>

<dt id="bib-klimek-kdict">[2]</dt>

<dd>B. Klimek and M. Brümmer, <cite>"Enhancing lexicography with semantic language databases"</cite> Kernerman Dictionary News, 23, 5-10\. 2015.</dd>

<dt id="bib-gracia-apertium">[3]</dt>

<dd>J. Gracia, M. Villegas, A. Gómez-Pérez, and N. Bel, <cite>"The apertium bilingual dictionaries on the web of data"</cite> Semantic Web Journal, vol. 9, no. 2, pp. 231-240, Jan. 2018.</dd>

<dt id="bib-bosque-kdict">[4]</dt>

<dd>J. Bosque-Gil, J. Gracia, E. Montiel-Ponsoda, and G. Aguado-de Cea, <cite>"Modelling multilingual lexicographic resources for the web of data: the k dictionaries case"</cite> in Proc. of GLOBALEX'16 workshop at LREC'15, Portoroz, Slovenia, May 2016.</dd>

<dt id="bib-kahn-diachronic">[5]</dt>

<dd>F. Khan, J. E. Díaz-Vera, and M. Monachini, <cite>"Representing Polysemy and Diachronic Lexico-Semantic Data on the Semantic Web"</cite> In SWASH at ESWC (2016)</dd>

<dt id="bib-declerck-dialectal">[6]</dt>

<dd>T. Declerck and E. Wandl-Vogt, <cite>"Cross-linking Austrian dialectal Dictionaries through formalized Meanings"</cite> In Proceedings of the XVI EURALEX International Congress, pp. 329-343\. 2014.</dd>

<dt id="bib-abromeit-etymological">[7]</dt>

<dd>F. Abromeit, C. Chiarcos, C. Fäth and M. Ionov, <cite>"Linking the Tower of Babel: Modelling a Massive Set of Etymological Dictionaries as RDF"</cite> In LDL 2016 5th Workshop on Linked Data in Linguistics: Managing, Building and Using Linked Language Resources (p. 11). May 2016.</dd>

<dt id="bib-bosque-lexicography">[8]</dt>

<dd>J. Bosque-Gil, J. Gracia, and A. Gómez-Pérez, <cite>"Linked data in lexicography"</cite> Kernerman Dictionary News, pp. 19-24, Jul. 2016.</dd>

<dt id="bib-declerck-paneuropean">[9]</dt>

<dd>T. Declerck, E. Wandl-Vogt, and K. Mörth, <cite>"Towards a Pan European Lexicography by Means of Linked (Open) Data"</cite> In Electronic lexicography in the 21st century: linking lexical data in the digital age. Proceedings of the eLex 2015 conference (pp. 342-355), 2015.</dd>

<dt id="bib-bosque-module">[10]</dt>

<dd>J. Bosque-Gil, J. Gracia, and E. Montiel-Ponsoda, [<cite>"Towards a module for lexicography in OntoLex"</cite> ](http://ceur-ws.org/Vol-1899/OntoLex_2017_paper_5.pdf)in Proc. of the LDK workshops: OntoLex, TIAD and Challenges for Wordnets at 1st Language Data and Knowledge conference (LDK 2017), Galway, Ireland, vol. 1899\. CEUR-WS, pp. 74-84, Jun 2017.</dd>

<dt id="bib-parvizi-oxford">[11]</dt>

<dd>A. Parvizi, M. Kohl, M. González, R. Saurí, <cite>"Towards a Linguistic Ontology with an Emphasis on Reasoning and Knowledge Reuse"</cite> Language Resources and Evaluation Conference (LREC), May 2016.</dd>

<dt id="bib-gracia-native">[12]</dt>

<dd>J. Gracia, I. Kernerman, and J. Bosque-Gil, [<cite>"Toward linked data-native dictionaries"</cite>]( https://elex.link/elex2017/wp-content/uploads/2017/09/paper33.pdf) in. Proc. of eLex 2017 conference (Electronic lexicography in the 21st century), in Leiden, Netherlands. Lexical Computing CZ s.r.o., pp. 550-559, Sep. 2017.</dd>

<dt id="bib-stolk-onomasiological">[13]</dt>

<dd>S. Stolk, <cite>"OntoLex and Onomasiological Ordering: Supporting Topical Thesauri"</cite> in Proc. of the LDK2017 Workshops, NUI Galway, Ireland, 18 June (pp. 60-67), 2017.</dd>

<dt id="bib-elmaarouf-verbs">[14]</dt>

<dd>I. El Maarouf, J. Bradbury, and P. Hanks, <cite>"PDEV-lemon: a Linked Data implementation of the Pattern Dictionary of English Verbs based on the Lemon model"</cite>. In 3rd Workshop on Linked Data in Linguistics: Multilingual Knowledge Resources and Natural Language Processing (p. 88). 2014.</dd>

<dt id="bib-kahn-citations">[15]</dt>

<dd>F. Khan and F. Boschetti, <cite>"Towards a Representation of Citations in Linked Data Lexical Resources"</cite> In proc. of the XVIII EURALEX International Congress (EURALEX 2018). 2018</dd>

<dt id="american-heritage-dict">[16]</dt>

<dd><cite>animal. American Heritage Dictionary. Houghton Mifflin Harcourt, 1994.</cite> Last accessed 28.10.18.</dd>

<dt id="RAE-dict">[17]</dt>

<dd><cite>blanco. Diccionario de la Lengua Española (DLE). Versión electrónica de la 23\. Edición. December 2017.</cite> Last accessed 28.10.18.</dd>

<dt id="OED-dict-air">[18]</dt>

<dd><cite>air. Oxford English Living Dictionaries Online.</cite> Last accessed 01.11.18\. https://en.oxforddictionaries.com/definition/air <script>setTimeout(function(){CodeMirror.colorize();}, 20);</script></dd>

